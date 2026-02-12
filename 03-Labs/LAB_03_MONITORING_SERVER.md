# HOLOCRON GUIDE: Módulo de Auditoria Técnica
**(Adaptação Avançada do Lab 186)**

Este documento substitui as instruções originais para transformar o laboratório em uma entrega de portfólio de alto nível.

---

## Fase 1: Infraestrutura Segura (Setup)

### 1. IAM Role (Identidade)
*   **Original:** Criar `CloudWatchAgentRole`.
*   **Adaptação Holocron:**
    *   Nome: `Holocron-Server-Role`.
    *   **Ação:** Adicione também a policy `AmazonSSMManagedInstanceCore` (para podermos auditar via Systems Manager sem abrir porta 22/SSH). Isso é "Security Best Practice".

### 2. EC2 Instance (O Servidor de Dados)
*   **Original:** Instância web comum.
*   **Adaptação Holocron:**
    *   **Tags Obrigatórias** (Para compliance com AWS Config):
        *   `Key: Project` | `Value: Holocron-Sentinel`
        *   `Key: DataClassification` | `Value: Confidential`
        *   `Key: ComplianceScope` | `Value: LGPD-Art37`
    *   **User Data (Script de Boot):**
        Use este script melhorado que já instala as ferramentas de segurança:
        ```bash
        #!/bin/bash
        yum update -y
        yum install -y httpd AmazonCloudWatchAgent
        systemctl start httpd
        systemctl enable httpd
        echo "<h1>Portal de Privacidade - Holocron</h1>" > /var/www/html/index.html
        # Cria logs falsos para teste de auditoria
        touch /var/log/secure-access.log
        ```

---

## Fase 2: O Agente Espião (CloudWatch Agent)

### 3. Configuração do Agente
*   **Original:** Baixar um JSON genérico do S3 do curso.
*   **Adaptação Holocron:** Criar nosso próprio arquivo de configuração focado em auditoria.
    1.  Conecte na instância (via EC2 Instance Connect).
    2.  Crie o arquivo: `nano config.json`
    3.  Cole o conteúdo do arquivo `04_CODE/cloudwatch_agent_config.json` (que está no seu repositório).
    4.  *Por que?* O original monitora apenas "disco". O nosso monitora "Tentativas de Acesso" e "Logs de Erro", que são vitais para a LGPD.

### 4. Inicialização
*   Rodar o comando de start apontando para o arquivo criado:
    ```bash
    sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:config.json -s
    ```

---

## Fase 3: Detecção de Incidentes (Alarms)

### 5. Configurando o Alerta (SNS)
*   **Original:** Alarme de CPU alta.
*   **Adaptação Holocron:** Alarme de **Invasão (404 Scanning)**.
    1.  Vá no CloudWatch > **Log Groups**.
    2.  Entre em `HttpErrorLog`.
    3.  Crie um **Metric Filter**: `[date, time, client, status=404, size, referer, agent]`.
    4.  Crie um Alarme para disparar se houver **> 3 erros em 1 minuto**.
    5.  Tópico SNS: `Holocron-DPO-Alerts`. E-mail: **SEU EMAIL REAL**.

---

## Fase 4: O Teste de Conformidade

### 6. Simulação de Ataque
Em vez de rodar `stress` (que só testa CPU), vamos rodar um `Scanning`:
1.  Abra o navegador com o IP da instância.
2.  Tente acessar páginas que não existem repetidamente para gerar Logs 404:
    *   `http://[IP]/admin`
    *   `http://[IP]/backup.zip`
    *   `http://[IP]/passwords.txt`
3.  Verifique seu e-mail. Você deve receber um alerta: **"ALARM: Potential Web Scanning Detected"**.

---

## Checklist de Evidências (Para o LinkedIn)
1.  [ ] Print das **Tags da EC2** mostrando a classificação de dados.
2.  [ ] Print do **JSON customizado** no terminal.
3.  [ ] Print do **E-mail de Alerta** recebido no celular/PC.
