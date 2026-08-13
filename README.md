# `Yummers` - Aplicativo de delivery

### Conteúdo da página:

> [1. Identificação do sistema](#-1-identificação-do-sistema)<br>
> [2. Descrição do sistema](#-2-descrição-do-sistema)<br>

---

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

0️⃣

</td>

<td align="right">

[Próxima página ➡️](docs/etapa-1/3%20-%20Usuários,%20ativos%20e%20pontos%20de%20interação.md)

</td>
</tr>
</table>
</center>

### **Índice**:

**Etapa 1**:

1. [**🆔 Identificação do sistema**](#-1-identificação-do-sistema) 👈
2. [**📝 Descrição do sistema**](#-2-descrição-do-sistema) 👈
3. [**👥 Usuários, ativos e pontos de interação**](docs/etapa-1/3%20-%20Usuários,%20ativos%20e%20pontos%20de%20interação.md) 
4. [**🔀 Visão geral da arquitetura e fluxos de uso**](docs/etapa-1/4%20-%20Visão%20geral%20da%20arquitetura%20e%20fluxos%20de%20uso.md)
5. [**🎯 Modelagem de ameaças com STRIDE**](docs/etapa-1/5%20-%20Modelagem%20de%20ameaças%20com%20STRIDE.md)
6. [**🚨 Casos de abuso**](docs/etapa-1/6%20-%20Casos%20de%20abuso.md)
7. [**📌 Considerações finais da Etapa 1**](docs/etapa-1/7%20-%20Considerações%20finais%20da%20Etapa%201.md)


**Etapa 2**:

8. [**🛡️ Análise e priorização dos riscos**](docs/etapa-2/8%20-%20Análise%20e%20priorização%20dos%20riscos.md)
9. [**🧩 Tratamento dos riscos com NIST CSF**](docs/etapa-2/9%20-%20Tratamento%20dos%20riscos%20com%20NIST%20CSF.md)


**Etapa 3**:

10. [**🏗️ Arquitetura segura**](docs/etapa-3/10%20-%20Arquitetura%20segura.md)


**Etapa 4**:

11. [**💻 Código seguro e testes de segurança**](docs/etapa-4/11%20-%20Código%20seguro%20e%20testes%20de%20segurança.md)


**Etapa 5**:

12. [**🔎 Verificação de vulnerabilidades**](docs/etapa-5/12%20-%20Verificação%20de%20vulnerabilidades.md)


**Etapa 6**:

13. [**📡 Monitoramento e detecção de intrusões**](roteiros/etapa-6-deteccao-de-intrusoes.md)


**Etapa 7**:

14. [**🎥 DevSecOps e vídeo final**](roteiros/etapa-7-devsecops-e-video-final.md)

---