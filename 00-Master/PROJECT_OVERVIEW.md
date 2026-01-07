# Holocron Sentinel — Sistema de Conformidade LGPD na AWS

## 1. 🎯 Problema Central
Implementar uma solução em nuvem AWS que garanta a conformidade com a **Lei Geral de Proteção de Dados (LGPD)** para uma empresa que processa dados pessoais de clientes brasileiros.

---

## 2. 🏗️ Arquitetura Recomendada

### Componentes Principais
*   **Amazon S3 (Criptografado):** Armazenamento seguro de dados pessoais (Data Lake).
*   **AWS IAM + MFA:** Controle rigoroso de acesso baseada no princípio do menor privilégio (*Least Privilege*).
*   **AWS CloudTrail + AWS Config:** Auditoria completa e monitoramento contínuo de conformidade.
*   **Amazon Macie:** Classificação automática e proteção de dados sensíveis (PII).
*   **AWS KMS:** Gerenciamento centralizado de chaves de criptografia (CMKs).
*   **AWS WAF & Shield:** Proteção perimetral contra violações e ataques web.

---

## 3. 🔄 Fluxo de Conformidade LGPD
1.  **Coleta de Dados** (Secure Ingestion)
2.  **Criptografia** (KMS at Rest/TLS in Transit)
3.  **Armazenamento Seguro** (S3 Bucket Policies)
4.  **Auditoria Contínua** (CloudTrail/Config)
5.  **Resposta a Incidentes** (EventBridge/Lambda)

---

## 4. 📦 Módulos do Projeto

### Módulo 1: Governança de Dados
*   Políticas de retenção e exclusão automática (S3 Lifecycle).
*   Mapeamento de fluxo de dados pessoais.
*   Registro das atividades de processamento (**Art. 37 LGPD**).

### Módulo 2: Segurança Técnica
*   Criptografia em repouso e trânsito obrigatória.
*   Estratégia de Backup e *Disaster Recovery* (Cross-Region).
*   Técnicas de Anonimização e Pseudonimização.

### Módulo 3: Direitos do Titular
*   Portal para exercício de direitos (acesso, correção, exclusão).
*   Sistema de requisições automatizadas (API Gateway + Lambda).
*   Painel de transparência.

---

## 5. 📊 Metas Mensuráveis
*   ✅ Reduzir tempo de resposta a incidentes para **< 24h**.
*   ✅ **100%** dos dados pessoais criptografados.
*   ✅ Auditoria trimestral automatizada.
*   ✅ Portal do titular com SLA de **72h** para requisições.

---

## 6. 🛡️ Serviços AWS Essenciais
*   **Security Hub:** Visão unificada da postura de segurança.
*   **AWS Certificate Manager (ACM):** Gerenciamento de certificados SSL/TLS.
*   **Amazon Cognito:** Gerenciamento de identidade (CIAM) para o portal do titular.
*   **AWS Lambda:** Automação de processos de "Direito ao Esquecimento".

---

## 7. ✅ Validação de Conformidade
*   Relatórios automáticos do **AWS Artifact**.
*   Checkpoints do **AWS Well-Architected Framework** (Security & Operational Excellence Pilliars).
*   Testes de penetração automatizados com **Amazon Inspector**.

---

## 🚀 Roadmap de Implementação
*   **Fase 1 (2 semanas):** Implementação da base de segurança (IAM, KMS, CloudTrail).
*   **Fase 2 (3 semanas):** Sistema de gestão de consentimento e portal do titular.
*   **Fase 3 (2 semanas):** Automação de auditoria e relatórios de conformidade.
