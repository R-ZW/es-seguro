# `Yummers` - Aplicativo de delivery

### Conteúdo da página:

> [5.1 Listagem das ameaças](#51-listagem-das-ameaças)<br>
> [5.2 Interpretação e análise](#52-interpretação-e-análise)<br>

---

## 🎯 5. Modelagem de ameaças com STRIDE

### 5.1 Listagem das ameaças

| ID | Categoria STRIDE | Componente ou ativo | Ameaça identificada | Possível impacto |
| --- | --- | --- | --- | --- |
| T01 | Spoofing | Conta do usuário (Cliente, Entregador ou Estabelecimento) | Um atacante utiliza credenciais roubadas (phishing, vazamento de senha reutilizada) para autenticar-se como outro usuário | Acesso a dados pessoais/financeiros, realização de pedidos ou saques fraudulentos em nome da vítima |
| T02 | Spoofing | Sessão do usuário | Um atacante forja ou rouba um token de acesso de sessão para se passar por outro usuário | Acesso total à conta de outro usuário sem saber a senha |
| T03 | Spoofing | Cadastro de estabelecimento ou entregador | Um atacante cria um cadastro de estabelecimento ou entregador com documentos falsificados/roubados, passando pela aprovação do Administrador | Operação de uma entidade falsa na plataforma, fraudes em massa, dano à confiança da plataforma |
| T04 | Spoofing | Cadastro de cliente | Um atacante cria uma conta de cliente usando dados pessoais de terceiros (nome, CPF, endereço) obtidos de vazamentos, para realizar pedidos fraudulentos com cartão roubado | Fraude de pagamento (chargeback), prejuízo ao gateway/plataforma, dano à pessoa cujos dados foram usados |
| T05 | Tampering | Valor do pedido ou carrinho | Um cliente malicioso intercepta e altera os dados de finalização do pedido, reduzindo o valor total antes de prosseguir para o pagamento | Prejuízo financeiro ao estabelecimento e à plataforma, pedidos processados por valor incorreto |
| T06 | Tampering | Localização do Entregador | Um entregador malicioso manipula a localização reportada pelo dispositivo (e.g. via Fake GPS/Modo desenvolvedor do Android) para apresentar ao sistema uma posição diferente da real, driblando a necessidade de atualizar localização | Entregador aceita pedido sem intenção de cumprir a rota real, gerando informações de rastreamento incorretas e dificuldade de auditoria em disputas sobre atraso ou desvio |
| T07 | Tampering | Avaliações (estabelecimento e entregador) | Um atacante manipula diretamente notas e comentários de avaliações após o envio sem ter feito pedidos ao estabelecimento ou usado os serviços de um entregador | Distorção de métricas de reputação, prejuízo a estabelecimentos/entregadores honestos, decisões de outros clientes baseadas em dados falsos |
| T08 | Tampering | Cardápio / preços do estabelecimento | Um atacante com acesso não autorizado ao Portal Web altera preços ou itens do cardápio de um estabelecimento vítima, sem sua permissão | Prejuízo financeiro ao estabelecimento, pedidos feitos com informações incorretas, dano à sua reputação |
| T09 | Tampering | Cupom de desconto | Um atacante ou cliente malicioso manipula a aplicação de cupom (e.g. reenvia um cupom já utilizado/expirado, ou altera o percentual de desconto) explorando validação insuficiente | Prejuízo financeiro à plataforma/estabelecimento, uso indevido de promoções além do limite permitido |
| T10 | Repudiation | Confirmação de retirada | Um entregador malicioso nega ter escaneado a Chave de Coleta e retirado o pedido do estabelecimento, alegando falha no aplicativo | Estabelecimento não consegue provar que a entrega foi retirada, disputa sobre responsabilidade pelo pedido extraviado |
| T11 | Repudiation | Confirmação de entrega | Um cliente malicioso nega ter recebido o pedido mesmo após ter fornecido a Chave de Entrega ao entregador, alegando não reconhecer a ação. | Disputa não resolvível, possível estorno indevido ao cliente e prejuízo ao entregador/estabelecimento que já cumpriram sua parte |
| T12 | Repudiation | Cancelamento de pedido | Um cliente/estabelecimento malicioso nega ter realizado o cancelamento de um pedido (alegando que foi um erro do sistema ou de terceiros), contestando a multa aplicada | Disputa sobre cobrança de multa, necessidade de mediação manual pelo Administrador, desgaste na relação com o usuário |
| T13 | Repudiation | Aceite de solicitação de entrega | Um entregador malicioso nega ter aceitado uma rota específica (alegando que o app aceitou sozinho ou por engano), buscando se eximir de penalidades por abandono ou atraso | Impossibilidade de responsabilizar o entregador por não cumprir a rota aceita, prejuízo à confiabilidade do sistema de atribuição |
| T14 | Repudiation | Ações administrativas (aprovação/suspensão de contas, estornos manuais) | Um administrador malicioso nega ter executado uma ação sensível (e.g. aprovar um cadastro fraudulento, autorizar um estorno manual) por falta de logs de auditoria vinculados à sua identidade | Impossibilidade de responsabilizar internamente o administrador, dificuldade em investigar fraudes ou abusos internos |
| T15 | Information Disclosure | Localização em tempo real do entregador/endereço do cliente | Uma falha de autorização na API permite que um usuário acesse a rota/localização de um pedido que não é seu, expondo endereço residencial do cliente ou trajeto do entregador | Violação de privacidade, risco físico ao cliente (exposição de endereço) e ao entregador (exposição de rotina/trajeto) |
| T16 | Information Disclosure | Dados pessoais dos usuários | Uma falha de configuração ou vulnerabilidade permite acesso não autorizado a dados cadastrais de clientes, entregadores e estabelecimentos | Vazamento em massa de dados pessoais (nome, CPF, endereço), exposição legal (LGPD), dano reputacional grave |
| T17 | Information Disclosure | Dados financeiros e de pagamento | Falha no tratamento ou armazenamento de dados sensíveis de pagamento expõe informações financeiras dos usuários | Fraude financeira contra os usuários, responsabilização legal da plataforma |
| T18 | Information Disclosure | Mensagens de erro | O sistema retorna mensagens de erro detalhadas (e. g.: stack traces, estrutura do banco) ou verbosas (e.g. "usuário não encontrado", "senha incorreta") expondo dados técnicos internos ou permitindo acesso a informações reservadas. | Facilita o reconhecimento da infraestrutura e detalhes internos por um atacante, servindo de base para outros ataques mais direcionados |
| T19 | Denial of Service | API do Sistema | Um atacante realiza um ataque volumétrico (flood de requisições) contra a API durante o horário de pico de refeições, esgotando recursos do servidor | Indisponibilidade do serviço no momento de maior demanda, perda de pedidos e receita, insatisfação generalizada de usuários |
| T20 | Denial of Service | Gateway de Pagamento | Um atacante abusa repetidamente da integração de pagamentos com tentativas de transações inválidas/repetidas (e.g. cartões de teste em loop), levando o Gateway externo a limitar ou bloquear a integração com a plataforma | Impossibilidade temporária de qualquer cliente finalizar pagamentos, paralisação do fluxo de novos pedidos |
| T21 | Denial of Service | Conta de usuário | Um atacante realiza tentativas massivas de login contra contas específicas, acionando bloqueios automáticos de segurança e impedindo que os usuários legítimos acessem suas contas | Indisponibilidade de acesso para clientes, entregadores ou estabelecimentos legítimos |
| T22 | Denial of Service | Banco de dados | Um atacante explora uma consulta mal otimizada ou não paginada (e.g. busca de estabelecimentos sem limites) para forçar consultas custosas repetidas, sobrecarregando o banco de dados | Lentidão ou indisponibilidade generalizada do sistema para todos os usuários |
| T23 | Elevation of Privilege | Sessão/Token de autenticação | Um atacante explora uma vulnerabilidade no Serviço de Autenticação para adulterar as permissões do próprio token e assumir um nível superior ao originalmente concedido | Acesso não autorizado a funcionalidades de qualquer perfil superior, comprometimento amplo do controle de acesso do sistema |
| T24 | Elevation of Privilege | Rotas administrativas | Falta de checagem de role no backend: front-end esconde botões de Admin, mas a API não valida a role do usuário no servidor; atacante descobre os endpoints de Administrador chama diretamente com sua própria sessão de cliente | Acesso não autorizado a funcionalidades de qualquer perfil superior, comprometimento amplo do controle de acesso do sistema |
| T25 | Elevation of Privilege | Fluxo de aprovação de estabelecimentos ou entregadores | Um Estabelecimento ou Entregador com cadastro ainda pendente consegue acessar funcionalidades operacionais reservadas a parceiros já aprovados. | Operação de parceiros não validados na plataforma, riscos de fraude e segurança para clientes que interagem com eles sem saber |
| T26 | Elevation of Privilege | Liberação de repasse/caução (fluxo de escrow) | Um Estabelecimento ou Entregador aciona diretamente o endpoint interno responsável por liberar o repasse, sem que a validação real da Chave de Coleta/Entrega tenha ocorrido, por falta de checagem server-side de que a etapa anterior do fluxo foi cumprida | Liberação indevida de valores retidos em custódia sem entrega efetivamente confirmada, prejuízo financeiro direto à plataforma/cliente |

### 5.2 Interpretação e análise

A análise das ameaças evidencia a necessidade de proteger diferentes aspectos da plataforma. A autenticação deve garantir que cada usuário seja corretamente identificado; as informações e operações dos pedidos devem manter sua integridade; as ações realizadas no sistema precisam ser rastreáveis e passíveis de comprovação; os dados pessoais, financeiros e de localização devem permanecer restritos a quem possui autorização; os principais serviços devem continuar disponíveis mesmo diante de tentativas de indisponibilização; e as funcionalidades de maior privilégio devem estar limitadas aos perfis que realmente possuem permissão para executá-las.

---
<center>
<table width="100%">
<tr>
<td align="left">

[⬅️ Página anterior](4%20-%20Visão%20geral%20da%20arquitetura%20e%20fluxos%20de%20uso.md)

</td>

<td align="center">

3️⃣

</td>

<td align="right">

[Próxima página ➡️](6%20-%20Casos%20de%20abuso.md)

</td>
</tr>
</table>
</center>

### **Índice**:

**Etapa 1**:

1. [**🆔 Identificação do sistema**](../../README.md)
2. [**📝 Descrição do sistema**](../../README.md)
3. [**👥 Usuários, ativos e pontos de interação**](3%20-%20Usuários,%20ativos%20e%20pontos%20de%20interação.md)
4. [**🔀 Visão geral da arquitetura e fluxos de uso**](4%20-%20Visão%20geral%20da%20arquitetura%20e%20fluxos%20de%20uso.md) 
5. [**🎯 Modelagem de ameaças com STRIDE**](#5-modelagem-de-ameaças-com-stride) 👈
6. [**🚨 Casos de abuso**](6%20-%20Casos%20de%20abuso.md)
7. [**📌 Considerações finais da Etapa 1**](7%20-%20Considerações%20finais%20da%20Etapa%201.md)


**Etapa 2**:

8. [**🛡️ Análise e priorização dos riscos**](../etapa-2/8%20-%20Análise%20e%20priorização%20dos%20riscos.md)
9. [**🧩 Tratamento dos riscos com NIST CSF**](../etapa-2/9%20-%20Tratamento%20dos%20riscos%20com%20NIST%20CSF.md)


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