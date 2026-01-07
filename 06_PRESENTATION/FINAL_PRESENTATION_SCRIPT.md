# Roteiro da Apresentação Final (15 Minutos)

**Público:** Banca Avaliadora AWS re/Start
**Objetivo:** Demonstrar competência técnica e soft skills de gestão.

---

## 1. Abertura e Identidade (2 min)
*   **Slide 1:** Capa (Holocron Sentinel - Sistema de Conformidade LGPD).
*   **Discurso:**
    *   "Bom dia. Meu nome é [Nome] e hoje apresento o Holocron Sentinel."
    *   "Mais do que um projeto de infraestrutura, é uma resposta à crise de privacidade de dados no Brasil."
    *   "Meu papel: Arquiteto de Cloud e Engenheiro de Segurança."

## 2. Identificação do Problema (3 min)
*   **Slide 2:** O Cenário LGPD.
*   **Contexto:** Empresas multadas em milhões por falta de governança.
*   **Problema:** "Como garantir que uma empresa pequena tenha segurança de nível bancário sem estourar o orçamento?"
*   **Justificativa:** A nuvem AWS democratiza a segurança (Pay-as-you-go).

## 3. Engenharia de Requisitos (3 min)
*   **Slide 3:** Requisitos Funcionais e Não-Funcionais (Mostrar arquivo `REQUIREMENTS_DOC.md`).
*   **Destaque:**
    *   RF-003: Auditoria de Acesso (Art. 37 LGPD).
    *   RNF-001: Criptografia Obrigatória (Art. 46 LGPD).
*   **MVP:** "Focamos na Fase 1: Fundação de Governança."

## 4. Planejamento Ágil (2 min)
*   **Slide 4:** O Backlog e Sprints (Mostrar arquivo `BACKLOG_SPRINTS.md`).
*   **Visual:** Mostrar print do Trello/Jira.
*   **Narrativa:** "Trabalhamos em Sprints de 1 semana. A Sprint 1 focou em IAM e Segurança. A Sprint 2 em Auditoria."

## 5. Solução Técnica e Arquitetura (3 min)
*   **Slide 5:** Diagrama de Arquitetura (Mostrar `02_ARCHITECTURE`).
*   **Explicação:**
    *   "Aqui vemos a VPC isolada..."
    *   "O bucket S3 com criptografia KMS..."
    *   "O CloudTrail vigiando tudo..."

## 6. Evidência e Conclusão (2 min)
*   **Slide 6:** "Show me the code" (Mostrar script Python `validate_audit_logs.py`).
*   **Encerramento:**
    *   "O Holocron Sentinel não é apenas um lab, é um sistema pronto para escalar."
    *   "Obrigado. Aberto para perguntas."
