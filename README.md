# `Yummers` - Aplicativo de delivery

## 🆔 1. Identificação do sistema

> **Nome do sistema:** `Yummers` - Aplicativo de delivery<br>
> **Repositório:** https://github.com/R-ZW/es-seguro/<br><br>
> **Justificativa:** O sistema foi escolhido por possuir múltiplos perfis de acesso (clientes, estabelecimentos, entregadores e administradores) e por gerenciar um volume considerável de dados sensíveis e regras de negócio críticas. A arquitetura de pagamentos intermediada (retendo valores até a confirmação da entrega), o gerenciamento de crédito de caução e o rastreamento de localização em tempo real geram uma superfície ampla e rica para a identificação de ameaças e vulnerabilidades.

#### **Integrantes:** 

| Username do GitHub   | Nome Completo                 | Matrícula   |
|----------------------|-------------------------------|-------------|
| ```AndreLGDM```      | André Luiz Gomes Medeiros     | 1901560736  |
| ```Erik-Fontella```  | Erik Ricarde Fontella         | 2210100252  |
| ```MiguelYSieghart```| Miguel Ângelo Bastos Muniz    | 2310101615  |
| ```R-ZW```           | Reinaldo Zimmer Wendt         | 2310100642  |


## 📝 2. Descrição do sistema

O `Yummers` é uma **plataforma de delivery** que intermedia a conexão entre clientes, estabelecimentos gastronômicos e entregadores e leva como base a política de *escrow* para evitar, via lógica de negócio, que determinados abusos venham a ocorrer. O sistema permite que **clientes** naveguem por cardápios, realizem pedidos com pagamentos retidos em custódia e acompanhem a rota de entrega. **Estabelecimentos** utilizam a plataforma para gerenciar seus catálogos, definir políticas de multas, aceitar demandas e coordenar o preparo e despacho dos pedidos. **Entregadores** controlam sua disponibilidade, gerenciam saldos de caução, aceitam solicitações de rota e atualizam suas coordenadas geográficas. Por fim, **administradores** moderam cadastros, gerenciam chamados de suporte e supervisionam a plataforma. Para sustentar essas operações, o sistema processa e armazena dados de identificação pessoal, credenciais de acesso, registros de geolocalização, informações financeiras e históricos completos de transações.

---
<center>
<table width="100%">
<tr>
<td align="left">

⬅️ Página anterior
</td>

<td align="center">

1️⃣
</td>

<td align="right">

[Próxima página ➡️](./docs/etapa-1/3%20-%20Usuários,%20ativos%20e%20pontos%20de%20interação.md)
</td>
</tr>
</table>
</center>

### Sumário:

1. [🆔 Identificação do sistema](#-1-identificação-do-sistema) 👈 
2. [📝 Descrição do sistema](#-2-descrição-do-sistema) 👈
3. [👥 Usuários, ativos e pontos de interação](docs/etapa-1/3%20-%20Usuários,%20ativos%20e%20pontos%20de%20interação.md)
4. [🔀 Visão geral da arquitetura e fluxos de uso](#)
5. [🎯 Modelagem de ameaças com STRIDE](#)
6. [🚨 Casos de abuso](#)
7. [📌 Considerações finais](#)

---