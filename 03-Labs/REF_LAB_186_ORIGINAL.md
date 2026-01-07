# Referência: Lab 186 Original (Monitoramento)

> **Nota:** Este é o resumo dos passos originais do laboratório previsto na grade, para fins de comparação.

## Cenario
Você é um Sysadmin precisando monitorar um servidor Web instável.

## Objetivos
1.  Criar Role IAM para EC2 e CloudWatch.
2.  Lançar instância EC2 e instalar Servidor Web (Apache).
3.  Instalar e configurar o CloudWatch Agent.
4.  Gerar carga de estresse para disparar alarmes.

---

## Passos Originais

### Tarefa 1: Criar Role IAM
*   Criar Role: `CloudWatchAgentRole`.
*   Policy: `CloudWatchAgentServerPolicy`.

### Tarefa 2: Lançar Instância
*   AMI: Amazon Linux 2.
*   Type: t2.micro.
*   User Data: Instalar httpd e stress tool.
*   Attach Role: `CloudWatchAgentRole`.

### Tarefa 3: Configurar Agente
*   Baixar o agente: `sudo yum install amazon-cloudwatch-agent`.
*   Baixar config: `wget [url]/config.json`.
*   Iniciar agente: `/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config ...`

### Tarefa 4: Criar Alarme
*   Métrica: `mem_used_percent` ou `CPUUtilization`.
*   Tópico SNS: `Topic-Lab`.
*   Threshold: > 60%.

### Tarefa 5: Teste
*   Rodar `stress --cpu 1`.
*   Verificar email.
