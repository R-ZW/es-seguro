import unittest

from exemplos.app_security import (
    AuthorizationError,
    ValidationError,
    insecure_authorize_order_action,
    insecure_create_order,
    secure_authorize_order_action,
    secure_create_order,
)


class SecureCodeExamplesTest(unittest.TestCase):
    def print_case(self, test_id, practice, action, expected, observed):
        # Impressão didática para demonstrar o teste durante a apresentação.
        print()
        print(f"[{test_id}] {practice}")
        print(f"Entrada ou ação: {action}")
        print(f"Resultado esperado: {expected}")
        print(f"Resultado observado: {observed}")

    def test_pedido_inseguro_confia_no_total_do_cliente(self):
        # Demonstra a vulnerabilidade: o cliente manipula o total para 1 centavo.
        payload = {
            "items": [{"item_id": "HAMBURGUER", "quantity": 2}],
            "total_cents": 1,
        }

        order = insecure_create_order(payload)

        self.print_case(
            "TS01-INSEGURO",
            "Validação de entrada e valor do pedido",
            "Cliente envia 2 HAMBURGUER de R$ 10,00, mas informa total_cents = 1",
            "Na versão insegura, o sistema aceita o valor manipulado.",
            f"Pedido criado com total_cents = {order['total_cents']}",
        )
        self.assertEqual(order["total_cents"], 1)

    def test_pedido_seguro_calcula_total_no_servidor(self):
        # Caso válido: sem preço no payload, o servidor calcula pelo catálogo interno.
        payload = {
            "items": [{"item_id": "HAMBURGUER", "quantity": 2}],
        }

        order = secure_create_order(payload)

        self.print_case(
            "TS01-SEGURO",
            "Validação de entrada e valor do pedido",
            "Cliente envia pedido válido com 2 HAMBURGUER de R$ 10,00",
            "O servidor calcula 2000 centavos usando o catálogo interno.",
            f"Pedido criado com total_cents = {order['total_cents']}",
        )
        self.assertEqual(order["total_cents"], 2000)

    def test_pedido_seguro_rejeita_campo_total_do_cliente(self):
        # Caso malicioso: o cliente tenta enviar um campo que não deveria controlar.
        payload = {
            "items": [{"item_id": "HAMBURGUER", "quantity": 2}],
            "total_cents": 1,
        }

        # A versão segura rejeita o payload antes de criar o pedido.
        with self.assertRaises(ValidationError):
            secure_create_order(payload)
        self.print_case(
            "TS02-SEGURO",
            "Validação de entrada e valor do pedido",
            "Cliente tenta enviar total_cents = 1 no payload",
            "O campo inesperado deve ser recusado; o cliente não define preço.",
            "ValidationError gerado corretamente",
        )

    def test_pedido_seguro_rejeita_entrada_invalida(self):
        # Caso inválido: item_id com caracteres suspeitos e quantidade fora do limite.
        payload = {
            "items": [{"item_id": "HAMBURGUER;DROP", "quantity": 999}],
        }

        with self.assertRaises(ValidationError):
            secure_create_order(payload)
        self.print_case(
            "TS02B-SEGURO",
            "Validação de entrada e valor do pedido",
            "Cliente envia item_id malformado e quantidade 999",
            "O pedido deve ser recusado antes do processamento.",
            "ValidationError gerado corretamente",
        )

    def test_autorizacao_insegura_permite_idor(self):
        # Demonstra IDOR: usuário autenticado acessa pedido de outro cliente.
        user = {"id": "cli-2", "role": "cliente"}
        order = {"id": "ord-1", "customer_id": "cli-1"}

        allowed = insecure_authorize_order_action(user, order, "read")
        self.print_case(
            "TS04-INSEGURO",
            "Controle de autorização no backend",
            "Cliente cli-2 tenta ler pedido do cliente cli-1",
            "Na versão insegura, qualquer usuário autenticado é aceito.",
            f"Acesso permitido = {allowed}",
        )
        self.assertTrue(allowed)

    def test_autorizacao_segura_permite_dono_do_pedido(self):
        # Caso válido: cliente acessa o próprio pedido.
        user = {"id": "cli-1", "role": "cliente"}
        order = {"id": "ord-1", "customer_id": "cli-1"}

        allowed = secure_authorize_order_action(user, order, "read")
        self.print_case(
            "TS03-SEGURO",
            "Controle de autorização no backend",
            "Cliente cli-1 acessa pedido cujo customer_id também é cli-1",
            "A solicitação deve ser permitida.",
            f"Acesso permitido = {allowed}",
        )
        self.assertTrue(allowed)

    def test_autorizacao_segura_bloqueia_outro_cliente(self):
        # Caso não autorizado: cliente tenta acessar pedido que não pertence a ele.
        user = {"id": "cli-2", "role": "cliente"}
        order = {"id": "ord-1", "customer_id": "cli-1"}

        with self.assertRaises(AuthorizationError):
            secure_authorize_order_action(user, order, "read")
        self.print_case(
            "TS04-SEGURO",
            "Controle de autorização no backend",
            "Cliente cli-2 tenta ler pedido cujo customer_id é cli-1",
            "A solicitação deve ser recusada com erro de autorização.",
            "AuthorizationError gerado corretamente",
        )

    def test_autorizacao_segura_bloqueia_acao_admin_para_cliente(self):
        # Caso não autorizado: dono do pedido ainda não pode executar ação administrativa.
        user = {"id": "cli-1", "role": "cliente"}
        order = {"id": "ord-1", "customer_id": "cli-1"}

        with self.assertRaises(AuthorizationError):
            secure_authorize_order_action(user, order, "refund")
        self.print_case(
            "TS04B-SEGURO",
            "Controle de autorização no backend",
            "Cliente cli-1 tenta executar refund no próprio pedido",
            "A ação administrativa deve ser recusada para cliente comum.",
            "AuthorizationError gerado corretamente",
        )


if __name__ == "__main__":
    unittest.main()
