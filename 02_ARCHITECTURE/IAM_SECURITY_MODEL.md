# Modelo de Segurança e Acesso (IAM RBAC)

## 🎯 Objetivo
Implementar o princípio de **Least Privilege** (Menor Privilégio) exigido pelo **Art. 6º** da LGPD (Princípio da Segurança).

---

## 🔐 Política de MFA Obrigatório
Todos os usuários humanos devem possuir MFA ativado para realizar qualquer ação que não seja configurar o próprio MFA.
**Implementação:** Política Anexada `iam_mfa_enforcement.json` (Veja pasta `04_CODE`).

---

## 👥 Definição de Grupos e Funções (RBAC)

### 1. `krayt-council` (Administradores)
*   **Acesso:** Full Access (exceto Billing).
*   **Política:** `AdministratorAccess` + `ForceMFA`.
*   **Responsabilidade:** Gestão de emergência e configuração inicial.

### 2. `holocron-keepers` (Auditores / DPO)
*   **Acesso:** Leitura em Logs e Configurações ("Read-Only").
*   **Política:** `SecurityAudit` + `CloudTrailReadOnly` + `ForceMFA`.
*   **Responsabilidade:** Auditoria de compliance (LGPD Art. 37) e revisão de incidentes.
*   *Nota:* Não podem alterar configurações, apenas reportar.

### 3. `sentinel-guardians` (DevSecOps)
*   **Acesso:** Operacional em EC2, Lambda e S3 (específico do projeto).
*   **Política:** `PowerUserAccess` (Restrito por Region) + `ForceMFA`.
*   **Responsabilidade:** Deploy e manutenção da infraestrutura de segurança.

---

## 🚫 Estratégia de Bloqueio
*   **Root User:** Acesso desabilitado (senha complexa + MFA físico no cofre).
*   **Access Keys:** Rotação a cada 90 dias (via AWS Config Rule).
