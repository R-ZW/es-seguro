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
