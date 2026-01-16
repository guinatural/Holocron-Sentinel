# Kit de Implementação — Holocron Sentinel Security Setup

Este documento integra a documentação estratégica (`AWS_SECURITY_SETUP.md`) com artefatos técnicos executáveis, formando um kit completo de implementação de segurança AWS com conformidade LGPD.

---

## Estrutura do Kit

```
04_CODE/
├── iam_policies/
│   ├── admin_group_policy.json          # Política para administradores
│   ├── developer_group_policy.json      # Política para desenvolvedores
│   └── readonly_group_policy.json       # Política para auditores
├── scripts/
│   ├── setup_iam_structure.py           # Automação de IAM
│   └── billing_alerts_setup.py          # Automação de billing alerts
└── IMPLEMENTATION_KIT.md                # Este documento
```

---

## Fase 1: Preparação do Ambiente

### Pré-requisitos Técnicos

**AWS CLI Configurado:**
```bash
aws --version
# Deve retornar: aws-cli/2.x.x ou superior

aws configure
# Inserir Access Key e Secret Key de usuário com permissões administrativas
```

**Python 3.8+ com Boto3:**
```bash
python --version
pip install boto3
```

**Credenciais AWS:**
- Access Key ID e Secret Access Key configurados
- Permissões necessárias: IAM Full Access, CloudWatch Full Access, SNS Full Access

---

## Fase 2: Execução Automatizada

### 2.1 Setup de Estrutura IAM

**Objetivo:** Criar grupos, políticas e usuário administrativo conforme `AWS_SECURITY_SETUP.md`.

**Arquivo:** `scripts/setup_iam_structure.py`

**Execução:**
```bash
cd 04_CODE/scripts
python setup_iam_structure.py
```

**O que será criado:**
- Grupos IAM: `Admins`, `Developers`, `ReadOnly`
- Políticas inline anexadas aos grupos
- Usuário `gui-dev-admin` no grupo Admins
- Política de senhas global (14 chars, 90 dias expiração)
- Relatório de credenciais para auditoria

**Saída esperada:**
```
============================================================
Holocron Sentinel - IAM Security Setup
Compliance: LGPD Art. 46 | AWS Well-Architected Security
============================================================

[STEP 1] Configurando política de senhas da conta
[OK] Política de senhas configurada: 14 chars, complexidade alta

[STEP 2] Criando grupos IAM
[OK] Grupo 'Admins' criado com sucesso
[OK] Política anexada ao grupo 'Admins'
[...]

Setup concluído com sucesso!
```

---

### 2.2 Configuração de Billing Alerts

**Objetivo:** Criar alarmes CloudWatch para monitoramento de custos.

**Arquivo:** `scripts/billing_alerts_setup.py`

**Configuração obrigatória:**
Editar o arquivo e alterar a variável:
```python
EMAIL_ADDRESS = "seu-email@exemplo.com"  # Substituir por email real
```

**Execução:**
```bash
python billing_alerts_setup.py
```

**O que será criado:**
- Tópico SNS: `BillingAlerts-HolocronSentinel`
- 3 Alarmes CloudWatch:
  - `Billing-Alert-10USD-Initial` (threshold: $10)
  - `Billing-Alert-50USD-Moderate` (threshold: $50)
  - `Billing-Alert-95USD-Critical` (threshold: $95)

**Ação pós-execução:**
Confirmar subscription no email recebido da AWS.

---

## Fase 3: Validação Manual

### 3.1 Checklist de Configuração Root Account

**Console AWS → Account → Security Credentials**

- [ ] MFA ativado na conta root
- [ ] Senha root alterada (14+ caracteres)
- [ ] Verificado que NÃO existem Access Keys para root
- [ ] Account ID documentado em local seguro

---

### 3.2 Checklist de Configuração IAM User

**Console AWS → IAM → Users → gui-dev-admin**

- [ ] Login realizado com sucesso
- [ ] Senha temporária alterada
- [ ] MFA virtual ativado (Google Authenticator/Authy)
- [ ] Grupos verificados: presente em `Admins`
- [ ] Testado: acesso negado sem MFA

---

### 3.3 Checklist de Billing Alerts

**Console AWS → CloudWatch → Alarms (região us-east-1)**

- [ ] 3 alarmes visíveis e em estado `OK` ou `INSUFFICIENT_DATA`
- [ ] SNS topic `BillingAlerts-HolocronSentinel` criado
- [ ] Email subscription confirmado
- [ ] Billing preferences habilitado:
  - Billing Dashboard → Preferences → Receive Billing Alerts

---

## Fase 4: Documentação de Evidências

### Template de Evidências

Para cada componente implementado, gerar:

**1. Screenshot do Console AWS:**
- IAM Groups listados
- IAM User `gui-dev-admin` criado
- MFA devices ativos
- CloudWatch Alarms configurados

**2. Logs de Execução:**
- Saída completa dos scripts Python
- Credential report gerado (`credential_report.csv`)

**3. Validação de Compliance:**
- Política de senhas: captura da tela IAM Account Settings
- CloudTrail: verificar que eventos de criação estão logados

**Caminho de armazenamento:** `05_EVIDENCE/IAM_SETUP_EVIDENCE.md`

---

## Fase 5: Auditoria e Compliance

### Mapeamento LGPD

**Artigo 46 LGPD:**
> "Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados"

**Controles implementados:**
- **MFA Enforcement:** Impede acesso sem autenticação multifator
- **Least Privilege:** Separação de funções via grupos IAM
- **Auditoria:** CloudTrail registra todas as ações (quem fez o quê)
- **Accountability:** Billing alerts previnem uso não autorizado de recursos

---

## Referências Técnicas

**Políticas IAM:**
- JSON Schema: [IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)
- MFA Conditions: [Using MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html)

**Billing Alerts:**
- [Creating Billing Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)

**Best Practices:**
- [AWS Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

---

## Troubleshooting

### Erro: "AccessDenied" ao executar scripts

**Causa:** Credenciais AWS não possuem permissões necessárias.

**Solução:**
```bash
aws iam get-user
# Verificar se o comando retorna seu usuário atual

# Anexar política AdministratorAccess ao usuário (temporariamente para setup)
```

---

### Erro: "InvalidClientTokenId"

**Causa:** Credenciais AWS não configuradas ou expiradas.

**Solução:**
```bash
aws configure list
# Verificar se Access Key está configurado

# Reconfigurar:
aws configure
```

---

### Alarmes de billing em "INSUFFICIENT_DATA"

**Causa:** Métricas de billing levam até 6h para aparecer.

**Solução:** Aguardar e verificar novamente. Estado normal para alarmes recém-criados.

---

## Próximos Passos

Após conclusão deste kit:

1. **Fase 2 do Projeto:** Configurar CloudTrail multi-region
2. **Implementar:** S3 Bucket para Data Lake com criptografia KMS
3. **Ativar:** AWS Config para monitoramento de compliance contínuo

**Referência:** `00-Master/PROJECT_OVERVIEW.md` - Cronograma de Implementação
