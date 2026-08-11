## 1. Objetivo
Esta etapa utilizou uma ferramenta de teste de segurança para observar vulnerabilidades, alertas e configurações inseguras. A verificação foi realizada exclusivamente sobre uma aplicação deliberadamente vulnerável executada para fins educacionais (OWASP Juice Shop), executada localmente pelo próprio grupo, não envolvendo nenhum sistema de terceiros.

## 2. Ambiente e ferramenta utilizados
* **Sistema/ambiente testado:** OWASP Juice Shop, disponibilizado localmente em `http://localhost:3000`
* **Ferramenta utilizada:** OWASP ZAP (Zed Attack Proxy) by Checkmarx, versão 2.17.0
* **Configuração básica do teste:** verificação automatizada (baseline/full scan) direcionada ao host `http://localhost:3000`, com todos os níveis de risco (Alto, Médio, Baixo, Informativo) e de confiança incluídos no relatório, sem exclusão de contextos
* **Evidência da execução:** relatório HTML completo gerado pelo ZAP, armazenado em `evidencias/etapa-5/ (2026-08-13-ZAP-Report-.html)`, contendo requisições, respostas e capturas de cada alerta. Além disso, em `evidencias/etapa-5/` também podem ser encontradas outras capturas de tela referentes aos testes realizados. 

### 2.1 Instruções para Reprodução do Ambiente (Como Rodar)
Para garantir a reprodutibilidade do teste, os seguintes passos foram executados:

1. **Pré-requisitos:**
   * [Docker](https://www.docker.com/) instalado e em execução no ambiente local.
   * [OWASP ZAP](https://www.zaproxy.org/download/) instalado na máquina.

2. **Execução do Alvo (OWASP Juice Shop):**
   No terminal, o contêiner Docker da aplicação foi iniciado mapeando a porta local 3000 para a porta 3000 do contêiner com o seguinte comando:
   ```bash
   docker run --rm -p 3000:3000 bkimminich/juice-shop
   ```
   Após a inicialização, o sistema alvo ficou acessível via navegador em `http://localhost:3000`.


## 3. Análise de Alertas e Achados

A sessão de verificação identificou 10 alertas distribuídos entre os níveis Alto (1), Médio (4), Baixo (3) e Informativo (2). A seguir são detalhados os três achados mais relevantes; os demais foram descartados por serem duplicados, de baixo impacto isolado ou meramente informativos, conforme justificado na tabela subsequente.

### 3.1 Análise dos três principais achados

| ID | Alerta ou achado | Evidência | Possível impacto | Relação com OWASP/CWE | Correção proposta |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A01** | Injeção SQL no endpoint de busca de produtos (parâmetro `q`) | **Requisição:** GET `/rest/products/search?q=%27%28`<br>**Resposta:** HTTP 500 com erro `SQLITE_ERROR: near "(": syntax error`, expondo a query SQL montada por concatenação<br>*(Captura salva em evidencias/etapa-5/)* | Um atacante pode manipular a cláusula WHERE da consulta para extrair, alterar ou apagar dados de outros usuários (produtos, pedidos, credenciais), comprometendo confidencialidade e integridade dos dados | OWASP Top 10 A03:2021 – Injection / CWE-89 (SQL Injection) | Substituir a concatenação de strings por consultas parametrizadas (prepared statements/ORM com bind de parâmetros); validar e tipar a entrada no servidor antes de usá-la na consulta |
| **A02** | Content Security Policy (CSP) Header Not Set | **Requisição:** GET `/`<br>**Resposta:** HTTP 200 sem o cabeçalho `Content-Security-Policy` | Facilita a exploração de XSS e ataques de injeção de conteúdo, pois o navegador não tem restrição sobre quais origens de script/estilo podem ser carregadas | OWASP Top 10 A05:2021 – Security Misconfiguration / CWE-693 (Protection Mechanism Failure) | Configurar o cabeçalho `Content-Security-Policy` no servidor/CDN, restringindo origens permitidas para `script-src`, `style-src`, `img-src` etc. |
| **A03** | Configuração incorreta de CORS (`Access-Control-Allow-Origin: *`) | **Requisição:** GET `/robots.txt`<br>**Resposta:** HTTP 200 com o cabeçalho `Access-Control-Allow-Origin: *` | Permite que páginas de domínios arbitrários façam requisições de leitura à API a partir do navegador da vítima, o que pode expor dados não autenticados ou facilitar ataques em conjunto com outras falhas | OWASP Top 10 A01:2021 – Broken Access Control / CWE-264 (Permissions, Privileges, and Access Controls) | Restringir `Access-Control-Allow-Origin` a uma lista de domínios confiáveis (ou remover o cabeçalho quando não houver necessidade de acesso cross-origin) |

### 3.2 Alertas descartados

| Alerta descartado | Classificação ZAP | Motivo do descarte |
| :--- | :--- | :--- |
| **Session ID in URL Rewrite** (parâmetro `sid` em requisições ao Socket.IO) | Risco Médio / Confiança Alta | Mesma causa-raiz de A02 (configuração incompleta de cabeçalhos/transporte); o `sid` é gerado pela própria lib Socket.IO e não é a sessão de autenticação da aplicação |
| **Missing Anti-clickjacking Header** | Risco Médio / Confiança Média | Duplicado: mesma causa-raiz de A02 (ausência de cabeçalhos de segurança); a correção de CSP com `frame-ancestors` também resolve este achado |
| **Private IP Disclosure / X-Content-Type-Options Header Missing** | Risco Baixo / Confiança Média | Baixo impacto isolado (IP interno de laboratório e cabeçalho de MIME-sniffing); tratados como enriquecimento dos achados de A02, não como itens autônomos |
| **Divulgação de Data e Hora - Unix** (timestamp em styles.css) | Risco Baixo / Confiança Baixa | Falso positivo provável: o timestamp está embutido em um arquivo CSS de terceiros (biblioteca de ícones), sem relação com dados sensíveis da aplicação |
| **Modern Web Application / User Agent Fuzzer** | Informativo | Alertas informativos do próprio ZAP (recomendação de uso do Ajax Spider e checagem de diferenças por User-Agent, sem diferença encontrada); não representam vulnerabilidade |