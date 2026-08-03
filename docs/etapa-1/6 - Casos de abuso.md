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