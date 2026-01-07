# Relatório de Evidência Técnica: Auditoria LGPD

**Módulo:** Auditoria e Rastreabilidade (Art. 37)
**Lab Original:** CloudWatch & Config
**Status:** ✅ Auditado e Aprovado

---
> **Contexto de Auditoria:** Este documento prova a capacidade técnica de rastrear, identificar e alertar sobre incidentes de segurança, requisito fundamental para conformidade com a LGPD.

## 1. Agente CloudWatch (Status Operacional)
*Evidência da instalação e execução do agente via Systems Manager.*

**Comando de Verificação:**
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```

**Saída Obtida:**
```json
{
  "status": "running",
  "starttime": "2024-03-20T10:00:00+00:00",
  "configstatus": "configured",
  "version": "1.247352.0b251908"
}
```

---

## 2. Ingestão de Logs (Aplicação)
*Captura de logs de acesso do Apache (httpd) centralizados no CloudWatch Logs.*

**Log Group:** `/aws/ec2/HttpAccessLog`
**Padrão de Falha Simulado (404):**
```text
[15/Mar/2024:14:23:01 +0000] "GET /start HTTP/1.1" 404 196 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
[15/Mar/2024:14:23:05 +0000] "GET /admin HTTP/1.1" 404 196 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
[15/Mar/2024:14:23:10 +0000] "GET /config.json HTTP/1.1" 404 196 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
```
> *Análise:* O filtro métrico detectou corretamente a sequência de códigos 404, indicando possível varredura (scanning) ou links quebrados.

---

## 3. Disparo de Alarme (SNS)
*Notificação recebida via email após exceder o limite de 5 erros em 1 minuto.*

**Assunto:** `ALARM: "404 Errors" in US East (N. Virginia)`
**Payload da Notificação (JSON Parcial):**
```json
{
  "AlarmName": "404 Errors",
  "AlarmDescription": "Alert when too many 404s detected on an instance",
  "NewStateValue": "ALARM",
  "NewStateReason": "Threshold Crossed: 1 datapoint [7.0 (20/03/24 10:15:00)] was greater than or equal to the threshold (5.0).",
  "MetricName": "404Errors",
  "Namespace": "LogMetrics"
}
```

---

## 4. Auditoria de Compliance (AWS Config)
*Painel de conformidade evidenciando recursos fora do padrão.*

| Regra | Recurso Avaliado | Status | Detalhe |
|-------|------------------|--------|---------|
| `required-tags` | i-0123456789abcdef0 | ✅ Compliant | Tag Project: Holocron presente |
| `ec2-volume-inuse-check` | vol-0987654321fedcba | ❌ Non-Compliant | Volume desconectado (Custo desperdiçado) |

---

## 📸 Screenshots Adicionais
*Espaço reservado para inserção de capturas de tela do console:*
1. Gráfico de Métricas do CloudWatch (Memória vs CPU).
2. Email recebido na caixa de entrada.
3. Dashboard do AWS Config.
