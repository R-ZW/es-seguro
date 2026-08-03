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