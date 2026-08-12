### Anexo C — Como reproduzir

```bash
# 1. Instalar o Snort
sudo apt-get install -y snort

# 2. Aplicar as regras (Anexo A) e a configuração (Anexo B)
sudo nano /etc/snort/rules/local.rules      # cole o Anexo A
sudo nano /etc/snort/snort_test.conf        # cole o Anexo B

# 3. Iniciar o Snort capturando ao vivo na interface de loopback
sudo snort -A fast -k none -i lo -c /etc/snort/snort_test.conf -l /var/log/snort_test

# 4. Em outro terminal, disparar os ataques (ex.: SQLi via curl) e acompanhar os alertas
curl "http://127.0.0.1/item.php?id=1'"
sudo tail -f /var/log/snort_test/alert
```

Mapeamento entre as três regras conceituais (Seção 4) e as regras Snort:
- Regra 1 → `1000005`/`1000006`; 
- Regra 2 → `1000009`–`1000013`; 
- Regra 3 → `1000014`/`1000016`.

- **Vídeo com a demonstração dos ataques e logs:** <https://www.youtube.com/watch?v=BxocdiYo8wY>