# `Yummers` - Aplicativo de delivery

## 3. Usuários, ativos e pontos de interação

### 3.1 Usuários e perfis

| Usuário/Perfil      | Principais ações |
|---------------------|------------------|
| **Cliente**         | Buscar estabelecimentos, realizar pedidos, efetuar pagamentos, acompanhar a rota de entrega, cancelar pedidos e avaliar a experiência. |
| **Estabelecimento** | Gerenciar cardápio e política de multas, receber pedidos, atualizar status de preparo, solicitar entrega e finalizar pedidos. |
| **Entregador**      | Gerenciar crédito de caução, alterar disponibilidade, aceitar solicitações de entrega, atualizar localização em tempo real e confirmar retiradas/entregas. |
| **Administrador**   | Gerenciar contas, aprovar cadastros de parceiros (estabelecimentos e entregadores), monitorar o fluxo de pedidos e gerenciar chamados de suporte.  |

> **Observação**: Todos os perfis (exceto o Administrador) herdam as ações comuns de um "Usuário Externo", que incluem realizar cadastro, manter perfil, manter sessão e abrir chamados de suporte.


### 3.2 Ativos importantes

Os principais ativos identificados que precisam ser protegidos são:

- Credenciais de acesso e tokens de sessão;
- Dados pessoais e de contato (clientes, entregadores e responsáveis pelos estabelecimentos);
- Dados financeiros e de pagamento (cartões, PIX, contas bancárias para repasse);
- Valores transacionados, retidos em custódia e créditos de caução;
- Localização em tempo real (dados de GPS dos entregadores e endereços dos clientes);
- Informações de negócio (cardápios, preços e políticas de multas);
- Histórico de pedidos, avaliações e métricas de desempenho;
- Permissões e privilégios dos perfis de usuários;
- Registros e logs das operações (essenciais para auditoria de estornos, cancelamentos e confirmações de entrega);
- Disponibilidade do sistema (crítica durante os horários de pico de refeições).


### 3.3 Pontos de interação e componentes

| Elemento                                | Principais ações |
|-----------------------------------------|------------------|
| **Aplicativo Mobile**                   | Interface principal utilizada por clientes (para compras) e entregadores (para rotas e gestão de entregas). |
| **Portal Web (Painel)**                 | Interface utilizada pelos estabelecimentos (gestão operacional) e administradores (gestão da plataforma). |
| **API do Sistema (Backend)**            | Processa as regras de negócio, gerencia o fluxo de pedidos, cauções e integra as interfaces aos dados. |
| **Banco de Dados**                      | Armazena dados cadastrais, financeiros, catálogos, históricos e registros de auditoria (logs). |
| **Serviço de Autenticação (Externo)**   | Valida a identidade, credenciais e gerencia as sessões de todos os usuários. |
| **Gateway de Pagamento (Externo)**      | Intermediário responsável por processar cobranças, reter valores em custódia, processar estornos e efetuar repasses. |
| **Serviço de Notificações (Externo)**   | Envia alertas push, e-mails e atualizações de status dos pedidos aos usuários. |
| **Serviço de Geolocalização (Externo)** | Fornece mapas, cálculo de rotas e processa o rastreamento em tempo real dos entregadores. |

---
<br>
<table width="100%">
<tr>
<td align="left">

[⬅️ Página anterior](./../../README.md)
</td>

<td align="center">

2️⃣
</td>

<td align="right">

[Próxima página](#) ➡️
</td>
</tr>
</table>

---

### Sumário:

1. [🆔 Identificação do sistema](./../../README.md)  
2. [📝 Descrição do sistema](./../../README.md) 
3. [👥 Usuários, ativos e pontos de interação](#) 👈
4. [🔀 Visão geral da arquitetura e fluxos de uso](#)
5. [🎯 Modelagem de ameaças com STRIDE](#)
6. [🚨 Casos de abuso](#)
7. [📌 Considerações finais](#)

---