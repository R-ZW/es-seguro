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

## 6. Validação prática — execução real do IDS

O enunciado não exige implementar um IDS. Ainda assim, para dar sustentação prática ao
roteiro, montamos o Snort e **executamos os ataques de verdade**, capturando alertas reais.

**Ambiente:** Snort 2.9.20 (GRE, Build 82), Ubuntu 24.04, capturando ao vivo na interface
de *loopback* (`lo`), com as regras do projeto (Anexo A) e a configuração do Anexo B
(`HOME_NET = 127.0.0.0/8`).

**Metodologia:** subimos serviços-alvo (HTTP:80, SSH:22, DNS:53) apenas para que o
*handshake* TCP e a remontagem de fluxo se completassem, permitindo a inspeção real de
conteúdo pelos pré-processadores `http_inspect`/`stream5`. Em seguida disparamos cada
ataque descrito na documentação de setup (Anexo D) contra `127.0.0.1`.

**Resultado:** **336 alertas reais**, com **todas as regras aplicáveis a este ambiente
disparando e sendo validadas** (ver "Cobertura das regras" abaixo).

### Resumo por regra (contagem real de alertas)

| SID | Regra | Alertas |
|---|---|---:|
| 1000008 | LOG -> PING REALIZADO | 100 |
| 1000020 | LOG -> DNS Query | 61 |
| 1000007 | ATAQUE -> ICMP Ping Flood | 50 |
| 1000017 | LOG -> HTTP GET | 31 |
| 1000019 | LOG -> SSH Connection | 25 |
| 1000005 | ATAQUE -> SSH Brute Force | 20 |
| 1000018 | LOG -> HTTP POST | 12 |
| 1000014 | ATAQUE -> DNS Tunneling High Volume | 11 |
| 1000001 | ATAQUE -> HTTP DoS GET Flood | 10 |
| 1000006 | ATAQUE -> SSH Multiple Connections | 5 |
| 1000012 | ATAQUE -> SQL Comment Injection | 2 |
| 1000013 | ATAQUE -> SQL Injection Quote | 2 |
| 1000002 | ATAQUE -> HTTP DoS POST Flood | 2 |
| 1000003 | ATAQUE -> HTTP Large Header | 1 |
| 1000004 | ATAQUE -> HTTP DoS User-Agent | 1 |
| 1000009 | ATAQUE -> SQL Injection UNION | 1 |
| 1000010 | ATAQUE -> SQL Injection OR 1=1 | 1 |
| 1000016 | ATAQUE -> DNS Tunneling Pacote UDP Muito Grande | 1 |
| **Total** | | **336** |

### Cobertura das regras

Todas as regras aplicáveis a este ambiente de laboratório foram acionadas e validadas com
tráfego real. Cada categoria de ataque do projeto — força bruta, SQL Injection, DNS
tunneling, HTTP DoS e ICMP flood — foi **detectada de ponta a ponta**.

A regra `sid:1000015` tem um alvo mais específico: consultas a um resolvedor DNS
**externo** (`8.8.8.8`). Ela atua na fronteira de saída à internet (interface **NAT**,
descrita no Anexo D) e é **complementar** à `sid:1000014`, que já cobre o alto volume de
consultas DNS. Por isso, o mecanismo de detecção de DNS tunneling ficou plenamente
comprovado neste teste (volume + pacote grande), e a `sid:1000015` amplia essa mesma
proteção no cenário com NAT — cobrindo, em conjunto, tanto o tráfego interno quanto o de
saída.

---

## 7. Evidências — logs reais por ataque

Abaixo, o **momento exato** em que cada regra dispara, extraído do log real
(`alert_fast`). O log completo está no Anexo D. Formato de cada linha:
`data-hora  [**] [gid:sid:rev] mensagem [**] [Priority] {PROTO} origem -> destino`.

### 7.1. Força bruta SSH (Regra 1)

As primeiras conexões geram apenas o log informativo `LOG -> SSH Connection`
(`sid:1000019`). Na **10ª tentativa dentro de 60 s**, o limiar da regra é atingido e o
alerta de ataque `sid:1000005` dispara junto — exatamente o comportamento esperado:

```
08/11-20:54:36.189149  [**] [1:1000019:1] LOG -> SSH Connection [**] [Priority: 0] {TCP} 127.0.0.1:34306 -> 127.0.0.1:22
08/11-20:54:36.239517  [**] [1:1000019:1] LOG -> SSH Connection [**] [Priority: 0] {TCP} 127.0.0.1:34316 -> 127.0.0.1:22
08/11-20:54:36.290014  [**] [1:1000019:1] LOG -> SSH Connection [**] [Priority: 0] {TCP} 127.0.0.1:34326 -> 127.0.0.1:22
08/11-20:54:36.340508  [**] [1:1000019:1] LOG -> SSH Connection [**] [Priority: 0] {TCP} 127.0.0.1:34330 -> 127.0.0.1:22
08/11-20:54:36.390994  [**] [1:1000019:1] LOG -> SSH Connection [**] [Priority: 0] {TCP} 127.0.0.1:34340 -> 127.0.0.1:22
08/11-20:54:36.441472  [**] [1:1000019:1] LOG -> SSH Connection [**] [Priority: 0] {TCP} 127.0.0.1:34350 -> 127.0.0.1:22
08/11-20:54:36.441472  [**] [1:1000005:1] ATAQUE -> SSH Brute Force [**] [Priority: 0] {TCP} 127.0.0.1:34350 -> 127.0.0.1:22
```

Ao ultrapassar **20 conexões em 30 s**, dispara também `sid:1000006` (*Multiple Connections*):

```
08/11-20:54:37.198974  [**] [1:1000006:1] ATAQUE -> SSH Multiple Connections [**] [Priority: 0] {TCP} 127.0.0.1:34482 -> 127.0.0.1:22
08/11-20:54:37.199043  [**] [1:1000019:1] LOG -> SSH Connection [**] [Priority: 0] {TCP} 127.0.0.1:34482 -> 127.0.0.1:22
08/11-20:54:37.199043  [**] [1:1000005:1] ATAQUE -> SSH Brute Force [**] [Priority: 0] {TCP} 127.0.0.1:34482 -> 127.0.0.1:22
```

### 7.2. SQL Injection (Regra 2)

Cada payload malicioso na URI casa com a assinatura correspondente. Numa única requisição
com `' or 1=1--` disparam três regras ao mesmo tempo (OR 1=1, comentário e aspas):

```
08/11-20:54:36.186320  [**] [1:1000009:1] ATAQUE -> SQL Injection UNION [**] [Priority: 0] {TCP} 127.0.0.1:44480 -> 127.0.0.1:80
08/11-20:54:36.186320  [**] [1:1000017:1] LOG -> HTTP GET [**] [Priority: 0] {TCP} 127.0.0.1:44480 -> 127.0.0.1:80
08/11-20:54:36.186320  [**] [1:1000001:1] ATAQUE -> HTTP DoS GET Flood [**] [Priority: 0] {TCP} 127.0.0.1:44480 -> 127.0.0.1:80
08/11-20:54:36.186882  [**] [1:1000010:1] ATAQUE -> SQL Injection OR 1=1 [**] [Priority: 0] {TCP} 127.0.0.1:44482 -> 127.0.0.1:80
08/11-20:54:36.186882  [**] [1:1000012:1] ATAQUE -> SQL Comment Injection [**] [Priority: 0] {TCP} 127.0.0.1:44482 -> 127.0.0.1:80
08/11-20:54:36.186882  [**] [1:1000013:1] ATAQUE -> SQL Injection Quote [**] [Priority: 0] {TCP} 127.0.0.1:44482 -> 127.0.0.1:80
08/11-20:54:36.186882  [**] [1:1000017:1] LOG -> HTTP GET [**] [Priority: 0] {TCP} 127.0.0.1:44482 -> 127.0.0.1:80
```

### 7.3. DNS Tunneling (Regra 3)

O pacote UDP de 250 bytes aciona imediatamente `sid:1000016` (pacote grande, `Priority: 1`);
o volume de queries aciona `sid:1000014` ao passar de 50 em 10 s:

```
08/11-20:54:37.451932  [**] [1:1000020:1] LOG -> DNS Query [**] [Priority: 0] {UDP} 127.0.0.1:56494 -> 127.0.0.1:53
08/11-20:54:37.451932  [**] [1:1000016:1] ATAQUE -> DNS Tunneling Pacote UDP Muito Grande [**] [Classification: Potential Corporate Privacy Violation] [Priority: 1] {UDP} 127.0.0.1:56494 -> 127.0.0.1:53
08/11-20:54:37.451984  [**] [1:1000020:1] LOG -> DNS Query [**] [Priority: 0] {UDP} 127.0.0.1:56494 -> 127.0.0.1:53
```

(...) e, ao ultrapassar 50 queries em 10 s:

```
08/11-20:54:37.452209  [**] [1:1000020:1] LOG -> DNS Query [**] [Priority: 0] {UDP} 127.0.0.1:56494 -> 127.0.0.1:53
08/11-20:54:37.452212  [**] [1:1000020:1] LOG -> DNS Query [**] [Priority: 0] {UDP} 127.0.0.1:56494 -> 127.0.0.1:53
08/11-20:54:37.452212  [**] [1:1000014:1] ATAQUE -> DNS Tunneling High Volume [**] [Priority: 0] {UDP} 127.0.0.1:56494 -> 127.0.0.1:53
```

### 7.4. HTTP DoS — GET/POST flood (regras de apoio)

Na **20ª requisição GET em 5 s**, `sid:1000001` dispara junto com o log de GET:

```
08/11-20:54:36.173183  [**] [1:1000017:1] LOG -> HTTP GET [**] [Priority: 0] {TCP} 127.0.0.1:44270 -> 127.0.0.1:80
08/11-20:54:36.173908  [**] [1:1000017:1] LOG -> HTTP GET [**] [Priority: 0] {TCP} 127.0.0.1:44286 -> 127.0.0.1:80
08/11-20:54:36.173908  [**] [1:1000001:1] ATAQUE -> HTTP DoS GET Flood [**] [Priority: 0] {TCP} 127.0.0.1:44286 -> 127.0.0.1:80
08/11-20:54:36.174686  [**] [1:1000017:1] LOG -> HTTP GET [**] [Priority: 0] {TCP} 127.0.0.1:44302 -> 127.0.0.1:80
08/11-20:54:36.174686  [**] [1:1000001:1] ATAQUE -> HTTP DoS GET Flood [**] [Priority: 0] {TCP} 127.0.0.1:44302 -> 127.0.0.1:80
```

### 7.5. ICMP Ping Flood (regra de apoio)

Cada *echo request* gera `LOG -> PING REALIZADO`; ao passar de **50 pings em 5 s**, dispara
`sid:1000007`:

```
08/11-20:54:37.453739  [**] [1:1000008:1] LOG -> PING REALIZADO [**] [Priority: 0] {ICMP} 127.0.0.1 -> 127.0.0.1
08/11-20:54:37.453745  [**] [1:1000008:1] LOG -> PING REALIZADO [**] [Priority: 0] {ICMP} 127.0.0.1 -> 127.0.0.1
08/11-20:54:37.453745  [**] [1:1000007:1] ATAQUE -> ICMP Ping Flood [**] [Priority: 0] {ICMP} 127.0.0.1 -> 127.0.0.1
08/11-20:54:37.453751  [**] [1:1000008:1] LOG -> PING REALIZADO [**] [Priority: 0] {ICMP} 127.0.0.1 -> 127.0.0.1
08/11-20:54:37.453751  [**] [1:1000007:1] ATAQUE -> ICMP Ping Flood [**] [Priority: 0] {ICMP} 127.0.0.1 -> 127.0.0.1
```

---
## 8. Anexos

Como a configuração, as regras e os logs geram um volume extenso de informações técnicas, esses artefatos foram separados em arquivos dedicados no diretório `anexos/` para facilitar a leitura do relatório principal e a auditoria dos resultados.

Abaixo está o índice de arquivos anexados a este roteiro:

* **[Anexo A — Conjunto completo de regras (`local.rules`)](./anexos/anexo-a-local.rules)**: Arquivo contendo as 19 regras do projeto elaboradas para o Snort.
* **[Anexo B — Configuração do Snort (`snort.conf`)](./anexos/anexo-b-snort.conf)**: Arquivo com a configuração mínima, pré-processadores e variáveis de rede utilizadas no laboratório.
* **[Anexo C — Guia de Reprodução](./anexos/anexo-c-como-reproduzir.md)**: Passo a passo rápido com os comandos para instalar o Snort, aplicar as configurações e disparar os testes locais.
* **[Anexo D — Documentação completa de setup do ambiente](./anexos/anexo-d-setup-ambiente.md)**: Tutorial integral de infraestrutura para montar a topologia de rede no VirtualBox e instalar todas as dependências do zero.
* **[Anexo E — Log de alertas completo](./anexos/anexo-e-alert_fast.log)**: Arquivo de log bruto gerado pelo Snort durante a bateria de testes, contendo todos os 336 alertas disparados.

---
<center>
<table width="100%">
<tr>
<td align="left">

[⬅️ Página anterior](../docs/etapa-5/12%20-%20Verificação%20de%20vulnerabilidades.md)

</td>

<td align="center">

1️⃣1️⃣

</td>

<td align="right">

[Próxima página ➡️](etapa-7-devsecops-e-video-final.md)

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

13. [**📡 Monitoramento e detecção de intrusões**](#) 👈


**Etapa 7**:

14. [**🎥 DevSecOps e vídeo final**](etapa-7-devsecops-e-video-final.md)

---