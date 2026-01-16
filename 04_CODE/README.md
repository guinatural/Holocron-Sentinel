# Holocron Sentinel - Implementation Kit

## Quick Start

Este diretório contém o **Kit de Implementação Técnica** do sistema Holocron Sentinel, incluindo políticas IAM, scripts de automação e templates de evidência.

---

## Estrutura

```
04_CODE/
├── iam_policies/              # Políticas IAM em JSON
├── scripts/                   # Scripts Python de automação
│   └── requirements.txt       # Dependências
├── cloudwatch_agent_config.json
├── iam_mfa_enforcement.json
├── validate_audit_logs.py
└── IMPLEMENTATION_KIT.md      # Guia completo de implementação
```

---

## Documentos Principais

**[IMPLEMENTATION_KIT.md](IMPLEMENTATION_KIT.md)**  
Guia master de implementação com todas as fases do setup de segurança.

**[../00-Master/AWS_SECURITY_SETUP.md](../00-Master/AWS_SECURITY_SETUP.md)**  
Documentação estratégica de segurança AWS.

**[../05_EVIDENCE/IAM_SETUP_EVIDENCE.md](../05_EVIDENCE/IAM_SETUP_EVIDENCE.md)**  
Template para documentação de evidências.

---

## Execução Rápida

### 1. Instalar Dependências

```bash
cd scripts
pip install -r requirements.txt
```

### 2. Configurar AWS CLI

```bash
aws configure
# Inserir Access Key, Secret Key e região padrão
```

### 3. Executar Setup IAM

```bash
python setup_iam_structure.py
```

### 4. Executar Setup de Billing Alerts

```bash
# Editar EMAIL_ADDRESS no arquivo antes de executar
python billing_alerts_setup.py
```

---

## Políticas Incluídas

**admin_group_policy.json**  
Acesso administrativo completo com enforcement de MFA.

**developer_group_policy.json**  
Acesso a serviços de desenvolvimento (S3, Lambda, EC2) com MFA.

**readonly_group_policy.json**  
Acesso somente leitura para auditores.

---

## Referências

- AWS IAM Best Practices: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- LGPD Artigo 46: Medidas de Segurança Técnicas
- AWS Well-Architected Security Pillar

---

Para mais detalhes, consultar **IMPLEMENTATION_KIT.md**.
