# Setup Inicial de Segurança AWS — Holocron Sentinel

Este guia documenta os passos críticos de segurança realizados na fase inicial do projeto para garantir a integridade da infraestrutura e a conformidade com as melhores práticas da AWS e regulamentações de privacidade (LGPD).

---

## 1. Proteção da Conta Raiz (Root Account)

A conta root possui acesso irrestrito a todos os recursos e faturamento. Sua proteção é o primeiro passo de qualquer arquitetura segura.

**Checklist de Segurança Root:**
- [ ] **MFA Ativo:** Configurado via aplicativo autenticador (Google Authenticator/Authy).
- [ ] **Senha Forte:** Mínimo de 14 caracteres com complexidade elevada.
- [ ] **Sem Access Keys:** Garantir que não existem chaves de acesso programático para o usuário root.
- [ ] **ID da Conta:** Documentado em local seguro para recuperação.

### Procedimento no Console:
1. Acesse **Security Credentials** no menu da conta.
2. Em **Multi-Factor Authentication (MFA)**, selecione **Activate MFA**.
3. Escolha **Virtual MFA device** e escaneie o código QR.
4. Insira dois códigos consecutivos para sincronização.

---

## 2. Configuração do Usuário Administrativo (IAM)

Para o uso diário, utilizamos um usuário IAM com permissões administrativas, nunca a conta root diretamente.

### Estratégia de Identidade:
- **Username:** `gui-dev-admin`.
- **Acesso ao Console:** Habilitado com senha customizada.
- **MFA:** Obrigatório para o usuário administrador.

### Estrutura de Grupos Inicial:
| Grupo | Política (Policy) | Finalidade |
| :--- | :--- | :--- |
| **Admins** | `AdministratorAccess` | Gestão total da infraestrutura. |
| **Developers** | Políticas Customizadas | Desenvolvimento e deployment. |
| **ReadOnly** | `ReadOnlyAccess` | Auditoria e visualização. |

---

## 3. Gestão de Access Keys (CLI/SDK)

As chaves de acesso são criadas apenas sob demanda e seguindo o princípio do menor privilégio.

```bash
# Configuração local da CLI após criação da key no IAM
aws configure

# Parâmetros necessários:
# AWS Access Key ID: AKIA...
# AWS Secret Access Key: ...
# Default region: us-east-1
# Default output format: json
```

**Boas Práticas:**
- Rotação regular (90 dias).
- Nunca incluir chaves em repositórios Git (uso de `.gitignore` rigoroso).
- Recomendado o uso de ferramentas como `aws-vault` para armazenamento seguro.

---

## 4. Gestão de Custos e Faturamento (Billing)

Monitoramento proativo para evitar surpresas no faturamento e garantir o uso dentro do Free Tier/Créditos.

### Alertas de Faturamento (CloudWatch):
- Ativar **Receive Billing Alerts** nas preferências de faturamento.
- Criar Alarmes no CloudWatch para os seguintes patamares:
  - **$10:** Alerta de consumo inicial.
  - **$50:** Alerta de consumo moderado.
  - **$95:** Alerta crítico (esgotamento de créditos/free tier).

### AWS Budgets:
Configuração de um **Cost Budget** de $100 com notificações em 50%, 80% e 100% de uso.

---

## 5. Política de Senhas e Compliance

Configuração global no IAM (Account Settings) para garantir que todos os usuários sigam padrões de segurança:

- **Comprimento mínimo:** 14 caracteres.
- **Complexidade:** Letras maiúsculas, minúsculas, números e caracteres especiais.
- **Expiração:** 90 dias.
- **Prevenção de reuso:** Histórico das últimas 5 senhas.

---

## 6. Auditoria com CloudTrail

Ativação do log de auditoria para registrar todas as chamadas de API feitas na conta.

- **Trail Name:** `management-events-trail`
- **Storage:** Bucket S3 dedicado e criptografado.
- **Objetivo:** Rastreabilidade completa (Quem fez o quê, onde e quando).

---

## 7. Estratégia de Tagging

Todos os recursos criados devem ser tagueados para facilitar a governança e o controle de custos.

```json
{
  "Environment": "dev|staging|prod",
  "Project": "holocron-sentinel",
  "Owner": "guilherme",
  "CostCenter": "security-compliance-study",
  "ManagedBy": "terraform|manual"
}
```

---

## 8. Responsabilidade Compartilhada (AWS & Holocron)

- **AWS:** Segurança **da** Nuvem (Infraestrutura, Data Centers, Hardware).
- **Holocron Sentinel (Nós):** Segurança **na** Nuvem (Configurações de IAM, Criptografia de Dados, Políticas de Firewall, Patching de OS).
