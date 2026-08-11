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