
### Anexo D — Documentação completa de setup do ambiente

Reprodução integral do laboratório, do zero até o Snort operante. Este anexo torna o
documento autossuficiente: com ele, qualquer avaliador consegue remontar o ambiente sem
depender de nenhum arquivo externo.

#### D.1. Pré-requisitos

**Ambiente de virtualização** — usado para hospedar o servidor IDS:

- Oracle VM VirtualBox — <https://www.virtualbox.org/wiki/Downloads>

**Sistema operacional** — distribuição Linux escolhida para hospedar o Snort, pela
estabilidade e facilidade de manipulação de pacotes de rede:

- Distribuição: **Ubuntu Server 24.04 LTS** — <https://ubuntu.com/download/server>
- Estado inicial: instalação limpa, com acesso de superusuário (root ou via `sudo`).

#### D.2. Topologia de rede

Para simular um ambiente realista de ataque e defesa, define-se uma topologia com **dois
adaptadores de rede** distintos na máquina virtual:

- **Interface 1 (NAT):** acesso à internet da VM (downloads, atualizações do sistema e das
  regras do Snort).
- **Interface 2 (Host-Only):** comunicação isolada entre o host (Windows) e o convidado
  (Ubuntu). É nesta rede privada (`192.168.56.x`) que ocorrem os testes de conectividade e
  a simulação de ataques, garantindo que o tráfego malicioso não saia para a rede externa.

**Configuração no VirtualBox (VM desligada → Configurações → Rede):**

1. **Adaptador 1:** habilitado, *Attached to:* **NAT**.
2. **Adaptador 2:** habilitado, *Attached to:* **Placa de Rede Exclusiva de Hospedeiro
   (Host-only Adapter)**; *Nome:* `VirtualBox Host-Only Ethernet Adapter` (ou `vboxnet0`).

> Credenciais padrão da VM de laboratório: usuário `vboxuser`, senha `changeme` (ambiente
> descartável e isolado; troque em qualquer uso fora do laboratório).

**Identificação das interfaces no Ubuntu** (`ip a` / `ip route`):

- `enp0s3` → NAT
- `enp0s8` → comunicação Windows ↔ VirtualBox (Host-Only)

**Configuração de IP estático (Netplan)** — garante reprodutibilidade dos testes. Edite
`/etc/netplan/01-netcfg.yaml` (substitua `enp0s8` pela sua interface; YAML é sensível à
indentação):

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s8:
      dhcp4: no
      addresses:
        - 192.168.56.101/24
      gateway4: 192.168.56.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 1.1.1.1
```

Aplique e confirme:

```bash
sudo netplan apply
ip a                         # verificar se 192.168.56.101 foi atribuído
```

**Validação da conectividade:**

```bash
# Do Windows para a VM (cmd/PowerShell):
ping 192.168.56.101
# Da VM (Ubuntu) para o Windows:
ping -c 4 192.168.56.1
# Se falhar, desative temporariamente o Firewall do Windows:
#   netsh advfirewall set allprofiles state off
```

#### D.3. Setup do Snort

**Acesso remoto por SSH (opcional, recomendado)** — facilita administrar o servidor e
colar as regras:

```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable --now ssh
# No host: ssh seu_usuario@192.168.56.101
```

**Preparação do ambiente e dependências:**

```bash
# Atualização do sistema
sudo apt update && sudo apt upgrade -y

# Ferramentas de compilação e bibliotecas de rede
sudo apt install -y build-essential cmake libpcap-dev libpcre3-dev \
  libdumbnet-dev bison flex zlib1g-dev liblzma-dev

# Ambiente web (Apache, MySQL, PHP) para os testes de aplicação
sudo apt install -y apache2 php php-mysqli php-curl libapache2-mod-php \
  mysql-server git unzip
```

**Instalação do Snort** (versão 2.9.x via `apt`, pela estabilidade):

```bash
sudo apt install -y snort
# Durante a instalação, informe o HOME_NET (CIDR da rede Host-Only): 192.168.56.0/24
snort --version   # deve exibir o porco em ASCII e a versão 2.9.x
```

**Configuração principal (`/etc/snort/snort.conf`):**

```bash
sudo cp /etc/snort/snort.conf /etc/snort/snort.conf.backup   # backup (boa prática)
sudo nano /etc/snort/snort.conf
```

Ajuste as variáveis de rede e o caminho das regras:

```conf
# Rede a proteger (sub-rede Host-Only)
ipvar HOME_NET 192.168.56.0/24
# Tudo que não for a rede interna é externo
ipvar EXTERNAL_NET !$HOME_NET
# Garantir a inclusão das regras locais
include $RULE_PATH/local.rules
```

Configure a saída de alertas (um formato legível para testes e o binário para análise):

```conf
# Alerta simples em texto (fácil de ler com 'cat' ou 'tail')
output alert_fast: alert_fast.log
# Log binário padrão (opcional)
output unified2: filename snort.u2, limit 128
```

**Criação do arquivo de regras locais:**

```bash
sudo touch /etc/snort/rules/local.rules
sudo chown root:root /etc/snort/rules/local.rules
sudo chmod 644 /etc/snort/rules/local.rules
# Cole o conteúdo do Anexo A (as 19 regras do projeto) neste arquivo.
```

Caminhos importantes:

| Caminho | Função |
|---|---|
| `/etc/snort/rules/local.rules` | Regras proprietárias do projeto (Anexo A) |
| `/etc/snort/snort.conf` | Configuração do Snort |
| `/var/log/snort/alert_fast.log` | Logs de alertas |

> Sempre que alterar regras/configuração, reinicie o serviço: `sudo systemctl restart snort`.

#### D.4. Execução dos ataques (variações sem Docker)

Comandos para disparar cada ataque a partir do host, contra a VM (`192.168.56.101`):

```bash
# SQL Injection — na aplicação DVWA:
#   http://192.168.56.101/dvwa/vulnerabilities/sqli/  → submeter:  1' or '1'='1

# DNS Tunneling (PowerShell no Windows) — pacote UDP grande para a porta 53:
powershell -Command "$u=New-Object System.Net.Sockets.UdpClient; \
  $u.Connect('192.168.56.101',53); \
  $b=[Text.Encoding]::ASCII.GetBytes('A'*250); \
  $u.Send($b,$b.Length); $u.Close(); Write-Host 'Pacote UDP Gigante Enviado!'"

# Ping Flood (cmd do Windows):
FOR /L %i IN (1,1,100) DO ping -n 1 -w 1 192.168.56.101

# Brute Force (DVWA) — variando a senha em cada requisição:
FOR /L %i IN (1,1,20) DO curl "http://192.168.56.101/dvwa/vulnerabilities/brute/?username=admin&password=%i&Login=Login" -H "Cookie: PHPSESSID=<COOKIE>; security=low" -s -o NUL
```

> No ambiente isolado deste documento (Anexo C), os mesmos ataques foram reproduzidos
> contra `127.0.0.1` para capturar os logs reais das seções 6 e 7.
