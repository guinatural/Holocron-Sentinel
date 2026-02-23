# LGPD x AWS: Mapeamento de Conformidade (Holocron Sentinel)

## Objetivo do Documento
Este documento serve como a **Matriz de Rastreabilidade** entre os requisitos jurídicos da **Lei Geral de Proteção de Dados (13.709/2018)** e as implementações técnicas deste projeto na AWS.

---

## Matriz Técnica de Conformidade

### 1. Soberania e Localização (Art. 3º)
*   **Requisito:** Tratamento realizado no território nacional ou sobre dados coletados no Brasil.
*   **Implementação AWS:** Pinagem de 100% dos recursos de armazenamento na região **São Paulo (`sa-east-1`)**.
*   **Justificativa:** Garante jurisdição brasileira e atende requisitos contratuais de residência de dados.

### 2. Segurança e Sigilo (Art. 46)
*   **Requisito:** Medidas técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados.
*   **Implementação AWS:**
    *   Criptografia em repouso com **AES-256** (SSE-S3 e SSE-KMS).
    *   Script `validate_audit_logs.py` para conferência contínua de status de criptografia.
    *   Trânsito protegido via **TLS 1.2+**.

### 3. Registro de Operações (Art. 37)
*   **Requisito:** O controlador e o operador devem manter registros das operações de tratamento.
*   **Implementação AWS:**
    *   **AWS CloudTrail:** Logs de Data Events e Management Events habilitados.
    *   **S3 Object Lock/Versioning:** Proteção contra alteração ou exclusão de trilhas de auditoria.

### 4. Direitos do Titular (Art. 18)
*   **Requisito:** Garantia de acesso, correção, anonimização ou exclusão de dados.
*   **Implementação AWS:**
    *   Arquitetura preparada para integração com **AWS Lambda** para execução de "Direito ao Esquecimento" (Work in Progress).
    *   Segregação de dados via **Tags** para facilitar a busca por UID de usuários.

### 5. Comunicação de Incidentes (Art. 48)
*   **Requisito:** Comunicação ao órgão encarregado e ao titular em caso de incidente de segurança.
*   **Implementação AWS:**
    *   **AWS Config + SNS:** Alertas automáticos para configurações fora de conformidade (ex: bucket público).
    *   **CloudWatch Alarms:** Alertas de billing e acessos anômalos.

### 6. Princípios da Segurança e Prevenção (Art. 6º, VII e VIII)
*   **Requisito:** Gerenciamento de riscos e medidas para evitar danos.
*   **Implementação AWS:**
    *   **IAM Least Privilege:** Uso de Policies restritivas JSON.
    *   **MFA enforcement:** Bloqueio de API calls para usuários sem token de segurança.

---

## Verificação Técnica
Para visualizar estes controles em ação durante a auditoria:
1.  Acesse o painel interativo: `index.html`
2.  Execute o script de auditoria: `04_CODE/validate_audit_logs.py`
3.  Confira as evidências: `05_EVIDENCE/`

---

## Compromisso Ético
A tecnologia no Holocron Sentinel é um meio para um fim: a preservação da privacidade como um direito fundamental. Nossa arquitetura foi desenhada sob os princípios de **Privacy by Design** e **Privacy by Default**.
