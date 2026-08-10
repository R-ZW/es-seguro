import re


class ValidationError(ValueError):
    # Erro usado quando a entrada enviada pelo cliente não passa na validação.
    pass


class AuthorizationError(PermissionError):
    # Erro usado quando o usuário autenticado não tem permissão para a ação.
    pass


CATALOG = {
    # Preços ficam em centavos inteiros para evitar problemas de arredondamento.
    "HAMBURGUER": {"name": "Hambúrguer", "price_cents": 1000, "active": True},
    "SUCO": {"name": "Suco", "price_cents": 500, "active": True},
}


def insecure_create_order(payload):
    """Exemplo inseguro: confia nos valores enviados pelo cliente."""
    # Falha proposital: aceita o total informado no app, que é um ambiente não confiável.
    return {
        "items": payload.get("items", []),
        "total_cents": payload.get("total_cents", 0),
    }


def secure_create_order(payload, catalog=None):
    """Exemplo seguro: valida a entrada e calcula os preços no servidor."""
    catalog = catalog or CATALOG

    # Primeiro valida o formato geral do payload recebido.
    if not isinstance(payload, dict):
        raise ValidationError("Payload must be an object.")

    # Allowlist de campos: o cliente só pode enviar itens, nunca preço ou total.
    if set(payload.keys()) != {"items"}:
        raise ValidationError("Unexpected order fields.")

    items = payload.get("items")
    # Limita tamanho do pedido para evitar entradas vazias ou abusivas.
    if not isinstance(items, list) or not 1 <= len(items) <= 50:
        raise ValidationError("Order must contain between 1 and 50 items.")

    normalized_items = []
    total = 0
    # Regex restritiva para impedir IDs malformados ou payloads com caracteres inesperados.
    item_id_pattern = re.compile(r"^[A-Z0-9_-]{3,40}$")

    for item in items:
        if not isinstance(item, dict):
            raise ValidationError("Each item must be an object.")

        item_id = item.get("item_id")
        quantity = item.get("quantity")

        if not isinstance(item_id, str) or not item_id_pattern.fullmatch(item_id):
            raise ValidationError("Invalid item identifier.")

        # Validação semântica: além do formato, o item precisa existir e estar ativo.
        if item_id not in catalog or not catalog[item_id]["active"]:
            raise ValidationError("Item is unavailable.")

        # Quantidade também é regra de negócio e precisa ser validada no servidor.
        if not isinstance(quantity, int) or not 1 <= quantity <= 20:
            raise ValidationError("Invalid item quantity.")

        # O preço usado vem do catálogo interno, não da requisição do cliente.
        unit_price = catalog[item_id]["price_cents"]
        total += unit_price * quantity
        normalized_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "unit_price_cents": unit_price,
            }
        )

    return {
        "items": normalized_items,
        "total_cents": total,
    }


def insecure_authorize_order_action(user, order, action):
    """Exemplo inseguro: assume que qualquer usuário autenticado pode executar a ação."""
    # Falha proposital: estar logado não significa estar autorizado para qualquer pedido.
    return bool(user)


def secure_authorize_order_action(user, order, action):
    """Exemplo seguro: verifica papel e relação com o pedido solicitado."""
    # Requisições sem usuário ou pedido válido são negadas antes de qualquer regra.
    if not isinstance(user, dict) or not isinstance(order, dict):
        raise AuthorizationError("Access denied.")

    role = user.get("role")
    user_id = user.get("id")

    # Deny by default: só vira True quando alguma regra explícita permitir.
    allowed = False

    # Admin pode executar ações administrativas, mas apenas dentro da lista prevista.
    if role == "admin":
        allowed = action in {"read", "update_status", "refund"}

    # Cliente só pode ler pedidos que pertencem à própria conta.
    elif role == "cliente":
        allowed = action == "read" and order.get("customer_id") == user_id

    # Estabelecimento só pode ler/atualizar pedidos vinculados ao próprio cadastro.
    elif role == "estabelecimento":
        allowed = (
            action in {"read", "update_status"}
            and order.get("establishment_id") == user_id
        )

    # Entregador só pode ler/atualizar pedidos atribuídos a ele.
    elif role == "entregador":
        allowed = (
            action in {"read", "update_status"}
            and order.get("delivery_person_id") == user_id
        )

    # Se nenhuma regra permitiu, a requisição é bloqueada.
    if not allowed:
        raise AuthorizationError("Access denied.")

    return True
