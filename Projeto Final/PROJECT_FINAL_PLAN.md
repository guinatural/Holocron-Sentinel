# Projeto Final: Holocron Sentinel — Segurança e Conformidade LGPD na AWS
## Módulo 1: AWS re/Start + Inteligência Artificial

**Grupo:** Holocron Sentinel  
**Curso:** AWS re/Start + IA — Escola da Nuvem  
**Ano:** 2025  
**Integrantes:**
- **Guilherme Barreto Gomes** (Arquiteto de Cloud e Engenheiro de Segurança)
- [Nome do Aluno 1]
- [Nome do Aluno 2]
- [Nome do Aluno 3]

---

## Módulo RESTART

### 1. Identificação do Problema

**Ideia do Projeto:** Holocron Sentinel - Sistema de Governança de Dados e Compliance Automatizado.

**Descrição do Problema:**
Empresas brasileiras enfrentam um cenário crítico de vulnerabilidade jurídica e técnica com a vigência da LGPD (Lei 13.709/2018). O problema central não é apenas o vazamento de dados, mas a **violação da auditabilidade (Art. 37)** e a **falha na proteção de dados por design (Art. 46)**. Muitas organizações não possuem visibilidade sobre quem acessa dados sensíveis (PII) em tempo real, resultando em multas que podem chegar a R$ 50 milhões. A falta de especialistas em segurança na nuvem impede que pequenas e médias empresas implementem controles baseados em Zero-Trust, deixando dados de clientes expostos em buckets S3 sem criptografia e contas IAM sem MFA.

**Stakeholders:**
*   **DPO (Data Protection Officer):** Necessita de relatórios de conformidade para a ANPD.
*   **Diretoria de TI / CTO:** Precisa garantir a continuidade do negócio e evitar danos à reputação.
*   **Clientes (Titulares dos Dados):** Exigem transparência e segurança sobre seus dados pessoais.
*   **Auditores Externos:** Requerem registros imutáveis de operações em nuvem.

**Justificativa:**
O Holocron Sentinel utiliza a infraestrutura escalável da AWS para democratizar a segurança corporativa. Através de uma arquitetura "Glass Box", permitimos que cada transação de dado seja rastreável e protegida. A escolha pela nuvem AWS justifica-se pela capacidade de automação via CloudTrail e AWS Config, entregando conformidade contínua a um custo operacional drasticamente reduzido. No próximo módulo (Extensão em IA), evoluiremos para uma análise preditiva de ameaças.

---

### 2. Levantamento de Requisitos

**Requisitos Funcionais (RF):**
*   **[RF-001] Ingestão Criptografada:** O sistema deve exigir criptografia (KMS) em 100% dos uploads de dados sensíveis.
*   **[RF-002] Auditoria Imutável:** Registro centralizado de logs via CloudTrail com verificação de integridade (Digest).
*   **[RF-003] Validação de Identidade (MFA):** Bloqueio ou alerta de usuários administrativos operando sem Autenticação em Dois Fatores.
*   **[RF-004] Relatórios de Conformidade:** Geração automática de relatórios técnicos sobre o status de segurança do ambiente.

**Requisitos Não Funcionais (RNF):**
*   **[RNF-001] Segurança:** Criptografia em repouso padrão AES-256 (SSE-S3/SSE-KMS).
*   **[RNF-002] Durabilidade:** Armazenamento de logs com durabilidade de 99.999999999% (S3 Standard).
*   **[RNF-003] Soberania de Dados:** Toda a infraestrutura deve estar localizada na região `sa-east-1` (São Paulo).
*   **[RNF-004] Auditoria Contínua:** Logs devem ser retidos por no mínimo 5 anos conforme requisitos legais.

**MVP (Produto Mínimo Viável):**
Uma arquitetura de segurança funcional na AWS composta por:
1.  **Fundação IAM:** Grupos e políticas com MFA obrigatório.
2.  **Repositório Seguro:** Bucket S3 com bloqueio de acesso público e versionamento.
3.  **Audit Trail:** CloudTrail ativo gerando logs de leitura/escrita em dados sensíveis.
4.  **Scripts de Validação:** Ferramenta Python (boto3) para auditoria automatizada de conformidade.

---

### 3. Planejamento Ágil

**Backlog de Tarefas:**
1.  **[Core]** Desenho da Arquitetura Zero-Trust e fluxograma de dados.
2.  **[IAM]** Configuração de Grupos (Admin/Dev/Audit) e MFA Enforcement (Art. 46).
3.  **[S3]** Provisionamento de Bucket Data Lake com criptografia KMS.
4.  **[Logs]** Implementação de CloudTrail Multi-Region e log de integridade.
5.  **[Code]** Desenvolvimento de script Python para validação automática de logs (`validate_audit_logs.py`).
6.  **[Review]** Simulação de incidentes de acesso e validação de trilha de auditoria.

**Sprints:**
*   **Sprint 1:** Planejamento e Arquitetura. Entrega: Documento de Requisitos e Diagrama AWS.
*   **Sprint 2:** Implementação Identity & Access Management (IAM). Entrega: Ambiente AWS configurado.
*   **Sprint 3:** Governança de Dados e Auditoria. Entrega: CloudTrail Logs e S3 Secure Buckets.
*   **Sprint 4:** Automação e Apresentação. Entrega: Script Python de Auditoria e Pitch Final.

**Quadro (Board):**
O progresso é monitorado via GitHub Projects / Trello, utilizando as colunas:
*   **To Do:** Atividades mapeadas no Backlog.
*   **In Progress:** Implementação técnica em andamento no console AWS/VS Code.
*   **Verification:** Teste de scripts e validação de logs.
*   **Done:** Tarefas com evidência (screenshot/log) anexada.

*(Link/Print do Quadro simulado: Disponível na pasta 01_SPRINTS)*

---

### 4. Apresentação Final (Roteiro de 15 Minutos)

**Estrutura da Apresentação:**

| Tempo | Seção | Objetivo | Recurso Visual |
|-------|-------|----------|----------------|
| **2 min** | **Introdução** | Apresentação pessoal e "The Hook" (A crise da LGPD). | Slide de Capa |
| **3 min** | **O Problema** | Descrição do risco financeiro e jurídico para empresas sem governança AWS. | REQUIREMENTS_DOC.md |
| **3 min** | **A Solução** | Explicação da Arquitetura Holocron Sentinel baseada em Zero-Trust. | 02_ARCHITECTURE |
| **4 min** | **Gestão e Agilidade** | Demonstração do Backlog, Sprints e as soft skills de coordenação. | BACKLOG_SPRINTS.md |
| **3 min** | **IA & Próximos Passos** | Demonstração do Script de Auditoria e Roadmap para Extensão em IA. | 04_CODE |

**Próximos Passos (Módulo EXTENSÃO EM IA):**
Na próxima etapa, integraremos o **Holocron AI Compliance Analyst**. Utilizaremos o **Amazon Bedrock** (com modelos LLM como Claude ou Titan) para processar os logs coletados e gerar pareceres executivos em linguagem natural. A IA identificará padrões de acesso anômalos (User Behavior Analytics) e sugerirá remediações automáticas via AWS Lambda, transformando dados brutos em decisões estratégicas de segurança.

### 5. Arquitetura Técnica Detalhada (Deep Dive AWS)

Para este projeto final de Cloud Practitioner, selecionamos os serviços que formam o "Hardening" de segurança da AWS, garantindo que cada requisito da LGPD tenha uma contrapartida técnica robusta:

*   **AWS Identity and Access Management (IAM):**
    *   *Papel:* Implementação de RBAC (Role-Based Access Control) e Segregação de Funções (SoD).
    *   *Configuração:* Políticas JSON customizadas com negação implícita (Implicit Deny), MFA obrigatório para acesso ao console e uso de Roles para automação, eliminando chaves de acesso permanentes.
*   **Amazon Simple Storage Service (S3):**
    *   *Papel:* Repositório central de dados (Data Lake) e armazenamento de logs imutáveis.
    *   *Configuração:* Bloqueio de Acesso Público ativado globalmente, Versionamento para recuperação de desastres e S3 Object Lock para garantir que trilhas de auditoria não sejam deletadas.
*   **AWS Key Management Service (KMS):**
    *   *Papel:* Gestão centralizada do ciclo de vida das chaves de criptografia.
    *   *Configuração:* Uso de Customer Managed Keys (CMK) com rotação automática anual e políticas de chave estritas que limitam quem pode descriptografar os dados.
*   **AWS CloudTrail:**
    *   *Papel:* Registro pericial de todas as API Calls no ambiente.
    *   *Configuração:* Trail Multi-Region ativado, captura de Data Events (S3) e Management Events, com validação de integridade de arquivo de log ativada.
*   **AWS Config:**
    *   *Papel:* Auditoria de conformidade em tempo real.
    *   *Configuração:* Regras de conformidade para detectar buckets sem criptografia ou usuários remotos sem MFA, disparando remediações automáticas.
*   **Amazon CloudWatch:**
    *   *Papel:* Monitoramento e Observabilidade.
    *   *Configuração:* Alerta de faturamento (Billing Alarms) e métricas de tentativas de login falhas no IAM.

---

**Métricas de Desempenho Técnico:**
- **Segurança de Identidade:** 100% dos usuários administrativos com MFA físico/virtual.
- **Criptografia:** 0% de dados sensíveis armazenados em plain-text.
- **Auditabilidade:** Retenção configurada para 1.825 dias (5 anos) em camada S3 Glacier via Lifecycle.

---

**Recursos Visuais de Apoio:**
*   Diagramas de Arquitetura em `/02_ARCHITECTURE`.
*   Evidências de Logs e Screenshots em `/05_EVIDENCE`.
*   Script de Auditoria em `/04_CODE/validate_audit_logs.py`.

---
*Atenção: Este documento é propriedade intelectual do Grupo Holocron Sentinel - AWS re/Start 2025.*