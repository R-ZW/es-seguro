# Etapa 6 — Monitoramento e Detecção de Intrusões

> **Documento** Reúne, em ordem explicativa, todo o conteúdo da
> Etapa 6: o roteiro conceitual exigido pelo enunciado (seções 1 a 5), a resposta a
> incidentes (seção 5) e — como diferencial — a **validação prática com um IDS real**,
> incluindo as regras, a configuração, o **setup completo do ambiente** e os **logs
> verdadeiros** capturados (seções 6 e 7 e anexos A–E).

## Sumário

1. [O que é detecção de intrusões](#1-o-que-é-detecção-de-intrusões)
2. [A diferença entre prevenir e detectar](#2-a-diferença-entre-prevenir-e-detectar)
3. [Quais eventos do sistema deveriam ser registrados](#3-quais-eventos-do-sistema-deveriam-ser-registrados)
4. [Três regras simples de detecção](#4-três-regras-simples-de-detecção)
5. [O que deveria acontecer depois de um alerta](#5-o-que-deveria-acontecer-depois-de-um-alerta)
6. [Validação prática — execução real do IDS](#6-validação-prática--execução-real-do-ids)
7. [Evidências — logs reais por ataque](#7-evidências--logs-reais-por-ataque)
8. [Anexos (regras, configuração, setup completo e log de auditoria)](#anexos)

---

## 1. O que é detecção de intrusões

**Detecção de intrusões** é a prática de **observar o sistema em operação e identificar
sinais de que algo indevido está acontecendo** — um acesso não autorizado, um abuso de
funcionalidade ou uma tentativa de ataque. Um **IDS** (*Intrusion Detection System*)
coleta evidências (logs, tráfego de rede, eventos da aplicação), compara esses dados com
**padrões de comportamento suspeito** e, quando há correspondência, **gera um alerta**
para a equipe responsável.

A ideia central é: **não basta tentar impedir ataques; é preciso enxergar quando um ataque
está ocorrendo (ou já ocorreu)** para reagir a tempo. O IDS funciona como um "alarme" que
registra e sinaliza atividades anômalas, deixando um rastro que permite investigar o que
aconteceu. Neste projeto usamos o **Snort** como IDS baseado em **assinaturas** (regras):
ele inspeciona o tráfego de rede e dispara alertas quando o conteúdo casa com uma regra.

## 2. A diferença entre prevenir e detectar

São camadas **complementares** de segurança, com papéis diferentes:

| Aspecto | Prevenir (prevenção) | Detectar (detecção) |
|---|---|---|
| **Objetivo** | Impedir que o ataque aconteça | Perceber que o ataque está acontecendo ou aconteceu |
| **Postura** | Barreira / bloqueio | Observação / alerta |
| **Exemplos** | Firewall, senha forte, validação de entrada, controle de acesso, atualização de software (IPS) | IDS (Snort), análise de logs, alertas de comportamento anômalo |
| **Quando age** | *Antes* do incidente | *Durante* ou *depois* do incidente |
| **Limitação** | Nem todo ataque é previsível; sempre resta risco residual | Não bloqueia sozinho; depende de uma resposta (humana ou automática) |

Em resumo: **prevenir** é trancar a porta; **detectar** é ter uma câmera e um alarme para
o caso de alguém tentar arrombá-la. A prevenção reduz a probabilidade de sucesso do ataque,
mas nenhuma prevenção é perfeita — por isso a detecção existe para cobrir o que passou pela
primeira camada e permitir uma reação informada.

## 3. Quais eventos do sistema deveriam ser registrados

Para detectar intrusões relacionadas aos **riscos deste projeto** (aplicação web com banco
de dados, acesso remoto por SSH e serviços de rede), os seguintes eventos devem ser
registrados. A coluna à direita mostra **quantas ocorrências reais foram capturadas** na
execução documentada nas seções 6 e 7:

| Evento a registrar | Por quê | Ocorrências reais capturadas |
|---|---|---|
| Tentativas de autenticação SSH (porta 22) | Detectar força bruta / uso indevido de conta | 25 conexões → 20 alertas de *brute force* |
| Requisições HTTP: método, URI e cabeçalhos (porta 80) | Detectar injeção e volume anormal | 31 GET + 12 POST registrados |
| Consultas/erros de banco via URI HTTP | Detectar SQL Injection | 6 alertas de SQLi (UNION, OR 1=1, `--`, `'`) |
| Pacotes ICMP *echo request* (tipo 8) | Detectar *ping flood* | 100 pings → 50 alertas de flood |
| Consultas DNS (porta 53): volume e tamanho | Detectar tunelamento/exfiltração | 61 queries → 11 alertas de alto volume + 1 pacote gigante |

Cada registro deve conter sempre **quem** (IP de origem), **o quê** (ação/evento),
**quando** (*timestamp*) e **onde** (serviço/porta). Esses são exatamente os campos
presentes em cada linha de alerta do Snort mostrada na seção 7.

## 4. Três regras simples de detecção

As três regras a seguir cobrem riscos distintos do projeto (uso indevido de conta,
integridade do banco e exfiltração de dados). Cada uma é apresentada no formato exigido
pelo enunciado e **comprovada pelo alerta real** que ela gerou (ver seção 7).

### Regra 1 — Força bruta / uso indevido de conta

| Campo | Descrição |
|---|---|
| **Risco observado** | Comprometimento de credenciais por tentativa e erro (força bruta em SSH ou no login web) |
| **Fonte de dados** | Logs de autenticação e tráfego TCP na porta 22 |
| **Condição de alerta** | Muitas tentativas de conexão a partir da **mesma origem** em curto intervalo (≥ 10 tentativas em 60 s) |
| **Resposta inicial** | Alertar a equipe e **limitar temporariamente** novas tentativas do IP de origem (*rate limit*/bloqueio); revisar a conta-alvo |

Regra Snort correspondente (`sid:1000005`), comprovação na seção 7.1.

### Regra 2 — Injeção de SQL (SQL Injection)

| Campo | Descrição |
|---|---|
| **Risco observado** | Acesso ou manipulação não autorizada do banco de dados através da aplicação web |
| **Fonte de dados** | Logs de requisições HTTP (URI e parâmetros) e tráfego TCP na porta 80 |
| **Condição de alerta** | Requisição contendo padrões típicos de SQLi — `UNION SELECT`, `OR 1=1`, comentário `--` ou aspas simples (`'`) em parâmetros |
| **Resposta inicial** | Registrar origem e carga, **bloquear o IP**, reforçar a validação de entrada da aplicação e verificar a integridade do banco |

Regras Snort correspondentes (`sid:1000009`, `1000010`, `1000012`, `1000013`), comprovação na seção 7.2.

### Regra 3 — Exfiltração via DNS Tunneling

| Campo | Descrição |
|---|---|
| **Risco observado** | Vazamento de dados ou canal encoberto de comando e controle (C2) usando o protocolo DNS |
| **Fonte de dados** | Tráfego UDP na porta 53 (consultas DNS) |
| **Condição de alerta** | Volume anormal de *queries* da mesma origem (≥ 50 em 10 s) e/ou pacotes DNS grandes demais (`dsize` > 200 bytes) |
| **Resposta inicial** | Alertar a equipe, **isolar o host** de origem da rede, inspecionar o tráfego e investigar possível comprometimento |

Regras Snort correspondentes (`sid:1000014`, `sid:1000016`), comprovação na seção 7.3.

## 5. O que deveria acontecer depois de um alerta

Um alerta não é o fim do processo — é o início da **resposta**. O fluxo recomendado é:

1. **Triagem** — confirmar se o alerta é real ou falso positivo, olhando os logs que o
   originaram (origem, horário, evento).
2. **Priorização** — classificar a gravidade conforme o risco (SQL Injection e exfiltração
   de dados têm prioridade sobre um *ping* isolado). O próprio Snort já atribui prioridade:
   o alerta de DNS Tunneling saiu com `[Priority: 1]` (ver seção 7.3).
3. **Contenção** — aplicar a *resposta inicial* da regra correspondente (bloquear/limitar
   o IP, isolar o host, restringir a conta afetada) para interromper o ataque em andamento.
4. **Investigação** — analisar o alcance: o que foi acessado, se houve sucesso e se outros
   hosts foram afetados.
5. **Escalonamento e comunicação** — notificar os responsáveis quando o incidente exceder a
   resposta automática.
6. **Registro e aprendizado** — documentar o incidente, **ajustar as regras** (reduzir
   falsos positivos, criar novas) e **reforçar a prevenção** (corrigir a falha explorada).
   A detecção realimenta a prevenção.

Princípio geral: **detectar → conter → investigar → aprender**, sempre deixando registro
para auditoria.

---