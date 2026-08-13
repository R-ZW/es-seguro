## 30. Objetivo

O objetivo desta etapa é integrar o que foi produzido ao longo da disciplina e demonstrar como a segurança pode acompanhar continuamente o ciclo de desenvolvimento do `Yummers`, desde a análise de ameaças até a operação.

Não foi implementado um pipeline real. A proposta abaixo descreve uma esteira DevSecOps textual, com evidências esperadas e condições de segurança que impediriam a continuidade do fluxo.

## 31. Pipeline DevSecOps Proposto

| Momento | Atividade de segurança | Evidência produzida | Condição para continuar |
| :--- | :--- | :--- | :--- |
| **Planejamento** | Modelagem de ameaças com STRIDE, identificação de casos de abuso e análise de riscos | Tabelas de ameaças, casos de abuso e registro de riscos priorizados | Riscos prioritários identificados e aceitos para tratamento |
| **Arquitetura** | Definição de requisitos e decisões de arquitetura para mitigar os riscos | Decisões arquiteturais relacionadas a autenticação, autorização, cálculo de valores e proteção de dados | Decisões revisadas e coerentes com os riscos `R01`, `R02`, `R03`, `R05`, `R09`, `R10` e `R12` |
| **Implementação segura** | Aplicação das práticas de código seguro selecionadas na Etapa 4 | Código ou pseudocódigo com versão insegura e versão segura | Regras de validação de entrada e autorização implementadas ou descritas |
| **Testes automatizados** | Execução dos testes de segurança definidos antes da implementação | Saída dos testes automatizados da Etapa 4 | Todos os testes de segurança aprovados |
| **Análise de código e dependências** | Execução de SAST, revisão de código, SCA e busca de segredos | Relatórios de SAST/SCA, revisão por pares e verificação de segredos | Sem segredo exposto, sem dependência crítica não tratada e sem achado crítico ignorado |
| **Teste dinâmico ou pentest** | Execução de DAST ou verificação equivalente em ambiente de teste/staging | Relatório do OWASP ZAP ou ferramenta equivalente | Achados críticos e altos analisados, corrigidos ou formalmente justificados |
| **Implantação** | Publicação controlada após aprovação das verificações de segurança | Registro do deploy e evidências dos quality gates | Deploy autorizado apenas se os gates anteriores forem aprovados |
| **Monitoramento e resposta** | Coleta de logs, regras de detecção, alertas e plano de resposta | Alertas, registros de eventos, painéis e ações de resposta | Incidentes investigados, tratados e usados para retroalimentar o backlog |

### 31.1 Condições de bloqueio do pipeline

O pipeline deve ser interrompido quando uma condição de segurança impedir a continuidade segura do projeto. Para o `Yummers`, as principais condições impeditivas seriam:

1. **Teste de segurança reprovado:** qualquer teste automatizado da Etapa 4 falha, especialmente testes de manipulação de valor do pedido ou de autorização.
2. **Falha no controle de acesso:** um cliente consegue acessar pedido de outro cliente, executar ação administrativa ou contornar regras de papel/perfil.
3. **Segredo encontrado no repositório:** tokens, senhas, chaves de API ou credenciais aparecem no código, em arquivos de configuração ou no histórico versionado.
4. **Dependência conhecida como vulnerável:** uma biblioteca, imagem ou componente usado pelo sistema possui vulnerabilidade crítica ou alta sem tratamento.
5. **Vulnerabilidade crítica não analisada:** achado crítico de SAST, SCA, DAST ou pentest permanece sem correção, justificativa ou aceite formal.

### 31.2 Integração com as etapas anteriores

| Etapa anterior | Como entra no pipeline |
| :--- | :--- |
| **Etapa 1 — Usuários, arquitetura, STRIDE e casos de abuso** | Alimenta o planejamento e a identificação de ameaças. |
| **Etapa 2 — Análise, priorização e tratamento de riscos** | Define quais riscos precisam de controles e quais são mais prioritários. |
| **Etapa 3 — Decisões de arquitetura** | Transforma riscos em decisões como recálculo de valores no servidor e autorização centralizada. |
| **Etapa 4 — Código seguro e testes** | Demonstra duas práticas implementáveis: validação de entrada/valor do pedido e controle de autorização. |
| **Etapas de verificação e detecção** | Produzem evidências de testes dinâmicos, alertas, logs e regras de resposta. |
| **Etapa 7 — DevSecOps e vídeo final** | Integra as evidências e mostra a evolução do projeto. |