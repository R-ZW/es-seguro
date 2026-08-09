## 18.1 Requisitos de segurança

Esta seção traduz as ameaças e riscos previamente priorizados em requisitos de segurança acionáveis. Cada requisito define uma restrição ou comportamento obrigatório para o sistema, acompanhado de um critério de verificação claro para garantir sua correta implementação e validação durante o ciclo de desenvolvimento

| ID | Risco de origem | Requisito de segurança | Critério de verificação |
|---|---|---|---|
| **RS01** | R01 — Uso indevido da conta de um cliente | O sistema deverá exigir autenticação adicional (reautenticação ou MFA/segundo fator) antes de confirmar operações sensíveis ou financeiras vinculadas à conta do cliente. | A operação deve ser bloqueada e um alerta de segurança registrado em log caso o desafio de autenticação adicional não seja concluído com sucesso. |
| **RS02** | R04 — Manipulação do valor do pedido | O backend deverá recalcular e validar o valor total do pedido de forma autônoma, utilizando a base de preços, taxas e regras de negócio armazenadas no servidor. | A requisição de finalização de pedido deve ser rejeitada (ou os valores sobrescritos pela versão do servidor) se o total enviado pelo frontend divergir do cálculo do backend. |
| **RS03** | R11 — Acesso a informações da conta e pedidos de outro usuário | A API deverá implementar validação de autorização a nível de objeto (BOLA/IDOR), garantindo que o usuário autenticado seja o legítimo proprietário do recurso acessado. | Requisições que manipulem ou consultem IDs de recursos pertencentes a terceiros devem retornar erro de autorização (ex.: `HTTP 403 Forbidden` ou `404 Not Found`) e gerar evento de auditoria. |
| **RS04** | R23 — Acesso não autorizado às funções administrativas | O servidor deverá validar rigorosamente o perfil (role) do usuário antes de conceder acesso a endpoints, funções ou relatórios de nível administrativo. | Tentativas de acesso a endpoints administrativos por contas sem a role correspondente no token/sessão devem ser sumariamente negadas (`HTTP 403 Forbidden`) e monitoradas. |

---

## 18.2 Vulnerabilidades catalogadas

Para fundamentar as estratégias de mitigação, esta seção mapeia os principais riscos identificados a vulnerabilidades e fraquezas de segurança reconhecidas pelo mercado. A utilização de catálogos padronizados, como OWASP e CWE, facilita a compreensão técnica do problema e orienta a equipe na adoção de práticas de desenvolvimento seguro.

| Risco | Vulnerabilidade ou categoria | Referência utilizada | Relação com o sistema |
|---|---|---|---|
| **R01 — Uso indevido da conta de um cliente** | Falha de autenticação e gerenciamento de sessão | CWE-287 (Improper Authentication) / OWASP Top 10 A07:2021 – Identification and Authentication Failures / OWASP ASVS V3 | Permite que um atacante que obtenha o token de sessão ou credenciais de um cliente realize compras com os meios de pagamento salvos, devido à falta de verificação de identidade no momento da transação. |
| **R04 — Manipulação do valor do pedido** | Confiança excessiva em dados controlados pelo cliente (Validação insuficiente) | CWE-602 (Client-Side Enforcement of Server-Side Security) / OWASP Top 10 A08:2021 – Software and Data Integrity Failures | Permite que um usuário mal-intencionado intercepte a requisição de checkout e reduza o valor final a ser pago, explorando a falha do backend em confiar no total calculado pelo frontend. |
| **R11 — Acesso a informações da conta e pedidos de outro usuário** | Quebra de controle de acesso a nível de objeto (BOLA/IDOR) | CWE-639 (Authorization Bypass Through User-Controlled Key) / OWASP Top 10 A01:2021 – Broken Access Control / OWASP API Security Top 10 (API1:2023) | Permite que um usuário legítimo altere o ID do pedido ou da conta na URL/API e consiga visualizar dados pessoais e histórico de compras de outros usuários da plataforma. |
| **R23 — Acesso não autorizado às funções administrativas** | Quebra de controle de acesso a nível de função (Missing Authorization) | CWE-862 (Missing Authorization) / OWASP Top 10 A01:2021 – Broken Access Control / OWASP API Security Top 10 (API5:2023) | Permite que um usuário comum descubra e acesse as rotas administrativas da API para executar ações privilegiadas, pois o sistema oculta os botões no frontend, mas não bloqueia a requisição no backend. |

---