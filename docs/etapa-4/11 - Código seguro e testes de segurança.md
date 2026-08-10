### 11.1 Objetivo

O objetivo desta etapa é demonstrar como decisões de arquitetura definidas anteriormente podem virar práticas simples de implementação segura.

Foram selecionadas apenas **duas práticas de código seguro**, ambas ligadas aos riscos priorizados nas etapas anteriores e às decisões discutidas na Etapa 3. Não foi implementado o sistema completo. Os exemplos são genéricos e servem apenas para demonstrar a diferença entre uma implementação insegura e uma implementação segura.

### 11.2 Práticas selecionadas

| Prática | Risco relacionado | Motivo da escolha |
| --- | --- | --- |
| **Validação de entrada e recálculo do valor do pedido no servidor** | R04 — Manipulação do valor do pedido | É simples de demonstrar e mostra claramente por que o backend não deve confiar em valores enviados pelo cliente. |
| **Controle de autorização no backend** | R11 — Acesso a informações da conta e pedidos de outro usuário; R23 — Acesso não autorizado às funções administrativas | É um caso clássico de broken access control/IDOR e pode ser demonstrado com poucas regras de papel e propriedade do recurso. |

Os exemplos estão em:

- `src/etapa-4/exemplos/app_security.py`
- `src/etapa-4/tests/test_app_security.py`

---

## 11.3 Prática 1 — Validação de entrada e recálculo do valor do pedido

### Risco e requisito relacionados

| Item | Descrição |
| --- | --- |
| **Risco** | R04 — O valor final de um pedido é reduzido ou alterado indevidamente durante a finalização da compra. |
| **Requisito seguro** | O servidor deve validar os itens e quantidades recebidos e recalcular o valor total usando preços armazenados no backend. |
| **Referência OWASP** | OWASP Input Validation Cheat Sheet. A referência recomenda validar entradas em nível sintático e semântico, preferencialmente no início do fluxo, e tratar dados externos como não confiáveis. |

### Testes antes da implementação

| Teste | Entrada ou ação | Resultado seguro esperado |
| --- | --- | --- |
| **TS01** | Cliente envia pedido válido com 2 unidades de `HAMBURGUER`, cada uma com preço padrão de R$ 10,00 | O servidor calcula `2000` centavos a partir do catálogo interno. |
| **TS02** | Cliente tenta enviar o campo `total_cents = 1` no payload | A solicitação é recusada porque o cliente não pode definir o valor do pedido. |

### Implementação sem segurança

Na versão insegura, o backend simplesmente aceita o valor enviado pelo cliente:

```python
def insecure_create_order(payload):
    return {
        "items": payload.get("items", []),
        "total_cents": payload.get("total_cents", 0),
    }
```

Problema: um cliente mal-intencionado poderia interceptar a requisição e trocar o valor total do pedido por `1` centavo.

### Implementação segura

Na versão segura, o backend valida a estrutura do pedido, confere se os itens existem no catálogo, limita a quantidade e calcula o total usando preços confiáveis do servidor. No exemplo, o catálogo possui `HAMBURGUER` com preço padrão de `1000` centavos, equivalente a R$ 10,00:

```python
CATALOG = {
    "HAMBURGUER": {"name": "Hambúrguer", "price_cents": 1000, "active": True},
    "SUCO": {"name": "Suco", "price_cents": 500, "active": True},
}
```

O valor é armazenado em centavos inteiros para evitar problemas de arredondamento com números decimais em operações financeiras:

```python
def secure_create_order(payload, catalog):
    if set(payload.keys()) != {"items"}:
        raise ValidationError("Unexpected order fields.")

    total = 0

    for item in payload["items"]:
        item_id = item["item_id"]
        quantity = item["quantity"]

        if item_id not in catalog:
            raise ValidationError("Item is unavailable.")
        if quantity < 1 or quantity > 20:
            raise ValidationError("Invalid item quantity.")

        total += catalog[item_id]["price_cents"] * quantity

    return {"total_cents": total}
```

### Resultado esperado

- pedidos válidos são aceitos;
- entradas malformadas são recusadas;
- o total do pedido é calculado pelo servidor;
- valores enviados pelo cliente não são usados como fonte de verdade.

---