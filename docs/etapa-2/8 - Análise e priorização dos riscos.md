# `Yummers` - Aplicativo de delivery

### Conteúdo da página:

> [8.1 Critérios de probabilidade](#81-critérios-de-probabilidade)<br>
> [8.2 Critérios de impacto](#82-critérios-de-impacto)<br>
> [8.3 Cálculo e classificação](#83-cálculo-e-classificação)<br>
> [8.4 Registro de riscos](#84-registro-de-riscos)<br>
> [8.5 Justificativas](#85-justificativas)<br>
> [8.6 Priorização](#86-priorização)<br>
> [8.7 Conclusão da análise](#87-conclusão-da-análise)<br>

---

## 🛡️ 8. Análise e priorização de riscos

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
| R21 | Denial of Service | A criação automatizada de pedidos consome recursos da plataforma e pode degradar seu desempenho | Ausência de limitação de frequência e de mecanismos de detecção de automação na criação de pedidos | 3 | 3 | 9 | Alto |
| R22 | Elevation of Privilege / Spoofing | Um atacante utiliza uma conta administrativa comprometida para executar operações sensíveis | Credenciais ou sessão administrativa comprometida e ausência de controles adicionais para operações privilegiadas | 2 | 4 | 8 | Alto |
| R23 | Elevation of Privilege / Spoofing | Um usuário sem privilégios administrativos acessa funções destinadas exclusivamente a administradores | API não verifica adequadamente a role ou as permissões do usuário no backend | 2 | 4 | 8 | Alto |

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

#### R21 — Criação automatizada de pedidos

**Probabilidade:** Média-alta. A criação de pedidos é uma funcionalidade acessível a clientes e pode ser automatizada quando não existem mecanismos eficazes de limitação de frequência ou detecção de comportamento automatizado.

**Impacto:** Alta. O abuso pode consumir recursos do backend e do banco de dados e gerar notificações e operações desnecessárias, mas normalmente não provoca imediatamente a indisponibilidade completa da plataforma.

#### R22 — Abuso de conta administrativa comprometida

**Probabilidade:** Média-baixa. O cenário exige o comprometimento prévio das credenciais ou sessão de um administrador, o que reduz sua frequência em comparação com ataques contra usuários comuns.

**Impacto:** Muito alto. Uma conta administrativa possui capacidade de gerenciar usuários, aprovar parceiros, monitorar pedidos e atuar em chamados e operações sensíveis. O comprometimento pode, portanto, produzir efeitos em escala.

#### R23 — Acesso às funções administrativas

**Probabilidade:** Média-baixa. A exploração depende de uma falha específica no controle de autorização do backend, como a existência de endpoints administrativos que não validem adequadamente a role do usuário.

**Impacto:** Muito alto. O acesso indevido pode permitir operações administrativas sobre contas, pedidos, cadastros e outras funções críticas da plataforma.

Aqui está a seção 8.6 refatorada e devidamente ordenada de acordo com as pontuações (do maior para o menor) estabelecidas na tabela 8.4.

Foi corrigido o erro de ordenação do item **R18** (que possuía pontuação 4, mas estava listado acima de itens com pontuação 6) e removido o 24º item duplicado/inexistente ("R23 — Consulta automatizada..."), já que a tabela original conta com exatamente 23 riscos.

### 8.6 Priorização

A ordem inicial de prioridade foi definida considerando a pontuação obtida na análise de risco. Nos casos de mesma pontuação, foram considerados como critérios complementares a abrangência do impacto, a quantidade de usuários potencialmente afetados e a criticidade da operação comprometida.

1. **R19 — Indisponibilidade da plataforma por sobrecarga (16):** possui a maior pontuação da análise e pode comprometer simultaneamente o acesso de clientes, estabelecimentos e entregadores, afetando diretamente a disponibilidade da plataforma.
2. **R01 — Uso indevido da conta de um cliente (12):** possui pontuação crítica e pode resultar em prejuízo financeiro direto para os clientes, além de permitir que o atacante utilize funcionalidades legítimas da conta comprometida.
3. **R11 — Acesso a informações da conta e pedidos de outro usuário (12):** possui pontuação crítica e pode permitir acesso a recursos pertencentes a terceiros, comprometendo o isolamento entre as contas da plataforma.
4. **R12 — Exposição de endereços e informações de localização (12):** possui pontuação crítica e envolve informações cuja exposição pode comprometer significativamente a privacidade e a segurança de clientes e entregadores.
5. **R13 — Vazamento de dados pessoais (12):** possui pontuação crítica e pode resultar na exposição de dados pessoais de clientes, entregadores e estabelecimentos, potencialmente em grande escala.
6. **R21 — Criação automatizada de pedidos (9):** possui pontuação alta e pode gerar grande quantidade de operações desnecessárias, consumindo recursos da plataforma e degradando o desempenho para usuários legítimos.
7. **R04 — Manipulação do valor do pedido (8):** possui pontuação alta e pode causar prejuízo financeiro direto ao alterar indevidamente o valor dos pedidos durante sua finalização.
8. **R05 — Liberação indevida de repasse (8):** possui pontuação alta e pode resultar na liberação de valores mantidos em custódia sem que a coleta ou entrega tenha sido devidamente confirmada.
9. **R23 — Acesso não autorizado às funções administrativas (8):** possui pontuação alta e pode permitir que um usuário obtenha acesso a operações administrativas capazes de afetar diferentes recursos da plataforma.
10. **R02 — Alteração dos dados de recebimento (8):** possui pontuação alta e pode direcionar valores devidos a um estabelecimento para uma conta ou chave de pagamento controlada pelo atacante.
11. **R22 — Abuso de conta administrativa comprometida (8):** possui pontuação alta e pode permitir a execução de operações sensíveis utilizando os privilégios legítimos de uma conta administrativa comprometida.
12. **R06 — Uso indevido de cupons (8):** possui pontuação alta e pode permitir a obtenção de descontos superiores aos previstos, gerando prejuízo financeiro para a plataforma ou para os estabelecimentos.
13. **R14 — Vazamento de informações financeiras (8):** possui pontuação alta e pode revelar informações relacionadas a transações e dados financeiros de usuários ou estabelecimentos.
14. **R10 — Manipulação de registros de auditoria (8):** possui pontuação alta e pode dificultar a identificação e investigação de operações fraudulentas, comprometendo a confiabilidade dos mecanismos de auditoria.
15. **R20 — Saturação do fluxo de pagamentos (8):** possui pontuação alta e pode prejudicar a capacidade de clientes legítimos de concluir pagamentos, afetando diretamente a realização de novos pedidos.
16. **R03 — Cadastro fraudulento de estabelecimento ou entregador (6):** possui pontuação média e pode introduzir uma identidade fraudulenta na plataforma, possibilitando posteriormente outros tipos de fraude.
17. **R09 — Manipulação das avaliações (6):** possui pontuação média e pode distorcer a reputação de estabelecimentos ou entregadores, influenciando a percepção de outros usuários.
18. **R15 — Rastreamento indevido de entregadores (6):** possui pontuação média e pode expor os deslocamentos de entregadores mesmo após o encerramento da relação autorizada com uma entrega.
19. **R18 — Bloqueio de contas legítimas (4):** possui pontuação média e pode impedir temporariamente usuários legítimos de acessar suas contas e utilizar os serviços da plataforma.
20. **R16 — Descoberta automatizada de cupons (4):** possui pontuação média e pode permitir a identificação de códigos promocionais válidos, possibilitando sua utilização indevida.
21. **R17 — Enumeração de usuários (4):** possui pontuação média e pode revelar quais usuários possuem contas cadastradas na plataforma, fornecendo informações que podem facilitar ataques posteriores.
22. **R07 — Manipulação da localização do entregador (2):** possui pontuação baixa e tende a afetar principalmente a confiabilidade das informações de acompanhamento, com impacto limitado sobre outras operações da plataforma.
23. **R08 — Falsificação de notificações de pedido (2):** possui pontuação baixa e pode induzir usuários ou componentes a interpretar incorretamente o estado de um pedido, mas apresenta impacto limitado no contexto analisado.

## 8.7 Conclusão da análise

A aplicação do STRIDE permitiu identificar diferentes ameaças, mas a avaliação de probabilidade e impacto mostrou que elas não possuem a mesma prioridade de tratamento.

Os riscos críticos e altos deverão receber atenção inicial, especialmente aqueles relacionados à disponibilidade da plataforma, à segurança das transações financeiras e à proteção dos dados pessoais de clientes, entregadores e estabelecimentos.

A classificação atual representa uma avaliação preliminar baseada no contexto operacional conhecido. Ela poderá ser revisada à medida que a arquitetura evoluir ou quando surgirem novas informações sobre o sistema, o comportamento dos usuários ou incidentes observados.

---
<center>
<table width="100%">
<tr>
<td align="left">

[⬅️ Página anterior](../etapa-1/7%20-%20Considerações%20finais%20da%20Etapa%201.md)

</td>

<td align="center">

6️⃣

</td>

<td align="right">

[Próxima página ➡️](9%20-%20Tratamento%20dos%20riscos%20com%20NIST%20CSF.md)

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

8. [**🛡️ Análise e priorização dos riscos**](#8-análise-e-priorização-de-riscos) 👈
9. [**🧩 Tratamento dos riscos com NIST CSF**](9%20-%20Tratamento%20dos%20riscos%20com%20NIST%20CSF.md)


**Etapa 3**:

10. [**🏗️ Arquitetura segura**](../etapa-3/10%20-%20Arquitetura%20segura.md)


**Etapa 4**:

11. [**💻 Código seguro e testes de segurança**](../etapa-4/11%20-%20Código%20seguro%20e%20testes%20de%20segurança.md)


**Etapa 5**:

12. [**🔎 Verificação de vulnerabilidades**](../etapa-5/12%20-%20Verificação%20de%20vulnerabilidades.md)


**Etapa 6**:

13. [**📡 Monitoramento e detecção de intrusões**](../../roteiros/etapa-6-deteccao-de-intrusoes.md)


**Etapa 7**:

14. [**🎥 DevSecOps e vídeo final**](../../roteiros/etapa-7-devsecops-e-video-final.md)

---