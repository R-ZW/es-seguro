## 18.1 Requisitos de segurança

Esta seção traduz as ameaças e riscos previamente priorizados em requisitos de segurança acionáveis. Cada requisito define uma restrição ou comportamento obrigatório para o sistema, acompanhado de um critério de verificação claro para garantir sua correta implementação e validação durante o ciclo de desenvolvimento

| ID | Risco de origem | Requisito de segurança | Critério de verificação |
|---|---|---|---|
| **RS01** | R01 — Uso indevido da conta de um cliente | O sistema deverá exigir autenticação adicional (reautenticação ou MFA/segundo fator) antes de confirmar operações sensíveis ou financeiras vinculadas à conta do cliente. | A operação deve ser bloqueada e um alerta de segurança registrado em log caso o desafio de autenticação adicional não seja concluído com sucesso. |
| **RS02** | R04 — Manipulação do valor do pedido | O backend deverá recalcular e validar o valor total do pedido de forma autônoma, utilizando a base de preços, taxas e regras de negócio armazenadas no servidor. | A requisição de finalização de pedido deve ser rejeitada (ou os valores sobrescritos pela versão do servidor) se o total enviado pelo frontend divergir do cálculo do backend. |
| **RS03** | R11 — Acesso a informações da conta e pedidos de outro usuário | A API deverá implementar validação de autorização a nível de objeto (BOLA/IDOR), garantindo que o usuário autenticado seja o legítimo proprietário do recurso acessado. | Requisições que manipulem ou consultem IDs de recursos pertencentes a terceiros devem retornar erro de autorização (ex.: `HTTP 403 Forbidden` ou `404 Not Found`) e gerar evento de auditoria. |
| **RS04** | R23 — Acesso não autorizado às funções administrativas | O servidor deverá validar rigorosamente o perfil (role) do usuário antes de conceder acesso a endpoints, funções ou relatórios de nível administrativo. | Tentativas de acesso a endpoints administrativos por contas sem a role correspondente no token/sessão devem ser sumariamente negadas (`HTTP 403 Forbidden`) e monitoradas. |

---