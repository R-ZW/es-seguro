# `Yummers` - Aplicativo de delivery

### Conteúdo da página:

> [1. Objetivo](#1-objetivo) <br>
> [2. Pipeline DevSecOps Proposto](#2-pipeline-devsecops-proposto) <br>
> [2.1 Condições de bloqueio do pipeline](#21-condições-de-bloqueio-do-pipeline) <br>
> [2.2 Integração com as etapas anteriores](#22-integração-com-as-etapas-anteriores) <br>
> [3. Roteiro do Vídeo Final](#3-roteiro-do-vídeo-final) <br>
> [3.1 Pontos que devem aparecer no vídeo](#31-pontos-que-devem-aparecer-no-vídeo) <br>
> [3.2 Observação sobre participação](#32-observação-sobre-participação) <br>
> [4. Critérios de avaliação atendidos](#4-critérios-de-avaliação-atendidos) <br>

---

## 🎥 Etapa 7 - DevSecOps e vídeo final

## 1. Objetivo

O objetivo desta etapa é integrar o que foi produzido ao longo da disciplina e demonstrar como a segurança pode acompanhar continuamente o ciclo de desenvolvimento do `Yummers`, desde a análise de ameaças até a operação.

Não foi implementado um pipeline real. A proposta abaixo descreve uma esteira DevSecOps textual, com evidências esperadas e condições de segurança que impediriam a continuidade do fluxo.

## 2. Pipeline DevSecOps Proposto

| Momento | Atividade de segurança | Evidência produzida | Condição para continuar |
| :--- | :--- | :--- | :--- |
| **Planejamento** | Modelagem de ameaças com STRIDE, identificação de casos de abuso e análise de riscos | Tabelas de ameaças, casos de abuso e registro de riscos priorizados | Riscos prioritários identificados e aceitos para tratamento |
| **Arquitetura** | Definição de requisitos e decisões de arquitetura para mitigar os riscos | Decisões arquiteturais relacionadas a autenticação, autorização, cálculo de valores e proteção de dados | Decisões revisadas e coerentes com os riscos `R01`, `R02`, `R03`, `R05`, `R09`, `R10` e `R12` |
| **Implementação segura** | Aplicação das práticas de código seguro selecionadas na Etapa 4 | Código ou pseudocódigo com versão insegura e versão segura | Regras de validação de entrada e autorização implementadas ou descritas |
| **Testes automatizados** | Execução dos testes de segurança definidos antes da implementação | Saída dos testes automatizados da Etapa 4 | Todos os testes de segurança aprovados |
| **Análise de código e dependências** | Execução de SAST, revisão de código, SCA e busca de segredos | Relatórios de SAST/SCA, revisão por pares e verificação de segredos | Sem segredo exposto, sem dependência crítica não tratada e sem achado crítico ignorado |
| **Teste dinâmico ou pentest** | Execução de DAST ou verificação equivalente em ambiente de teste/staging | Relatório do OWASP ZAP ou ferramenta equivalente | Achados críticos e altos analisados, corrigidos ou formalmente justificados |
| **Implantação** | Publicação controlada após aprovação das verificações de segurança | Registro do deploy e evidências dos quality gates | Deploy autorizado apenas se os gates anteriores forem aprovados |
| **Monitoramento e resposta** | Coleta de logs, regras de detecção, alertas e plano de resposta | Alertas, registros de eventos, painéis e ações de resposta | Incidentes investigados, tratados e usados para retroalimentar o backlog |

### 2.1 Condições de bloqueio do pipeline

O pipeline deve ser interrompido quando uma condição de segurança impedir a continuidade segura do projeto. Para o `Yummers`, as principais condições impeditivas seriam:

1. **Teste de segurança reprovado:** qualquer teste automatizado da Etapa 4 falha, especialmente testes de manipulação de valor do pedido ou de autorização.
2. **Falha no controle de acesso:** um cliente consegue acessar pedido de outro cliente, executar ação administrativa ou contornar regras de papel/perfil.
3. **Segredo encontrado no repositório:** tokens, senhas, chaves de API ou credenciais aparecem no código, em arquivos de configuração ou no histórico versionado.
4. **Dependência conhecida como vulnerável:** uma biblioteca, imagem ou componente usado pelo sistema possui vulnerabilidade crítica ou alta sem tratamento.
5. **Vulnerabilidade crítica não analisada:** achado crítico de SAST, SCA, DAST ou pentest permanece sem correção, justificativa ou aceite formal.

### 2.2 Integração com as etapas anteriores

| Etapa anterior | Como entra no pipeline |
| :--- | :--- |
| **Etapa 1 — Usuários, arquitetura, STRIDE e casos de abuso** | Alimenta o planejamento e a identificação de ameaças. |
| **Etapa 2 — Análise, priorização e tratamento de riscos** | Define quais riscos precisam de controles e quais são mais prioritários. |
| **Etapa 3 — Decisões de arquitetura** | Transforma riscos em decisões como recálculo de valores no servidor e autorização centralizada. |
| **Etapa 4 — Código seguro e testes** | Demonstra duas práticas implementáveis: validação de entrada/valor do pedido e controle de autorização. |
| **Etapas de verificação e detecção** | Produzem evidências de testes dinâmicos, alertas, logs e regras de resposta. |
| **Etapa 7 — DevSecOps e vídeo final** | Integra as evidências e mostra a evolução do projeto. |

## 3. Roteiro do Vídeo Final

**Tempo estimado:** 5 a 8 minutos.  
**Participantes:** André, Erik, Miguel e Reinaldo.

| Tempo aprox. | Responsável | Seção | Descrição da fala e conteúdo visual |
| :--- | :--- | :--- | :--- |
| **0:00 - 0:50** | **Reinaldo** | **Descrição geral do sistema** | Apresenta o `Yummers`, aplicativo de delivery com política de *escrow*, seus quatro perfis de usuário (cliente, estabelecimento, entregador e admin) e a importância da proteção dos dados. **Visual**: Repositório. |
| **0:50 - 1:50** | **Reinaldo** | **Etapa 1** | Traz as principais ameaças STRIDE e Casos de Abuso levantados, com ênfase no spoofing de contas (T01) e adulteração do valor do pedido (T05), acesso como admin (T23,T24). **Visual**: Repositório. |
| **1:50 - 2:40** | **André** | **Etapa 2** | Explica a priorização dos riscos com o framework NIST CSF. Destaca os riscos críticos, como o acesso a informações alheias e roubo de credenciais, apontando estratégias como MFA. **Visual**: Repositório. |
| **2:40 - 3:30** | **Reinaldo** | **Etapa 3** | Expõe as decisões arquiteturais criadas para mitigar os riscos críticos: *Source of Truth* no servidor (calculando valores) e Middleware centralizado de autorização. **Visual**: Repositório. |
| **3:30 - 4:30** | **Miguel** | **Etapa 4** | Demonstra como a arquitetura virou código seguro. Explica as práticas aplicadas (validação de valores e role-based access) e mostra os casos de testes antes de implementar. **Visual**: Repositório e execução dos testes. |
| **4:30 - 5:20** | **Erik** | **Etapa 5** | Apresenta a sessão prática de verificação com a ferramenta OWASP ZAP. Aponta os achados mais críticos levantados nos alertas do relatório e como eles se ligam às ameaças. **Visual**: Repositório e captura de tela do relatório ZAP. |
| **5:20 - 6:20** | **André** | **Etapa 6** | Destaca a configuração do IDS Snort no laboratório e as regras aplicadas. Mostra a detecção bem-sucedida de ataques de força bruta, injeção SQL e *DNS tunneling*. **Visual**: Repositório. |
| **6:20 - 7:20** | **Miguel** | **Etapa 7** | Resume a esteira de DevSecOps, explicando em que etapas cada análise se encaixa e quais são as condições rígidas de parada (*Quality Gates*) para o deploy. **Visual**: Repositório. |
| **7:20 - 8:00** | **Todos** | **Conclusão** | Reflexões e aprendizados ao longo do semestre: a mudança de mentalidade entre prevenir vulnerabilidades (*shift-left*) e detectar intrusões ativas. **Visual**: Repositório. |



### 3.1 Pontos que devem aparecer no vídeo

- sistema escolhido: `Yummers`;
- principais ameaças e casos de abuso;
- riscos prioritários;
- decisões de arquitetura;
- práticas de código seguro da Etapa 4;
- principais resultados da verificação;
- regras de detecção e resposta;
- pipeline DevSecOps proposto;
- aprendizados do grupo.

### 3.2 Observação sobre participação

Todos os integrantes devem aparecer ou narrar uma parte do vídeo. A divisão proposta ajuda a evidenciar participação individual, mas a avaliação também poderá considerar os commits e contribuições feitas nas etapas do repositório.

## 4. Critérios de avaliação atendidos

| Critério | Como foi contemplado |
| :--- | :--- |
| **Integração entre as etapas** | O pipeline referencia ameaças, riscos, decisões, código seguro, testes, verificação e operação. |
| **Compreensão de DevSecOps** | A segurança acompanha todo o ciclo: planejamento, código, verificação, deploy e operação. |
| **Coerência do pipeline** | Cada momento possui atividade, evidência e condição para continuar. |
| **Qualidade das condições de segurança** | Há gates objetivos para testes falhos, controle de acesso, segredos, dependências vulneráveis e achados críticos. |
| **Clareza e objetividade do vídeo** | O roteiro divide o vídeo em blocos curtos, com tempo, responsável, fala e visual. |
| **Capacidade de apresentar decisões e aprendizados** | O roteiro conecta riscos a decisões e finaliza com aprendizados individuais. |
| **Participação individual** | A divisão por responsável facilita a participação dos quatro integrantes. |

---
<center>
<table width="100%">
<tr>
<td align="left">

[⬅️ Página anterior](etapa-6-deteccao-de-intrusoes.md)

</td>

<td align="center">

1️⃣2️⃣

</td>

<td align="right">

Próxima página ➡️

</td>
</tr>
</table>
</center>

### **Índice**:

**Etapa 1**:

1. [**🆔 Identificação do sistema**](../README.md)
2. [**📝 Descrição do sistema**](../README.md)
3. [**👥 Usuários, ativos e pontos de interação**](../docs/etapa-1/3%20-%20Usuários,%20ativos%20e%20pontos%20de%20interação.md)
4. [**🔀 Visão geral da arquitetura e fluxos de uso**](../docs/etapa-1/4%20-%20Visão%20geral%20da%20arquitetura%20e%20fluxos%20de%20uso.md) 
5. [**🎯 Modelagem de ameaças com STRIDE**](../docs/etapa-1/5%20-%20Modelagem%20de%20ameaças%20com%20STRIDE.md)
6. [**🚨 Casos de abuso**](../docs/etapa-1/6%20-%20Casos%20de%20abuso.md)
7. [**📌 Considerações finais da Etapa 1**](../docs/etapa-1/7%20-%20Considerações%20finais%20da%20Etapa%201.md)


**Etapa 2**:

8. [**🛡️ Análise e priorização dos riscos**](../docs/etapa-2/8%20-%20Análise%20e%20priorização%20dos%20riscos.md)
9. [**🧩 Tratamento dos riscos com NIST CSF**](../docs/etapa-2/#9-tratamento-dos-riscos-com-nist-csf)


**Etapa 3**:

10. [**🏗️ Arquitetura segura**](../docs/etapa-3/10%20-%20Arquitetura%20segura.md)


**Etapa 4**:

11. [**💻 Código seguro e testes de segurança**](../docs/etapa-4/11%20-%20Código%20seguro%20e%20testes%20de%20segurança.md)


**Etapa 5**:

12. [**🔎 Verificação de vulnerabilidades**](../docs/etapa-5/12%20-%20Verificação%20de%20vulnerabilidades.md)


**Etapa 6**:

13. [**📡 Monitoramento e detecção de intrusões**](etapa-6-deteccao-de-intrusoes.md)


**Etapa 7**:

14. [**🎥 DevSecOps e vídeo final**](#) 👈

---