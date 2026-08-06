## 9. Tratamento dos riscos com NIST CSF

Após a identificação e a avaliação dos riscos, foram estabelecidas estratégias e medidas de segurança visando reduzir a probabilidade de ocorrência dos eventos e, caso aconteçam, minimizar seus impactos.

O **NIST Cybersecurity Framework 2.0** foi adotado como base para estruturar os resultados obtidos e as medidas de segurança previstas. O framework é dividido em seis funções principais:

| Função   | Finalidade no projeto                                                                                                |
| -------- | -------------------------------------------------------------------------------------------------------------------- |
| Govern   | Definir políticas, responsabilidades, prioridades e critérios para a gestão dos riscos                               |
| Identify | Identificar os ativos, dependências, vulnerabilidades e riscos associados ao sistema                                 |
| Protect  | Implementar medidas de proteção com o intuito de diminuir a probabilidade de ocorrência e os impactos dos incidentes |
| Detect   | Reconhecer atividades suspeitas, falhas e possíveis ocorrências relacionadas à segurança                             |
| Respond  | Realizar ações diante dos incidentes identificados, incluindo contenção, análise, comunicação e tratamento           |
| Recover  | Recuperar os serviços e dados afetados, buscando reduzir os impactos causados pelos incidentes                       |

As funções definidas pelo NIST CSF têm como objetivo auxiliar na organização das metas e dos resultados esperados relacionados à segurança, sem determinar a utilização de uma tecnologia ou solução específica. Assim, os controles descritos nas seções posteriores correspondem a propostas desenvolvidas pelo grupo, levando em consideração as características do sistema e os riscos identificados ao longo da análise.

### 9.1 Estratégias de tratamento

Para o gerenciamento dos riscos identificados, foram adotadas quatro abordagens principais:

| Estratégia   | Descrição                                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| Evitar       | Eliminar a atividade, funcionalidade ou condição que esteja relacionada à origem do risco                        |
| Reduzir      | Implementar controles e medidas de segurança que contribuam para reduzir a probabilidade ou os impactos do risco |
| Compartilhar | Repassar parte das responsabilidades, operações ou possíveis impactos para outra organização ou terceiro         |
| Aceitar      | Manter o risco de maneira consciente, desde que sua aceitação seja devidamente justificada e monitorada          |

A aceitação de um risco não implica que ele será simplesmente ignorado. É necessário que essa decisão seja devidamente registrada e justificada, aprovada pelo responsável competente e revisada sempre que houver alterações no sistema, no ambiente ou no nível de exposição ao risco.



### 9.2 Estratégia escolhida para cada risco

| Risco                                                              | Nível inicial | Estratégia principal       | Justificativa                                                                                                                                                                                                                |
| ------------------------------------------------------------------ | ------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R01 — Uso indevido da conta de um cliente**                      | Crítico       | **Reduzir**                | O acesso às contas é essencial para o funcionamento da plataforma, mas pode receber autenticação mais forte, proteção de sessão e monitoramento de acessos suspeitos.                                                        |
| **R02 — Alteração dos dados de recebimento**                       | Alto          | **Reduzir**                | A alteração dos dados financeiros pode ser necessária para manter os cadastros atualizados, mas operações desse tipo devem exigir autenticação e validação adicionais para impedir redirecionamentos fraudulentos.           |
| **R03 — Cadastro fraudulento de estabelecimento ou entregador**    | Médio         | **Reduzir**                | O cadastro de novos parceiros é necessário para ampliar a operação da plataforma, mas a identidade e as informações apresentadas devem passar por validação antes da concessão de acesso às funcionalidades correspondentes. |
| **R04 — Manipulação do valor do pedido**                           | Alto          | **Reduzir**                | A finalização de pedidos precisa permanecer disponível, mas os valores devem ser validados no servidor e calculados a partir de dados confiáveis para reduzir alterações indevidas.                                          |
| **R05 — Liberação indevida de repasse**                            | Alto          | **Reduzir**                | O fluxo de repasse é necessário para o funcionamento financeiro da plataforma, mas suas etapas críticas devem exigir confirmações confiáveis e validações adicionais antes da liberação dos valores.                         |
| **R06 — Uso indevido de cupons**                                   | Alto          | **Reduzir**                | Os cupons fazem parte das funcionalidades comerciais da plataforma, mas suas regras devem ser validadas no servidor e seu uso deve ser monitorado para reduzir fraudes e abusos.                                             |
| **R07 — Manipulação da localização do entregador**                 | Baixo         | **Reduzir**                | O acompanhamento da entrega é necessário, mas a plataforma pode utilizar mecanismos de validação e detecção de inconsistências para reduzir a possibilidade de localização falsificada.                                      |
| **R08 — Falsificação de notificações de pedido**                   | Baixo         | **Reduzir**                | As notificações são necessárias para informar os participantes sobre o andamento dos pedidos, mas sua autenticidade e integridade devem ser protegidas para evitar alterações ou mensagens falsas.                           |
| **R09 — Manipulação das avaliações**                               | Médio         | **Reduzir**                | As avaliações são necessárias para fornecer informações aos usuários, mas somente participantes autorizados e relacionados ao pedido devem poder criar ou alterar avaliações.                                                |
| **R10 — Manipulação de registros de auditoria**                    | Alto          | **Reduzir**                | Os registros são necessários para investigação e responsabilização, portanto devem possuir proteção de integridade, controle de acesso e mecanismos que dificultem sua alteração ou remoção indevida.                        |
| **R11 — Acesso a informações da conta e pedidos de outro usuário** | Crítico       | **Reduzir**                | O acesso aos pedidos é necessário para o funcionamento do sistema, porém cada operação deve verificar rigorosamente se o usuário possui autorização sobre o recurso solicitado.                                              |
| **R12 — Exposição de endereços e informações de localização**      | Crítico       | **Reduzir**                | O compartilhamento de localização e endereço é necessário para realizar as entregas, mas os dados devem ser disponibilizados somente enquanto houver necessidade e para usuários devidamente autorizados.                    |
| **R13 — Vazamento de dados pessoais pela API**                     | Crítico       | **Reduzir**                | O sistema precisa processar dados pessoais para funcionar, porém seu acesso deve ser limitado ao mínimo necessário, com validação de autorização e monitoramento das consultas.                                              |
| **R14 — Vazamento de informações financeiras**                     | Alto          | **Reduzir**                | O processamento e armazenamento de informações financeiras são necessários para os pagamentos e repasses, mas o acesso deve ser restrito e as operações sensíveis devem receber proteção adicional.                          |
| **R15 — Rastreamento indevido de entregadores**                    | Médio         | **Reduzir**                | O acesso à localização é necessário durante a entrega, mas deve ser limitado temporalmente e encerrado quando a finalidade que justificou o acesso deixar de existir.                                                        |
| **R16 — Descoberta automatizada de cupons**                        | Médio         | **Reduzir**                | A consulta e aplicação de cupons precisam permanecer disponíveis aos clientes, mas a quantidade de tentativas deve ser controlada e comportamentos automatizados suspeitos devem ser identificados.                          |
| **R17 — Enumeração de usuários**                                   | Médio         | **Reduzir**                | A existência de contas deve permanecer protegida, evitando respostas que permitam distinguir usuários cadastrados de inexistentes e limitando consultas automatizadas.                                                       |
| **R18 — Bloqueio de contas legítimas**                             | Médio         | **Reduzir**                | Os mecanismos de proteção contra tentativas de autenticação são necessários, mas devem limitar o impacto sobre usuários legítimos e identificar padrões de abuso antes de bloquear uma conta.                                |
| **R19 — Indisponibilidade da plataforma por sobrecarga**           | Crítico       | **Reduzir e compartilhar** | A disponibilidade da plataforma é essencial, podendo ser protegida por mecanismos próprios de limitação e monitoramento e, quando necessário, por serviços especializados de proteção contra tráfego malicioso.              |
| **R20 — Saturação do fluxo de pagamentos**                         | Alto          | **Reduzir e compartilhar** | O processamento de pagamentos é indispensável, mas pode receber mecanismos de limitação e detecção de abuso próprios e proteções oferecidas pelo Gateway de Pagamento utilizado.                                             |
| **R21 — Criação automatizada de pedidos**                          | Alto          | **Reduzir**                | A criação de pedidos é uma função essencial da plataforma, mas sua utilização deve possuir limites e mecanismos de detecção capazes de diferenciar o comportamento legítimo de automações abusivas.                          |
| **R22 — Abuso de conta administrativa comprometida**               | Alto          | **Reduzir**                | Contas administrativas são necessárias para a operação do sistema, mas seu uso deve ser protegido por autenticação reforçada, menor privilégio possível e monitoramento das operações sensíveis.                             |
| **R23 — Acesso não autorizado às funções administrativas**         | Alto          | **Reduzir**                | As funções administrativas são necessárias para operar a plataforma, mas devem possuir controle rigoroso de privilégios, autenticação reforçada e monitoramento das operações realizadas.                                    |


### 9.3 Mapeamento dos riscos para as funções do NIST CSF

| Risco                                                          | Govern | Identify | Protect | Detect | Respond | Recover |
| -------------------------------------------------------------- | ------ | -------- | ------- | ------ | ------- | ------- |
| R01 — Uso indevido da conta de um cliente                      | X      | X        | X       | X      | X       | X       |
| R02 — Alteração dos dados de recebimento                       | X      | X        | X       | X      | X       | X       |
| R03 — Cadastro fraudulento de estabelecimento ou entregador    | X      | X        | X       | X      | X       |         |
| R04 — Manipulação do valor do pedido                           | X      | X        | X       | X      | X       | X       |
| R05 — Liberação indevida de repasse                            | X      | X        | X       | X      | X       |         |
| R06 — Uso indevido de cupons                                   | X      | X        | X       | X      | X       | X       |
| R07 — Manipulação da localização do entregador                 | X      | X        | X       | X      | X       |         |
| R08 — Falsificação de notificações de pedido                   | X      | X        | X       | X      | X       | X       |
| R09 — Manipulação das avaliações                               | X      | X        | X       | X      | X       | X       |
| R10 — Manipulação de registros de auditoria                    | X      | X        | X       | X      | X       | X       |
| R11 — Acesso a informações da conta e pedidos de outro usuário | X      | X        | X       | X      | X       | X       |
| R12 — Exposição de endereços e informações de localização      | X      | X        | X       | X      | X       | X       |
| R13 — Vazamento de dados pessoais pela API                     | X      | X        | X       | X      | X       | X       |
| R14 — Vazamento de informações financeiras                     | X      | X        | X       | X      | X       | X       |
| R15 — Rastreamento indevido de entregadores                    | X      | X        | X       | X      | X       |         |
| R16 — Descoberta automatizada de cupons                        | X      | X        | X       | X      | X       |         |
| R17 — Enumeração de usuários                                   | X      | X        | X       | X      | X       |         |
| R18 — Bloqueio de contas legítimas                             | X      | X        | X       | X      | X       | X       |
| R19 — Indisponibilidade da plataforma por sobrecarga           | X      | X        | X       | X      | X       | X       |
| R20 — Saturação do fluxo de pagamentos                         | X      | X        | X       | X      | X       | X       |
| R21 — Criação automatizada de pedidos                          | X      | X        | X       | X      | X       | X       |
| R22 — Abuso de conta administrativa comprometida               | X      | X        | X       | X      | X       |         |
| R23 — Acesso não autorizado às funções administrativas         | X      | X        | X       | X      | X       |         |
