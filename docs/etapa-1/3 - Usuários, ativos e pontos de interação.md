# `Yummers` - Aplicativo de delivery

### Sumário da página:

> [3.1 Usuários e perfis](#31-usuários-e-perfis)<br>
> [3.2 Ativos importantes](#32-ativos-importantes)<br>
> [3.3 Pontos de interação e componentes](#33-pontos-de-interação-e-componentes)

---

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
<center>
<table width="100%">
<tr>
<td align="left">

[⬅️ Página anterior](../../README.md)

</td>

<td align="center">

1️⃣

</td>

<td align="right">

[Próxima página ➡️](4%20-%20Visão%20geral%20da%20arquitetura%20e%20fluxos%20de%20uso.md)

</td>
</tr>
</table>
</center>

### **Índice**:

**Etapa 1**:

1. [**🆔 Identificação do sistema**](../../README.md)
2. [**📝 Descrição do sistema**](../../README.md)
3. [**👥 Usuários, ativos e pontos de interação**](#3-usuários-ativos-e-pontos-de-interação) 👈
4. [**🔀 Visão geral da arquitetura e fluxos de uso**](4%20-%20Visão%20geral%20da%20arquitetura%20e%20fluxos%20de%20uso.md)
5. [**🎯 Modelagem de ameaças com STRIDE**](5%20-%20Modelagem%20de%20ameaças%20com%20STRIDE.md)
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