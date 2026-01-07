# LGPD x AWS: Mapeamento de Conformidade (Holocron Sentinel)

## Objetivo do Documento
Este documento traduz os requisitos jurídicos da **Lei Geral de Proteção de Dados (13.709/2018)** em configurações técnicas implementadas neste projeto.

---

## Mapeamento Técnico de Requisitos Legais

### 1. Soberania e Localização de Dados (Art. 3º)
A LGPD se aplica ao tratamento realizado no território nacional ou sobre dados coletados aqui.
*   **Implementação AWS:** Seleção da região **São Paulo (`sa-east-1`)** para recursos de armazenamento persistente.
*   **Justificativa:** Garante que a residência física dos dados esteja sob jurisdição brasileira primária, reduzindo latência e complexidade legal de transferência internacional.

### 2. Segurança e Sigilo (Art. 46)
O controlador deve adotar medidas técnicas para proteger os dados pessoais.
*   **Implementação AWS:**
    *   **Em Repouso (At Rest):** Volumes EBS e Buckets S3 com criptografia padrão (**SSE-S3** ou **AWS KMS**).
    *   **Em Trânsito (In Transit):** Acesso web via HTTPS (TLS 1.2+) e API calls via endpoints seguros.

### 3. Registro de Operações (Art. 37)
O controlador deve manter registro das operações de tratamento de dados pessoais.
*   **Implementação AWS:**
    *   **AWS CloudTrail:** Habilitado para registrar *quem* fez *o que*, *onde* e *quando*.
    *   **Log Retention:** Configuração de Lifecycle no S3 para reter logs por 5 anos (compliance legal).

### 4. Gestão de Acesso (Princípio da Segurança - Art. 6º)
*   **Implementação AWS:**
    *   **IAM (Identity and Access Management):** Uso de *Roles* para instâncias EC2 (evitando credenciais hardcoded).
    *   **MFA (Multi-Factor Authentication):** Obrigatório para conta Root e usuários Admins.

---

## 🔍 Evidência de Auditoria
Para auditar estes controles, consulte os logs gerados no módulo de monitoramento:
> `05_EVIDENCE/MONITORING_LAB_EVIDENCE.md`

---

## 5. Compromisso com a Privacidade do Titular
Mais do que uma obrigação legal, o Holocron Sentinel prioriza a transparência. Cada componente técnico listado acima serve como uma camada de proteção aos direitos fundamentais de liberdade e privacidade do cidadão brasileiro, transformando a conformidade em um valor ético da organização.
