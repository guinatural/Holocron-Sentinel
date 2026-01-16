# Evidências de Implementação — IAM Security Setup

**Projeto:** Holocron Sentinel  
**Fase:** 1 - Security Foundation  
**Data de Execução:** [Preencher após execução]  
**Responsável:** Guilherme Barreto  

---

## 1. Configuração da Conta Root

### 1.1 Multi-Factor Authentication (MFA)

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot do console AWS mostrando MFA ativo na conta root
- Tipo de dispositivo MFA utilizado (Virtual/Hardware)

**Caminho:** `IAM_ROOT_MFA.png`

**Validação:**
```bash
# Comando para verificar (executar com credenciais de admin)
aws iam get-account-summary | grep "AccountMFAEnabled"
# Resultado esperado: 1 (ativo)
```

---

### 1.2 Política de Senhas Global

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot: IAM > Account Settings > Password Policy
- Configurações visíveis:
  - Minimum length: 14 characters
  - Password expiration: 90 days
  - Password reuse prevention: 5 passwords

**Caminho:** `IAM_PASSWORD_POLICY.png`

**Validação via CLI:**
```bash
aws iam get-account-password-policy
```

**Output esperado:**
```json
{
  "PasswordPolicy": {
    "MinimumPasswordLength": 14,
    "RequireSymbols": true,
    "RequireNumbers": true,
    "RequireUppercaseCharacters": true,
    "RequireLowercaseCharacters": true,
    "ExpirePasswords": true,
    "MaxPasswordAge": 90,
    "PasswordReusePrevention": 5
  }
}
```

---

## 2. Estrutura IAM - Grupos e Políticas

### 2.1 Grupos Criados

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot: IAM > Groups mostrando os 3 grupos criados
- Lista de grupos: Admins, Developers, ReadOnly

**Caminho:** `IAM_GROUPS_LIST.png`

**Validação via CLI:**
```bash
aws iam list-groups
```

**Output esperado:**
```json
{
  "Groups": [
    {
      "GroupName": "Admins",
      "Path": "/",
      "CreateDate": "YYYY-MM-DDTHH:MM:SSZ",
      "GroupId": "AGPAI..."
    },
    {
      "GroupName": "Developers",
      [...]
    },
    {
      "GroupName": "ReadOnly",
      [...]
    }
  ]
}
```

---

### 2.2 Políticas Anexadas

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot de cada grupo mostrando a política inline anexada
- Confirmação de que políticas contêm enforcement de MFA

**Caminhos:**
- `IAM_ADMINS_POLICY.png`
- `IAM_DEVELOPERS_POLICY.png`
- `IAM_READONLY_POLICY.png`

**Validação via CLI:**
```bash
# Verificar política do grupo Admins
aws iam get-group-policy --group-name Admins --policy-name AdminsPolicy

# Verificar condição de MFA
aws iam get-group-policy --group-name Admins --policy-name AdminsPolicy \
  | grep -A5 "MultiFactorAuthPresent"
```

---

## 3. Usuário Administrativo

### 3.1 Criação do Usuário gui-dev-admin

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot: IAM > Users > gui-dev-admin
- Detalhes visíveis:
  - Grupos: Admins
  - Password age
  - MFA device: Assigned

**Caminho:** `IAM_USER_ADMIN_DETAILS.png`

**Validação via CLI:**
```bash
aws iam get-user --user-name gui-dev-admin
aws iam list-groups-for-user --user-name gui-dev-admin
```

---

### 3.2 MFA Ativo no Usuário

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot mostrando MFA device ativo
- Tipo de dispositivo (arn:aws:iam::ACCOUNT:mfa/gui-dev-admin)

**Caminho:** `IAM_USER_MFA_ACTIVE.png`

**Validação via CLI:**
```bash
aws iam list-mfa-devices --user-name gui-dev-admin
```

**Output esperado:**
```json
{
  "MFADevices": [
    {
      "UserName": "gui-dev-admin",
      "SerialNumber": "arn:aws:iam::ACCOUNT_ID:mfa/gui-dev-admin",
      "EnableDate": "YYYY-MM-DDTHH:MM:SSZ"
    }
  ]
}
```

---

## 4. Billing Alerts e Monitoramento

### 4.1 Tópico SNS Criado

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot: SNS > Topics > BillingAlerts-HolocronSentinel
- Subscription confirmada (Status: Confirmed)

**Caminho:** `SNS_BILLING_TOPIC.png`

**Validação via CLI:**
```bash
aws sns list-topics --region us-east-1 | grep BillingAlerts
aws sns list-subscriptions-by-topic \
  --topic-arn arn:aws:sns:us-east-1:ACCOUNT_ID:BillingAlerts-HolocronSentinel \
  --region us-east-1
```

---

### 4.2 Alarmes CloudWatch Configurados

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot: CloudWatch > Alarms (região us-east-1)
- 3 alarmes visíveis:
  - Billing-Alert-10USD-Initial
  - Billing-Alert-50USD-Moderate
  - Billing-Alert-95USD-Critical

**Caminho:** `CLOUDWATCH_BILLING_ALARMS.png`

**Validação via CLI:**
```bash
aws cloudwatch describe-alarms --region us-east-1 | grep BillingAlert
```

**Output esperado:**
```json
{
  "MetricAlarms": [
    {
      "AlarmName": "Billing-Alert-10USD-Initial",
      "Threshold": 10.0,
      "ComparisonOperator": "GreaterThanOrEqualToThreshold"
    },
    [...]
  ]
}
```

---

### 4.3 Billing Preferences Habilitado

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot: Billing & Cost Management > Billing Preferences
- Checkboxes marcados:
  - Receive PDF Invoice By Email
  - Receive Free Tier Usage Alerts
  - Receive Billing Alerts

**Caminho:** `BILLING_PREFERENCES.png`

**Nota:** Esta configuração é manual e só pode ser feita via Console AWS.

---

## 5. Auditoria e Compliance

### 5.1 CloudTrail Verificação

**Status:** [ ] Concluído

**Evidência requerida:**
- Screenshot de eventos de criação no CloudTrail:
  - CreateGroup
  - CreateUser
  - PutGroupPolicy
  - CreateTopic (SNS)
  - PutMetricAlarm

**Caminho:** `CLOUDTRAIL_EVENTS.png`

**Validação via CLI:**
```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=CreateUser \
  --max-results 10
```

---

### 5.2 Credential Report

**Status:** [ ] Concluído

**Evidência requerida:**
- Arquivo CSV: `credential_report.csv` (gerado pelo script)
- Análise do relatório mostrando:
  - Root com MFA: yes
  - gui-dev-admin com MFA: yes
  - Nenhum access key para root

**Caminho:** `credential_report.csv`

**Geração:**
```bash
aws iam generate-credential-report
aws iam get-credential-report --query 'Content' --output text | base64 -d > credential_report.csv
```

---

## 6. Execução dos Scripts

### 6.1 Log de Execução - setup_iam_structure.py

**Status:** [ ] Concluído

**Evidência requerida:**
- Arquivo de log completo da execução do script
- Todos os steps marcados como [OK]

**Caminho:** `SCRIPT_IAM_EXECUTION_LOG.txt`

**Captura:**
```bash
python setup_iam_structure.py > SCRIPT_IAM_EXECUTION_LOG.txt 2>&1
```

---

### 6.2 Log de Execução - billing_alerts_setup.py

**Status:** [ ] Concluído

**Evidência requerida:**
- Arquivo de log completo da execução do script
- Confirmação de criação de tópico e alarmes

**Caminho:** `SCRIPT_BILLING_EXECUTION_LOG.txt`

**Captura:**
```bash
python billing_alerts_setup.py > SCRIPT_BILLING_EXECUTION_LOG.txt 2>&1
```

---

## 7. Conformidade LGPD

### 7.1 Mapeamento de Controles

| Requisito LGPD | Controle AWS Implementado | Status |
|----------------|---------------------------|--------|
| Art. 46 - Medidas de Segurança Técnicas | IAM com MFA Enforcement | [ ] |
| Art. 46 - Proteção contra acessos não autorizados | Least Privilege via Groups | [ ] |
| Art. 37 - Registro de Operações | CloudTrail ativo | [ ] |
| Art. 48 - Comunicação de Incidentes | Billing Alerts (SNS) | [ ] |

---

## 8. Checklist Final de Validação

**Configurações Root:**
- [ ] MFA ativo
- [ ] Senha forte (14+ chars)
- [ ] Sem Access Keys
- [ ] Account ID documentado

**IAM Structure:**
- [ ] 3 grupos criados (Admins, Developers, ReadOnly)
- [ ] Políticas inline anexadas
- [ ] MFA enforcement nas políticas
- [ ] Política de senhas global configurada

**Usuário Administrativo:**
- [ ] gui-dev-admin criado
- [ ] Presente no grupo Admins
- [ ] MFA ativo
- [ ] Login testado

**Billing & Monitoring:**
- [ ] SNS topic criado
- [ ] Email subscription confirmado
- [ ] 3 alarmes CloudWatch ativos
- [ ] Billing preferences habilitado

**Auditoria:**
- [ ] CloudTrail registrou todos os eventos
- [ ] Credential report gerado
- [ ] Logs de execução salvos

---

## 9. Assinatura de Conformidade

**Declaro que todas as configurações acima foram implementadas conforme especificação técnica do projeto Holocron Sentinel, seguindo as diretrizes do AWS Well-Architected Framework Security Pillar e em conformidade com o Art. 46 da LGPD.**

**Responsável:** Guilherme Barreto  
**Data:** ___/___/______  
**Assinatura:** _______________________

---

## 10. Anexos

**Arquivos de evidência esperados:**
```
05_EVIDENCE/IAM_SETUP/
├── IAM_ROOT_MFA.png
├── IAM_PASSWORD_POLICY.png
├── IAM_GROUPS_LIST.png
├── IAM_ADMINS_POLICY.png
├── IAM_DEVELOPERS_POLICY.png
├── IAM_READONLY_POLICY.png
├── IAM_USER_ADMIN_DETAILS.png
├── IAM_USER_MFA_ACTIVE.png
├── SNS_BILLING_TOPIC.png
├── CLOUDWATCH_BILLING_ALARMS.png
├── BILLING_PREFERENCES.png
├── CLOUDTRAIL_EVENTS.png
├── credential_report.csv
├── SCRIPT_IAM_EXECUTION_LOG.txt
└── SCRIPT_BILLING_EXECUTION_LOG.txt
```
