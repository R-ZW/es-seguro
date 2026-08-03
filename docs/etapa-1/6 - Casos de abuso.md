## 6. Casos de abuso
### CA01 — Fraude de pedido por sequestro de conta de cliente

**Ator:** atacante externo.

**Objetivo:** realizar pedidos fraudulentos às custas de outro usuário, utilizando saldo ou meio de pagamento cadastrado na conta da vítima.

**Condições necessárias:**

- o atacante obtém as credenciais da vítima (phishing, reuso de senha ou vazamento de credenciais);
- o sistema não exige autenticação adicional para acesso à conta ou confirmação de operações sensíveis;
- a sessão autenticada pode permanecer válida por período excessivo ou não é invalidada adequadamente.

**Fluxo de abuso:**

1. O atacante obtém as credenciais de um cliente por meio de phishing, reutilização de senha ou vazamento ocorrido em outro serviço.
2. O atacante autentica-se na plataforma utilizando as credenciais da vítima.
3. O sistema aceita a autenticação sem exigir uma verificação adicional que permita confirmar a identidade do usuário.
4. O atacante acessa os meios de pagamento ou saldo disponíveis na conta da vítima e monta um novo pedido.
5. O atacante confirma o pagamento utilizando o método já cadastrado na conta.
6. O sistema processa o pedido normalmente, mantendo o valor em custódia e notificando o estabelecimento.
7. A vítima somente percebe o abuso posteriormente, ao consultar o histórico de pedidos ou o extrato do meio de pagamento.

**Impacto esperado:** prejuízo financeiro direto ao cliente, possível contestação da transação junto ao Gateway de Pagamento, necessidade de estorno e dano à confiança na plataforma.

**Categorias STRIDE relacionadas:** Spoofing, Repudiation.

---

### CA02 — Fraude por alteração não autorizada dos dados de recebimento de um estabelecimento

**Ator:** atacante externo ou usuário mal-intencionado com acesso à conta de um estabelecimento.

**Objetivo:** redirecionar os valores devidos a um estabelecimento para uma conta ou chave de pagamento controlada pelo atacante.

**Condições necessárias:**

- o estabelecimento pode cadastrar ou alterar seus dados de recebimento pela plataforma;
- a alteração dos dados financeiros não exige autenticação ou confirmação adicional adequada;
- o sistema não verifica suficientemente a identidade e a autorização do responsável pela alteração;
- o atacante consegue obter acesso à conta do estabelecimento ou explorar uma falha de autorização na API.

**Fluxo de abuso:**

1. O atacante obtém acesso à conta de um estabelecimento por meio de credenciais comprometidas ou explora uma falha de autorização na API.
2. O atacante acessa a funcionalidade de gerenciamento dos dados de recebimento.
3. O atacante substitui a conta bancária ou chave PIX cadastrada pelo estabelecimento por dados controlados por ele.
4. O sistema aceita a alteração sem exigir uma confirmação adicional ou verificar adequadamente a legitimidade da operação.
5. O estabelecimento continua recebendo e processando pedidos normalmente, sem perceber imediatamente a alteração.
6. Quando ocorre o repasse de valores, a plataforma utiliza os dados de recebimento adulterados.
7. Os valores destinados ao estabelecimento são transferidos para a conta ou chave controlada pelo atacante.

**Impacto esperado:** perda financeira direta para o estabelecimento, possível perda de valores em custódia, necessidade de investigação e recuperação das transações e comprometimento da confiança no mecanismo de repasse da plataforma.

**Categorias STRIDE relacionadas:** Spoofing, Tampering, Elevation of Privilege.

---

### CA03 — Exploração de cadastro fraudulento de estabelecimento ou entregador

**Ator:** atacante externo.

**Objetivo:** obter acesso legítimo à plataforma utilizando uma identidade ou documentação fraudulenta para atuar como estabelecimento ou entregador.

**Condições necessárias:**

- o sistema permite o cadastro de estabelecimentos ou entregadores mediante envio de dados e documentos;
- o processo de validação e aprovação não verifica adequadamente a autenticidade das informações apresentadas;
- o atacante consegue obter ou produzir documentos e informações suficientes para concluir o cadastro;
- a conta criada recebe permissões para realizar operações próprias do perfil após a aprovação.

**Fluxo de abuso:**

1. O atacante reúne dados pessoais ou documentos falsificados, adulterados ou pertencentes a outra pessoa.
2. O atacante realiza o cadastro na plataforma apresentando os dados e documentos obtidos.
3. O processo de validação da plataforma não identifica a inconsistência ou falsificação das informações apresentadas.
4. A conta é aprovada e recebe as permissões correspondentes ao perfil de estabelecimento ou entregador.
5. O atacante passa a utilizar a conta normalmente para interagir com clientes, pedidos ou outros componentes da plataforma.
6. O atacante utiliza a confiança concedida pela aprovação da plataforma para realizar atividades indevidas ou obter benefícios antes que a fraude seja identificada.

**Impacto esperado:** criação de uma identidade fraudulenta com acesso legítimo à plataforma, possibilidade de realização de fraudes contra clientes ou outros participantes e comprometimento da confiança no processo de cadastro e aprovação de parceiros.

**Categorias STRIDE relacionadas:** Spoofing.

---

### CA04 — Manipulação do valor do pedido durante a finalização da compra

**Ator:** cliente mal-intencionado ou atacante externo.

**Objetivo:** reduzir ou modificar o valor de um pedido antes de sua confirmação, obtendo produtos ou serviços por um preço inferior ao estabelecido pelo sistema.

**Condições necessárias:**

- o cliente consegue manipular os dados enviados pelo aplicativo durante a finalização do pedido;
- a API aceita valores de produtos, quantidades, descontos ou valor total fornecidos pelo cliente sem recalculá-los no servidor;
- não existe validação de integridade entre os itens efetivamente selecionados e o valor utilizado no pagamento.

**Fluxo de abuso:**

1. O atacante monta normalmente um pedido utilizando produtos disponíveis na plataforma.
2. Durante a finalização, o atacante intercepta ou modifica a requisição enviada pelo aplicativo à API.
3. O atacante altera o preço de um ou mais itens, a quantidade ou o valor total do pedido.
4. A API recebe os dados manipulados e aceita o valor fornecido sem recalcular o preço com base nos dados armazenados no servidor.
5. O sistema registra e processa o pedido utilizando o valor adulterado.
6. O estabelecimento recebe a solicitação do pedido como se o valor fosse legítimo.
7. O atacante recebe os produtos ou serviços pagando um valor inferior ao originalmente estabelecido.

**Impacto esperado:** prejuízo financeiro para o estabelecimento e/ou para a plataforma, distorção dos registros financeiros e possibilidade de exploração repetida da vulnerabilidade em diversos pedidos.

**Categorias STRIDE relacionadas:** Tampering.

---

### CA05 — Liberação indevida de repasse por falsificação da confirmação de coleta ou entrega

**Ator:** atacante externo ou usuário legítimo mal-intencionado.

**Objetivo:** induzir a plataforma a considerar uma coleta ou entrega como concluída para obter indevidamente um repasse financeiro mantido em custódia.

**Condições necessárias:**

- a confirmação de coleta ou entrega é utilizada pelo sistema como condição para liberar valores em custódia;
- a API não valida adequadamente a autenticidade, validade ou associação da confirmação ao pedido;
- o atacante consegue obter, prever, reutilizar ou manipular os dados utilizados para confirmar a operação.

**Fluxo de abuso:**

1. O atacante identifica um pedido que possui valores mantidos em custódia.
2. O atacante obtém ou manipula os dados utilizados para confirmar a coleta ou entrega do pedido.
3. O atacante envia à API uma solicitação de confirmação utilizando os dados adulterados.
4. O servidor aceita a confirmação sem verificar adequadamente se a operação realmente ocorreu ou se a confirmação está associada ao pedido correto.
5. O sistema altera o estado do pedido para indicar que a etapa correspondente foi concluída.
6. A plataforma libera o repasse financeiro que estava condicionado à confirmação da etapa.
7. O atacante recebe ou direciona indevidamente o valor liberado sem que a coleta ou entrega tenha ocorrido conforme o fluxo legítimo.

**Impacto esperado:** liberação indevida de valores mantidos em custódia, prejuízo financeiro para a plataforma, estabelecimento ou entregador, além de disputas sobre a realização da coleta ou entrega.

**Categorias STRIDE relacionadas:** Tampering, Repudiation, Elevation of Privilege.

---

### CA06 — Uso indevido de cupons por manipulação das regras de desconto

**Ator:** cliente mal-intencionado ou atacante externo.

**Objetivo:** obter descontos superiores aos permitidos ou utilizar repetidamente cupons que deveriam possuir restrições de uso.

**Condições necessárias:**

- a aplicação permite que o cliente informe ou manipule os dados utilizados para aplicação de um cupom;
- a API não valida adequadamente as condições de uso do cupom no servidor;
- restrições como quantidade máxima de utilizações, validade, percentual de desconto ou associação à conta podem ser alteradas ou contornadas pelo atacante.

**Fluxo de abuso:**

1. O atacante identifica um cupom disponível na plataforma e analisa as informações utilizadas pelo aplicativo para solicitar sua aplicação.
2. O atacante intercepta a requisição enviada à API durante a aplicação do cupom.
3. O atacante modifica parâmetros da requisição, como o código do cupom, percentual de desconto ou informações utilizadas para verificar sua utilização.
4. A API recebe os dados manipulados e não realiza uma validação completa das regras do cupom no servidor.
5. O sistema aplica um desconto superior ao permitido ou aceita um cupom que já deveria estar expirado ou esgotado.
6. O atacante finaliza o pedido utilizando o valor indevidamente reduzido.
7. O procedimento pode ser repetido em novos pedidos caso a vulnerabilidade permita contornar as limitações de utilização.

**Impacto esperado:** prejuízo financeiro para a plataforma e para os estabelecimentos, utilização indevida de campanhas promocionais e aumento artificial dos descontos concedidos.

**Categorias STRIDE relacionadas:** Tampering.

---

### CA07 — Manipulação da localização do entregador para fraudar o acompanhamento da entrega

**Ator:** entregador mal-intencionado.

**Objetivo:** transmitir uma localização falsa para ocultar atrasos, desvios de rota ou outras irregularidades durante uma entrega.

**Condições necessárias:**

- o aplicativo utiliza a localização fornecida pelo dispositivo do entregador para atualizar sua posição na plataforma;
- o sistema não possui mecanismos suficientes para detectar ou validar coordenadas incompatíveis com o deslocamento esperado;
- o entregador consegue utilizar recursos de falsificação de localização disponíveis no dispositivo.

**Fluxo de abuso:**

1. O entregador aceita um pedido e inicia normalmente o processo de entrega.
2. O entregador utiliza um mecanismo de falsificação de localização no dispositivo para fornecer coordenadas diferentes de sua posição real.
3. O aplicativo transmite as coordenadas adulteradas para a plataforma.
4. O servidor registra a localização recebida sem identificar que os dados foram manipulados.
5. O cliente e a plataforma visualizam uma posição diferente da localização real do entregador.
6. O entregador utiliza a localização falsificada para ocultar atrasos, desvios ou permanência em outro local durante a entrega.
7. Caso necessário, o entregador retorna à rota real antes de concluir a entrega, reduzindo a possibilidade de o desvio ser percebido pelo acompanhamento convencional.

**Impacto esperado:** informações incorretas sobre o andamento das entregas, dificuldade de fiscalização do serviço, possibilidade de ocultação de atrasos ou desvios e redução da confiabilidade do mecanismo de rastreamento.

**Categorias STRIDE relacionadas:** Tampering, Repudiation.

---

### CA08 — Interceptação ou falsificação de notificações de alteração de status do pedido

**Ator:** atacante externo.

**Objetivo:** induzir usuários ou componentes da plataforma a acreditar que um pedido atingiu um estado diferente do seu estado real.

**Condições necessárias:**

- a plataforma utiliza notificações para informar alterações no estado dos pedidos;
- as notificações não possuem mecanismos suficientes para garantir sua autenticidade e integridade;
- o atacante consegue interceptar, reproduzir ou enviar mensagens que sejam aceitas como notificações legítimas;
- usuários ou componentes consumidores confiam no conteúdo das notificações para tomar decisões.

**Fluxo de abuso:**

1. O atacante identifica o mecanismo utilizado pela plataforma para transmitir notificações de alteração de status.
2. O atacante intercepta uma notificação legítima ou obtém informações suficientes para reproduzir o formato esperado pelo sistema.
3. O atacante modifica o conteúdo da mensagem ou cria uma nova notificação indicando um estado diferente do estado real do pedido.
4. A mensagem adulterada é encaminhada ao usuário ou componente responsável pelo processamento da notificação.
5. O destinatário aceita a mensagem como legítima por não conseguir verificar adequadamente sua autenticidade ou integridade.
6. O cliente, estabelecimento ou outro componente passa a considerar o pedido como estando no estado informado na mensagem falsa.
7. O atacante utiliza a informação adulterada para induzir decisões incorretas, como acreditar que um pedido foi entregue, cancelado ou teve seu pagamento confirmado.

**Impacto esperado:** desinformação sobre o estado dos pedidos, decisões incorretas por usuários ou componentes do sistema, disputas sobre operações realizadas e possibilidade de utilização da notificação falsificada como etapa de ataques posteriores.

**Categorias STRIDE relacionadas:** Tampering, Spoofing.

---

### CA09 — Manipulação das avaliações para prejudicar a reputação de um estabelecimento ou entregador

**Ator:** usuário mal-intencionado ou atacante com acesso à API.

**Objetivo:** alterar, inserir ou remover avaliações para prejudicar artificialmente a reputação de um estabelecimento ou entregador.

**Condições necessárias:**

- as avaliações são armazenadas e gerenciadas por meio da API;
- a API não verifica adequadamente a identidade do autor ou sua relação com o pedido avaliado;
- o atacante consegue modificar os dados enviados na requisição ou acessar avaliações de terceiros;
- não existem mecanismos suficientes para impedir alterações ou avaliações incompatíveis com os pedidos realizados.

**Fluxo de abuso:**

1. O atacante identifica a funcionalidade utilizada para registrar ou consultar avaliações.
2. O atacante analisa as requisições enviadas pela aplicação durante o registro de uma avaliação.
3. O atacante modifica os parâmetros da requisição, como o identificador do pedido, do estabelecimento, do entregador ou o conteúdo da avaliação.
4. A API recebe os dados manipulados sem verificar adequadamente se o atacante está autorizado a avaliar ou alterar aquele registro.
5. O sistema registra a avaliação ou alteração como se fosse uma operação legítima.
6. O atacante repete o procedimento para inserir múltiplas avaliações ou alterar avaliações existentes.
7. A reputação do estabelecimento ou entregador é alterada artificialmente nas informações apresentadas aos demais usuários.

**Impacto esperado:** dano à reputação de estabelecimentos ou entregadores, distorção das avaliações apresentadas aos usuários e possível perda de clientes ou oportunidades de trabalho.

**Categorias STRIDE relacionadas:** Tampering, Repudiation.

---

### CA10 — Manipulação de registros de auditoria para ocultar uma operação fraudulenta

**Ator:** atacante que obteve acesso indevido a componentes internos ou usuário privilegiado mal-intencionado.

**Objetivo:** alterar ou remover registros de auditoria para dificultar a identificação de uma operação fraudulenta.

**Condições necessárias:**

- os registros de auditoria podem ser acessados ou modificados pelo componente ou usuário que realizou a operação;
- não existe proteção adequada contra alteração ou exclusão dos registros após sua criação;
- os registros de auditoria são utilizados como evidência das operações realizadas na plataforma.

**Fluxo de abuso:**

1. O atacante obtém acesso a uma conta ou componente com permissão suficiente para executar uma operação fraudulenta.
2. O atacante realiza uma operação sensível, como alteração de dados, cancelamento ou movimentação relacionada a um pedido.
3. A plataforma registra a operação nos mecanismos de auditoria.
4. O atacante identifica os registros relacionados à operação realizada.
5. O atacante altera ou remove os registros que poderiam associar a operação à sua identidade ou ao momento em que ela foi executada.
6. Uma investigação posterior consulta os registros de auditoria e não encontra evidências suficientes da operação original.
7. O atacante utiliza a ausência ou adulteração dos registros para dificultar a identificação da origem da fraude e eventual responsabilização.

**Impacto esperado:** perda de confiabilidade dos registros de auditoria, dificuldade de investigação de incidentes, comprometimento da capacidade de responsabilização dos envolvidos e possibilidade de ocultação de operações fraudulentas.

**Categorias STRIDE relacionadas:** Repudiation, Tampering.

---

### CA11 — Acesso indevido às informações da conta de outro usuário por falha de autorização

**Ator:** cliente autenticado ou atacante externo com uma conta válida na plataforma.

**Objetivo:** acessar informações ou operações pertencentes a outro usuário, explorando uma falha no controle de autorização da API.

**Condições necessárias:**

- a API utiliza identificadores de usuários, pedidos ou outros recursos fornecidos nas requisições;
- o servidor não verifica adequadamente se o recurso solicitado pertence ao usuário autenticado;
- o atacante consegue obter ou inferir o identificador de outro usuário ou pedido.

**Fluxo de abuso:**

1. O atacante autentica-se normalmente na plataforma utilizando sua própria conta.
2. O atacante identifica ou obtém o identificador de um pedido ou recurso pertencente a outro usuário.
3. O atacante envia uma requisição à API substituindo o identificador de seu próprio recurso pelo identificador da vítima.
4. A API autentica o atacante, mas não verifica corretamente se ele possui autorização para acessar o recurso solicitado.
5. O sistema retorna informações pertencentes ao outro usuário ou permite a execução de uma operação sobre o recurso.
6. O atacante repete o procedimento para consultar outros recursos, caso os identificadores sejam previsíveis ou possam ser obtidos sucessivamente.

**Impacto esperado:** exposição de dados pessoais e informações de pedidos de terceiros, possibilidade de alteração indevida de recursos e violação do isolamento entre contas de usuários.

**Categorias STRIDE relacionadas:** Information Disclosure, Elevation of Privilege.

---

### CA12 — Exposição de endereço e localização de usuários por acesso indevido aos dados de entrega

**Ator:** atacante externo ou usuário autenticado mal-intencionado.

**Objetivo:** obter informações de localização de clientes ou entregadores às quais não deveria possuir acesso.

**Condições necessárias:**

- a API disponibiliza endereço de entrega ou localização do entregador para funcionalidades relacionadas aos pedidos;
- o servidor não verifica adequadamente se o usuário possui autorização para acessar essas informações;
- o atacante consegue identificar ou consultar pedidos ou recursos de outros usuários.

**Fluxo de abuso:**

1. O atacante autentica-se na plataforma ou obtém acesso a uma interface que permite consultar dados de pedidos.
2. O atacante identifica o identificador de um pedido que não lhe pertence.
3. O atacante envia uma requisição à API solicitando os dados associados ao pedido.
4. A API retorna informações de endereço, localização ou outros dados de entrega sem verificar adequadamente a autorização do solicitante.
5. O atacante utiliza as informações obtidas para identificar o endereço de um cliente ou acompanhar a localização de um entregador.
6. Caso a localização seja atualizada continuamente, o atacante pode realizar novas consultas para acompanhar o deslocamento do entregador durante a entrega.

**Impacto esperado:** violação da privacidade de clientes e entregadores, exposição indevida de endereços e localização em tempo real e possível risco à segurança física das pessoas envolvidas.

**Categorias STRIDE relacionadas:** Information Disclosure.

---

### CA13 — Vazamento de dados pessoais por acesso indevido à API

**Ator:** atacante externo ou usuário autenticado mal-intencionado.

**Objetivo:** obter dados pessoais de clientes, entregadores ou estabelecimentos que não deveriam estar disponíveis ao atacante.

**Condições necessárias:**

- a API disponibiliza dados pessoais para diferentes funcionalidades do sistema;
- determinados endpoints não verificam adequadamente a autorização do usuário para acessar os dados solicitados;
- o atacante consegue identificar ou inferir identificadores de usuários ou outros recursos existentes na plataforma.

**Fluxo de abuso:**

1. O atacante autentica-se na plataforma ou identifica endpoints que permitem consultar dados por meio da API.
2. O atacante identifica ou obtém o identificador de um usuário ou recurso que não lhe pertence.
3. O atacante envia uma requisição à API utilizando o identificador obtido.
4. A API autentica o solicitante, mas não verifica adequadamente se ele possui autorização para consultar os dados associados ao recurso.
5. O servidor retorna informações pessoais pertencentes ao usuário consultado.
6. O atacante repete as consultas utilizando diferentes identificadores para obter dados de outros usuários.
7. Caso a API permita consultas automatizadas, o atacante pode ampliar a coleta e obter uma quantidade significativa de registros.

**Impacto esperado:** exposição indevida de dados pessoais, violação da privacidade de clientes, entregadores ou estabelecimentos e possibilidade de utilização das informações obtidas em ataques posteriores, como phishing ou engenharia social.

**Categorias STRIDE relacionadas:** Information Disclosure.

---

### CA14 — Exposição de informações financeiras por acesso indevido ao histórico de transações

**Ator:** atacante externo ou usuário autenticado mal-intencionado.

**Objetivo:** obter informações financeiras e transacionais pertencentes a outro usuário ou estabelecimento.

**Condições necessárias:**

- a plataforma disponibiliza histórico de pedidos, pagamentos, estornos ou repasses por meio da API;
- a API não verifica adequadamente se o solicitante possui autorização para acessar o histórico consultado;
- o atacante consegue identificar ou inferir identificadores de usuários, pedidos ou transações.

**Fluxo de abuso:**

1. O atacante autentica-se na plataforma utilizando uma conta legítima ou obtém acesso a um endpoint de consulta do histórico de transações.
2. O atacante identifica o identificador de uma conta, pedido ou transação que não lhe pertence.
3. O atacante envia uma requisição à API utilizando o identificador obtido.
4. A API verifica a identidade do solicitante, mas não valida adequadamente sua autorização para acessar o histórico solicitado.
5. O servidor retorna informações financeiras relacionadas às transações do usuário ou estabelecimento.
6. O atacante repete as consultas para obter informações de outras contas ou transações.
7. As informações obtidas podem ser armazenadas ou utilizadas para identificar padrões de consumo, valores movimentados ou outras informações financeiras dos usuários.

**Impacto esperado:** exposição de informações financeiras e transacionais, violação da privacidade dos usuários e estabelecimentos e possibilidade de utilização das informações obtidas em ataques posteriores ou fraudes direcionadas.

**Categorias STRIDE relacionadas:** Information Disclosure.

---

### CA15 — Utilização indevida de dados de localização para rastrear entregadores fora de uma entrega autorizada

**Ator:** atacante externo ou usuário autenticado mal-intencionado.

**Objetivo:** acompanhar a localização de um entregador mesmo quando não existe uma relação legítima com o pedido ou com a entrega em andamento.

**Condições necessárias:**

- a plataforma disponibiliza dados de localização do entregador durante o acompanhamento das entregas;
- os dados de localização permanecem acessíveis após o encerramento ou alteração da relação entre usuário e entrega;
- a API não verifica adequadamente se o solicitante ainda possui autorização para consultar a localização;
- o atacante consegue identificar o entregador ou o recurso utilizado para consultar sua localização.

**Fluxo de abuso:**

1. O atacante obtém acesso a uma conta legítima da plataforma ou identifica um mecanismo de consulta de localização.
2. O atacante identifica o identificador de um pedido ou entregador cuja localização deseja acompanhar.
3. Após a entrega ser encerrada, cancelada ou deixar de estar associada ao atacante, ele envia novas requisições à API para consultar a localização.
4. A API retorna as coordenadas sem verificar adequadamente se ainda existe uma relação autorizada entre o solicitante e o entregador.
5. O atacante realiza consultas sucessivas para obter novas posições do entregador.
6. A partir das coordenadas obtidas, o atacante consegue acompanhar o deslocamento do entregador mesmo fora do contexto da entrega original.

**Impacto esperado:** violação da privacidade do entregador, exposição de seus deslocamentos e rotinas e possível risco à sua segurança pessoal.

**Categorias STRIDE relacionadas:** Information Disclosure.

---

### CA16 — Tentativas automatizadas de cupons para descobrir códigos válidos

**Ator:** atacante externo ou cliente mal-intencionado.

**Objetivo:** identificar códigos de cupons válidos por meio de tentativas automatizadas e utilizá-los para obter descontos indevidos.

**Condições necessárias:**

- a plataforma permite que usuários submetam códigos de cupom para validação;
- a API fornece respostas diferentes dependendo da existência ou validade do código informado;
- não existe limitação adequada para o número de tentativas de validação realizadas por uma conta ou endereço de origem;
- os códigos de cupom possuem formato ou espaço de possibilidades que permite tentativas automatizadas.

**Fluxo de abuso:**

1. O atacante identifica a funcionalidade da plataforma responsável pela validação de cupons.
2. O atacante analisa as respostas retornadas pela API para códigos válidos, inválidos, expirados ou inexistentes.
3. O atacante automatiza o envio de diferentes combinações de códigos de cupom.
4. A API processa as tentativas sem aplicar uma limitação adequada à quantidade de consultas.
5. O atacante identifica os códigos que produzem uma resposta indicando que o cupom é válido.
6. O atacante utiliza os códigos descobertos em pedidos próprios ou os compartilha com outros usuários.
7. Caso os cupons possuam limitações de utilização que também possam ser contornadas, o atacante pode repetir o abuso em múltiplos pedidos.

**Impacto esperado:** utilização indevida de campanhas promocionais, concessão de descontos não planejados e prejuízo financeiro limitado à plataforma ou aos estabelecimentos participantes.

**Categorias STRIDE relacionadas:** Information Disclosure, Denial of Service.

---

### CA17 — Enumeração de usuários por respostas diferentes da API

**Ator:** atacante externo.

**Objetivo:** identificar quais usuários possuem contas cadastradas na plataforma para obter uma base de contas válidas.

**Condições necessárias:**

- a API possui funcionalidades que recebem identificadores como e-mail, telefone ou nome de usuário;
- a API retorna respostas diferentes para identificadores cadastrados e não cadastrados;
- não existe mecanismo adequado para impedir ou limitar consultas automatizadas;
- o atacante consegue realizar várias consultas à funcionalidade vulnerável.

**Fluxo de abuso:**

1. O atacante identifica uma funcionalidade da plataforma que permite consultar ou validar a existência de usuários.
2. O atacante envia uma requisição utilizando um e-mail, telefone ou outro identificador de possível usuário.
3. A API retorna uma resposta que permite distinguir entre um usuário existente e um usuário inexistente.
4. O atacante registra o resultado da consulta e envia uma nova requisição utilizando outro identificador.
5. O procedimento é automatizado para consultar uma grande quantidade de identificadores.
6. O atacante constrói uma lista de usuários potencialmente cadastrados na plataforma.
7. A lista obtida pode ser utilizada posteriormente para ataques direcionados, como tentativas de comprometimento de contas, phishing ou engenharia social.

**Impacto esperado:** exposição indireta da existência de contas de usuários, violação de privacidade e fornecimento de informações que podem facilitar ataques posteriores direcionados.

**Categorias STRIDE relacionadas:** Information Disclosure.

---

### CA18 — Bloqueio de contas legítimas por abuso do mecanismo de autenticação

**Ator:** atacante externo.

**Objetivo:** impedir que usuários legítimos acessem suas contas por meio da exploração do mecanismo automático de bloqueio após tentativas consecutivas de autenticação.

**Condições necessárias:**

- o sistema bloqueia temporariamente uma conta após determinado número de tentativas de autenticação malsucedidas;
- o mecanismo de bloqueio pode ser acionado por terceiros sem exigir uma prova adicional de controle da conta;
- não existe proteção adequada contra tentativas automatizadas de autenticação.

**Fluxo de abuso:**

1. O atacante identifica o identificador de uma conta legítima da plataforma.
2. O atacante envia repetidamente tentativas de autenticação inválidas para essa conta.
3. O sistema contabiliza as tentativas como falhas legítimas de autenticação.
4. Após atingir o limite configurado, o mecanismo de proteção bloqueia temporariamente a conta.
5. O usuário legítimo tenta acessar sua conta e não consegue realizar a autenticação devido ao bloqueio.
6. O atacante repete o procedimento sempre que a conta é desbloqueada, mantendo o acesso do usuário legítimo indisponível.

**Impacto esperado:** indisponibilidade temporária de contas legítimas, impedimento de realização ou acompanhamento de pedidos e transtornos aos usuários afetados, sem necessariamente resultar em comprometimento das contas.

**Categorias STRIDE relacionadas:** Denial of Service.

---