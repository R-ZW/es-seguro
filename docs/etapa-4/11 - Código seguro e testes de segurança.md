# `Yummers` - Aplicativo de delivery

### Conteúdo da página:

> [11.1 Objetivo](#111-objetivo)<br>
> [11.2 Práticas selecionadas](#112-práticas-selecionadas)<br>
> [11.3 Prática 1 — Validação de entrada e recálculo do valor do pedido](#113-prática-1--validação-de-entrada-e-recálculo-do-valor-do-pedido)<br>
> [11.4 Prática 2 — Controle de autorização no backend](#114-prática-2--controle-de-autorização-no-backend)<br>
> [11.5 Testes automatizados](#115-testes-automatizados)<br>
> [11.6 Referências utilizadas](#116-referências-utilizadas)<br>
> [11.7 Conclusão da Etapa 4](#117-conclusão-da-etapa-4)<br>

---

## 💻 11. Código seguro e testes de segurança

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

## 11.4 Prática 2 — Controle de autorização no backend

### Risco e requisito relacionados

| Item | Descrição |
| --- | --- |
| **Riscos** | R11 — Usuário acessa dados ou pedidos de outro usuário; R23 — Usuário sem privilégio acessa funções administrativas. |
| **Requisito seguro** | Toda requisição deve passar por uma checagem de autorização no servidor, considerando o papel do usuário e sua relação com o recurso acessado. |
| **Referência OWASP** | OWASP Authorization Cheat Sheet. A referência recomenda negar por padrão, validar permissões em cada requisição e não depender apenas da interface do usuário. |

### Testes antes da implementação

| Teste | Entrada ou ação | Resultado seguro esperado |
| --- | --- | --- |
| **TS03** | Cliente `cli-1` acessa o pedido cujo `customer_id` é `cli-1` | A solicitação é permitida. |
| **TS04** | Cliente `cli-2` tenta acessar pedido cujo `customer_id` é `cli-1` ou cliente comum tenta executar `refund` | A solicitação é recusada com erro de autorização. |

### Implementação sem segurança

Na versão insegura, o sistema só verifica se existe algum usuário autenticado:

```python
def insecure_authorize_order_action(user, order, action):
    return bool(user)
```

Problema: qualquer cliente autenticado poderia alterar o identificador do pedido na requisição e consultar dados de outro cliente.

### Implementação segura

Na versão segura, a autorização é feita no servidor. O sistema verifica a `role` do usuário e se ele possui relação direta com o pedido:

```python
def secure_authorize_order_action(user, order, action):
    if user["role"] == "admin":
        return True

    if user["role"] == "cliente":
        return action == "read" and order["customer_id"] == user["id"]

    raise AuthorizationError("Access denied.")
```

No exemplo completo, também há regras para `estabelecimento` e `entregador`.

### Resultado esperado

- autenticação e autorização ficam separadas;
- usuários autenticados não acessam automaticamente qualquer recurso;
- pedidos de terceiros são protegidos contra IDOR;
- funções administrativas continuam restritas a usuários com papel adequado.

---

## 11.5 Testes automatizados

Foram implementados testes executáveis para demonstrar o comportamento das versões insegura e segura.

| Teste automatizado | O que demonstra |
| --- | --- |
| `test_pedido_inseguro_confia_no_total_do_cliente` | A versão insegura aceita o total manipulado pelo cliente. |
| `test_pedido_seguro_calcula_total_no_servidor` | A versão segura calcula o valor correto no servidor. |
| `test_pedido_seguro_rejeita_campo_total_do_cliente` | A versão segura rejeita o campo `total_cents` enviado pelo cliente. |
| `test_pedido_seguro_rejeita_entrada_invalida` | A versão segura rejeita entrada malformada. |
| `test_autorizacao_insegura_permite_idor` | A versão insegura permite acesso indevido por usuário autenticado. |
| `test_autorizacao_segura_permite_dono_do_pedido` | A versão segura permite acesso ao dono do pedido. |
| `test_autorizacao_segura_bloqueia_outro_cliente` | A versão segura bloqueia acesso a pedido de outro cliente. |
| `test_autorizacao_segura_bloqueia_acao_admin_para_cliente` | A versão segura bloqueia ação administrativa executada por cliente comum. |

Comando:

```bash
python -m unittest discover -s tests
```

Para exibir os nomes dos testes e os prints demonstrando entrada, resultado esperado e resultado observado:

```bash
python -m unittest discover -s tests -v
```

Resultado esperado:

```text
Ran 8 tests
OK
```

### 11.6 Referências utilizadas

- OWASP Cheat Sheet Series — Input Validation Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- OWASP Cheat Sheet Series — Authorization Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

### 11.7 Conclusão da Etapa 4

A Etapa 4 demonstrou duas práticas de código seguro ligadas diretamente aos riscos anteriores. A primeira impede manipulação de preço ao recalcular valores no servidor. A segunda impede acesso indevido ao validar autorização no backend.

A comparação entre implementação insegura e segura deixa claro que o problema não está apenas na interface, mas na confiança indevida em dados e ações vindas do cliente. Por isso, as validações precisam ocorrer no servidor e devem ser verificadas por testes de segurança.

---
<center>
<table width="100%">
<tr>
<td align="left">

[⬅️ Página anterior](../etapa-3/10%20-%20Arquitetura%20segura.md)

</td>

<td align="center">

9️⃣

</td>

<td align="right">

[Próxima página ➡️](../etapa-5/12%20-%20Verificação%20de%20vulnerabilidades.md)

</td>
</tr>
</table>
</center>

### **Índice**:

**Etapa 1**:

1. [**🆔 Identificação do sistema**](../../README.md)
2. [**📝 Descrição do sistema**](../../README.md)
3. [**👥 Usuários, ativos e pontos de interação**](../etapa-1/3%20-%20Usuários,%20ativos%20e%20pontos%20de%20interação.md)
4. [**🔀 Visão geral da arquitetura e fluxos de uso**](../etapa-1/4%20-%20Visão%20geral%20da%20arquitetura%20e%20fluxos%20de%20uso.md) 
5. [**🎯 Modelagem de ameaças com STRIDE**](../etapa-1/5%20-%20Modelagem%20de%20ameaças%20com%20STRIDE.md)
6. [**🚨 Casos de abuso**](../etapa-1/6%20-%20Casos%20de%20abuso.md)
7. [**📌 Considerações finais da Etapa 1**](../etapa-1/7%20-%20Considerações%20finais%20da%20Etapa%201.md)


**Etapa 2**:

8. [**🛡️ Análise e priorização dos riscos**](../etapa-2/8%20-%20Análise%20e%20priorização%20dos%20riscos.md)
9. [**🧩 Tratamento dos riscos com NIST CSF**](../etapa-2/#9-tratamento-dos-riscos-com-nist-csf)


**Etapa 3**:

10. [**🏗️ Arquitetura segura**](../etapa-3/10%20-%20Arquitetura%20segura.md)


**Etapa 4**:

11. [**💻 Código seguro e testes de segurança**](#) 👈


**Etapa 5**:

12. [**🔎 Verificação de vulnerabilidades**](../etapa-5/12%20-%20Verificação%20de%20vulnerabilidades.md)


**Etapa 6**:

13. [**📡 Monitoramento e detecção de intrusões**](../../roteiros/etapa-6-deteccao-de-intrusoes.md)


**Etapa 7**:

14. [**🎥 DevSecOps e vídeo final**](../../roteiros/etapa-7-devsecops-e-video-final.md)

---