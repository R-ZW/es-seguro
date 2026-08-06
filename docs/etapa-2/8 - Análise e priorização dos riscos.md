## 8. Análise e priorização de riscos

A análise de riscos foi elaborada com base nas ameaças identificadas por meio do STRIDE e nos casos de abuso apresentados anteriormente.

Para cada risco analisado, foram considerados:

- o evento que pode resultar em danos;
- a ameaça associada ao cenário;
- a vulnerabilidade ou condição necessária para que o abuso ocorra;
- a probabilidade de exploração ou ocorrência;
- os possíveis impactos para a plataforma e seus usuários;
- a pontuação atribuída ao risco e sua respectiva prioridade.


### 8.1 Critérios de probabilidade

| Valor | Classificação | Critério utilizado                                                                                                          |
| ----- | ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1     | Baixa         | A ocorrência exige circunstâncias pouco comuns, privilégios muito específicos ou um nível elevado de conhecimento técnico   |
| 2     | Média-baixa   | A ocorrência é viável, porém depende da existência de uma falha ou de condições específicas para ser explorada              |
| 3     | Média-alta    | A ocorrência é considerada provável e pode acontecer em cenários relativamente comuns de utilização ou exploração           |
| 4     | Alta          | A ocorrência pode ser realizada com pouca dificuldade, de forma recorrente ou diante de condições previsíveis da plataforma |


### 8.2 Critérios de impacto

| Valor | Classificação | Critério utilizado                                                                                                                     |
| ----- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Baixo         | Gera efeitos pouco significativos e pode ser solucionado sem grandes esforços ou consequências                                         |
| 2     | Moderado      | Provoca uma interrupção ou inconsistência de alcance limitado, sendo possível recuperar o funcionamento ou os dados afetados           |
| 3     | Alto          | Pode resultar em prejuízos relevantes, afetar processos importantes ou expor informações sensíveis                                     |
| 4     | Muito alto    | Pode atingir um grande número de usuários, comprometer funções essenciais ou provocar perdas financeiras e operacionais significativas |

### 8.3 Cálculo e classificação

A classificação de cada risco é obtida pela combinação entre sua probabilidade de ocorrência e o impacto esperado:

`Pontuação = Probabilidade × Impacto`

| Pontuação | Nível do risco |
| --------- | -------------- |
| 1 a 3     | Baixo          |
| 4 a 7     | Médio          |
| 8 a 11    | Alto           |
| 12 a 16   | Crítico        |

A pontuação permite estabelecer uma comparação e uma ordem de prioridade entre os riscos identificados. Entretanto, ela deve ser interpretada em conjunto com as características de cada cenário e com a justificativa utilizada para determinar a probabilidade e o impacto.


### 8.4 Registro de riscos

| ID | Origem STRIDE | Evento de risco | Vulnerabilidade ou condição | Probabilidade | Impacto | Pontuação | Nível |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Spoofing | Um atacante acessa a conta de um cliente e realiza pedidos utilizando seus meios de pagamento | Credenciais comprometidas, ausência de autenticação adicional e proteção insuficiente da sessão | 3 | 4 | 12 | Crítico |
| R02 | Tampering / Elevation of Privilege | Valores repassados a um estabelecimento são direcionados para uma conta ou chave de pagamento controlada pelo atacante | Alteração de dados de recebimento sem autenticação adicional e controle de autorização insuficiente | 2 | 4 | 8 | Alto |
| R03 | Spoofing | Um atacante atua como estabelecimento ou entregador utilizando identidade ou documentação fraudulenta | Processo de cadastro e aprovação não valida adequadamente a autenticidade dos dados e documentos apresentados | 2 | 3 | 6 | Médio |
| R04 | Tampering | O valor final de um pedido é reduzido ou alterado indevidamente durante a finalização da compra | Backend confia em valores enviados pelo cliente e não recalcula ou valida adequadamente os valores do pedido | 2 | 4 | 8 | Alto |
| R05 | Tampering / Elevation of Privilege | Uma coleta ou entrega é falsamente confirmada e um repasse é liberado indevidamente | Validação insuficiente da Chave de Coleta/Entrega e possibilidade de acionar etapas do fluxo sem comprovação adequada | 2 | 4 | 8 | Alto |
| R06 | Tampering | Um atacante manipula regras de aplicação de cupons para obter descontos superiores aos permitidos | Validação insuficiente das regras de cupom no backend e confiança em parâmetros enviados pelo cliente | 4 | 2 | 8 | Alto |
| R07 | Tampering | A localização transmitida pelo entregador é adulterada para apresentar uma posição diferente da real | O sistema confia nas coordenadas fornecidas pelo dispositivo sem mecanismos suficientes para detectar localização falsificada | 2 | 1 | 2 | Baixo |
| R08 | Tampering / Spoofing | Usuários ou componentes recebem notificações falsas sobre o estado de um pedido | Notificações não possuem mecanismos suficientes de autenticação e integridade | 2 | 1 | 2 | Baixo |
| R09 | Tampering | Avaliações de estabelecimentos ou entregadores são alteradas ou inseridas indevidamente para prejudicar sua reputação | API não verifica adequadamente a identidade do autor, sua relação com o pedido ou a integridade dos registros | 3 | 2 | 6 | Médio |
| R10 | Repudiation / Tampering | Registros de auditoria são alterados ou removidos para ocultar uma operação fraudulenta | Logs podem ser modificados ou excluídos por usuários ou componentes envolvidos na própria operação | 2 | 4 | 8 | Alto |
| R11 | Information Disclosure | Um usuário tem acesso a informação da conta e pedidos pertencentes a outro usuário | Falha de autorização na API e ausência de validação da propriedade do recurso solicitado | 3 | 4 | 12 | Crítico |
| R12 | Information Disclosure | Endereços ou informações de localização de clientes e entregadores são acessados por usuários não autorizados | Falha de autorização nos dados de entrega e localização disponibilizados pela API | 3 | 4 | 12 | Crítico |
| R13 | Information Disclosure | Dados pessoais de clientes, entregadores ou estabelecimentos são obtidos indevidamente por meio da API | Falhas de autorização, configuração ou proteção dos endpoints que disponibilizam dados pessoais | 3 | 4 | 12 | Crítico |
| R14 | Information Disclosure | Informações financeiras e transacionais de outros usuários ou estabelecimentos são acessadas indevidamente | Falha de autorização no acesso ao histórico de transações ou proteção insuficiente dos dados financeiros | 2 | 4 | 8 | Alto |
| R15 | Information Disclosure | Dados de localização de entregadores continuam acessíveis após o encerramento da relação autorizada com uma entrega | Falha no controle de acesso e no ciclo de vida das permissões de consulta à localização | 2 | 3 | 6 | Médio |
| R16 | Information Disclosure / Denial of Service | Um atacante descobre cupons válidos por meio de tentativas automatizadas de validação | Respostas diferenciadas da API e ausência de limitação adequada para tentativas de consulta de cupons | 4 | 1 | 4 | Médio |
| R17 | Information Disclosure | Um atacante identifica quais usuários possuem contas cadastradas na plataforma | Respostas diferentes da API para usuários existentes e inexistentes permitem a enumeração de contas | 4 | 1 | 4 | Médio |
| R18 | Denial of Service | Contas de usuários legítimos são bloqueadas por tentativas deliberadas de autenticação malsucedida | Mecanismo de bloqueio acionável por terceiros e ausência de proteção adequada contra tentativas automatizadas | 2 | 2 | 4 | Médio |
| R19 | Denial of Service | A plataforma sofre degradação ou indisponibilidade devido a um volume deliberado de requisições | Ausência de rate limiting eficaz, detecção insuficiente de tráfego anômalo e capacidade limitada de absorção de picos | 4 | 4 | 16 | Crítico |
| R20 | Denial of Service | O fluxo de pagamentos fica indisponível devido a um grande volume de transações inválidas automatizadas | Ausência de limitação de tentativas e mecanismos de detecção de comportamento anômalo na integração com o Gateway | 2 | 4 | 8 | Alto |


### 8.5 Justificativas

#### R01 — Uso indevido da conta de um cliente

**Probabilidade:** Média-alta. O comprometimento de credenciais é uma situação plausível, especialmente por phishing, reutilização de senhas ou vazamentos ocorridos em outros serviços. A ausência de uma segunda etapa de autenticação aumenta a possibilidade de utilização indevida da conta.

**Impacto:** Muito alto. O atacante pode realizar pedidos utilizando meios de pagamento ou saldo associados à vítima, causando prejuízo financeiro direto e disputas posteriores sobre as transações.

#### R02 — Alteração dos dados de recebimento

**Probabilidade:** Média-baixa. A exploração depende de acesso à conta do estabelecimento ou de uma falha específica de autorização na funcionalidade responsável pelos dados financeiros.

**Impacto:** Muito alto. O atacante pode redirecionar valores destinados ao estabelecimento, causando prejuízo financeiro direto e afetando o fluxo de repasses da plataforma.

#### R03 — Cadastro fraudulento de estabelecimento ou entregador

**Probabilidade:** Média-baixa. O atacante precisa contornar o processo de cadastro e aprovação, normalmente utilizando documentos falsificados, roubados ou adulterados. O sistema possui uma etapa administrativa específica para aprovação de novos parceiros.

**Impacto:** Alto. Uma conta fraudulenta aprovada recebe legitimidade dentro da plataforma e pode interagir diretamente com clientes e pedidos, possibilitando fraudes posteriores e comprometendo a confiança no processo de aprovação.

#### R04 — Manipulação do valor do pedido

**Probabilidade:** Média-baixa. A exploração depende de uma falha específica na validação do valor do pedido, especialmente caso o backend confie em informações enviadas pelo cliente.

**Impacto:** Muito alto. A exploração pode permitir que pedidos sejam processados por valores inferiores aos corretos, causando prejuízo financeiro direto ao estabelecimento e à plataforma.

#### R05 — Liberação indevida de repasse

**Probabilidade:** Média-baixa. A exploração depende de uma falha específica na validação das etapas de coleta e entrega ou da possibilidade de manipular as confirmações utilizadas pelo fluxo de custódia.

**Impacto:** Muito alto. Uma exploração bem-sucedida pode liberar valores retidos em custódia sem que a entrega tenha sido efetivamente confirmada, gerando prejuízo financeiro direto.

#### R06 — Uso indevido de cupons

**Probabilidade:** Alta. A aplicação de cupons é uma funcionalidade acessível aos clientes e pode ser explorada caso a API não valide corretamente as regras de utilização.

**Impacto:** Moderado. O prejuízo tende a ficar limitado aos descontos concedidos indevidamente, embora a exploração repetida possa aumentar as perdas financeiras.

#### R07 — Manipulação da localização do entregador

**Probabilidade:** Média-baixa. Ferramentas de falsificação de localização podem ser utilizadas por um entregador com acesso ao próprio dispositivo, não exigindo necessariamente o comprometimento da infraestrutura da plataforma.

**Impacto:** Baixo. A manipulação prejudica a confiabilidade do acompanhamento e pode ocultar atrasos ou desvios, mas normalmente não compromete diretamente informações críticas ou valores financeiros.

#### R08 — Falsificação de notificações de pedido

**Probabilidade:** Média-baixa. A exploração depende da possibilidade de interceptar ou reproduzir mensagens aceitas como notificações legítimas, além de uma proteção insuficiente de sua autenticidade ou integridade.

**Impacto:** Baixo. A falsificação pode induzir usuários ou componentes a tomar decisões incorretas sobre pedidos, mas normalmente depende de outras condições para produzir um prejuízo mais grave.

#### R09 — Manipulação das avaliações

**Probabilidade:** Média-alta. A exploração pode ocorrer caso a API não valide corretamente a relação entre usuário, pedido e avaliação, permitindo que requisições sejam manipuladas.

**Impacto:** Moderado. O principal efeito é a distorção da reputação de estabelecimentos ou entregadores e a apresentação de informações falsas aos demais clientes, sem necessariamente comprometer diretamente operações críticas.

#### R10 — Manipulação dos registros de auditoria

**Probabilidade:** Média-baixa. O abuso depende de o atacante obter acesso suficiente para modificar ou remover registros de auditoria, o que normalmente exige comprometimento prévio de uma conta ou componente privilegiado.

**Impacto:** Muito alto. A alteração das evidências pode dificultar a investigação de fraudes, impedir a responsabilização dos envolvidos e comprometer a confiabilidade dos mecanismos de auditoria.

#### R11 — Acesso a informações da conta e pedidos de outro usuário

**Probabilidade:** Média-alta. Falhas de autorização em APIs são plausíveis quando o servidor autentica o usuário, mas não verifica corretamente se ele possui acesso ao recurso solicitado.

**Impacto:** Muito alto. O atacante pode obter dados pessoais, informações de pedidos e potencialmente executar operações em recursos pertencentes a terceiros.

#### R12 — Exposição de endereços e informações de localização

**Probabilidade:** Média-alta. Os dados de localização e entrega são utilizados por funcionalidades normais do sistema, e uma falha de autorização pode permitir que usuários consultem recursos pertencentes a terceiros. A localização e os endereços são ativos explicitamente relevantes no sistema.

**Impacto:** Muito alto. A exposição pode revelar endereços residenciais e trajetos em tempo real, afetando a privacidade e podendo representar risco à segurança física de clientes e entregadores.

#### R13 — Vazamento de dados pessoais

**Probabilidade:** Média-alta. APIs que disponibilizam dados cadastrais podem apresentar falhas de autorização ou configuração capazes de permitir consultas indevidas.

**Impacto:** Muito alto. A exposição pode atingir dados pessoais de clientes, entregadores e estabelecimentos em quantidade significativa, além de gerar consequências legais e reputacionais.

#### R14 — Vazamento de informações financeiras

**Probabilidade:** Média-baixa. O acesso depende de uma falha específica na autorização, proteção dos históricos de transações ou configuração do gateway de pagamento.

**Impacto:** Muito alto. Informações financeiras podem ser utilizadas para fraudes e ataques direcionados, além de representarem dados sensíveis cuja exposição pode gerar prejuízos relevantes à plataforma e aos usuários.


#### R15 — Rastreamento indevido de entregadores

**Probabilidade:** Média-baixa. A exploração depende da permanência indevida das permissões de acesso à localização após o encerramento ou alteração da relação com a entrega.

**Impacto:** Alto. O acesso prolongado pode expor os deslocamentos e padrões de rotina do entregador, representando uma violação relevante de privacidade e potencial risco à sua segurança.

#### R16 — Descoberta automatizada de cupons

**Probabilidade:** Alta. A exploração pode ser automatizada e exige apenas que a API forneça respostas distinguíveis para códigos válidos e inválidos e não limite adequadamente as tentativas.

**Impacto:** Baixo. O principal prejuízo é a descoberta e utilização indevida de códigos promocionais, normalmente resultando em descontos não planejados de valor limitado.

#### R17 — Enumeração de usuários

**Probabilidade:** Alta. Caso a API retorne respostas diferentes para usuários existentes e inexistentes, a enumeração pode ser realizada automaticamente com baixo esforço técnico.

**Impacto:** Baixo. A informação obtida isoladamente possui valor limitado, pois revela principalmente a existência de uma conta. Entretanto, ela pode facilitar ataques posteriores, como phishing e tentativas direcionadas de comprometimento.

#### R18 — Bloqueio de contas legítimas

**Probabilidade:** Média-baixa. O ataque pode ser realizado por meio de repetidas tentativas de autenticação e depende de um comportamento previsível do mecanismo de bloqueio automático.

**Impacto:** Moderado. O usuário legítimo pode ficar temporariamente impedido de acessar sua conta e acompanhar ou realizar pedidos, mas o bloqueio pode ser revertido após o período de proteção.

#### R19 — Indisponibilidade da plataforma por sobrecarga

**Probabilidade:** Alta. Pois em determinados períodos (horário de almoço e jantar) o aumento de acessos é significativo e também pode ser alvo de atacantes com tráfego malicioso.

**Impacto:** Muito alto. A indisponibilidade durante horários de pico pode impedir pedidos e pagamentos, afetando simultaneamente clientes, estabelecimentos e a própria plataforma. A disponibilidade é considerada um ativo crítico justamente nesses períodos.

#### R20 — Saturação do fluxo de pagamentos

**Probabilidade:** Média-baixa. O ataque exige a geração automatizada de um volume suficiente de transações inválidas para provocar limitação ou bloqueio por parte do Gateway de Pagamento.

**Impacto:** Muito alto. Caso a integração seja limitada ou bloqueada, clientes legítimos podem ficar temporariamente impossibilitados de concluir pagamentos e, consequentemente, de realizar novos pedidos.