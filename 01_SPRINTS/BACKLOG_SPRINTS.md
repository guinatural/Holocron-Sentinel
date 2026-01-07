# Planejamento Ágil: Backlog & Sprints

**Metodologia:** Scrum Adaptado (Sprints de 1 Semana)
**Ferramenta de Gestão:** Trello/GitHub Projects (Simulado)

---

## 📌 Product Backlog (Priorizado)

### Épico 1: Governança e Segurança (Core)
1.  **[Alta]** Configurar AWS Organizations e separar contas (Prod/Audit).
2.  **[Alta]** Implementar Bucket S3 com bloqueio de acesso público e criptografia.
3.  **[Alta]** Definir Policies IAM para segregação de funções (Admin vs Auditor).
4.  **[Média]** Ativar CloudTrail Multi-Region.

### Épico 2: Monitoramento e Resposta
5.  **[Alta]** Configurar AWS Config para monitorar buckets não criptografados.
6.  **[Média]** Criar Alertas SNS para alterações no IAM (Criação de usuários).
7.  **[Baixa]** Dashboard CloudWatch para volumetria de logs.

### Épico 3: Portal de Conformidade (Fase 2)
8.  **[Baixa]** Desenhar arquitetura Serverless para Portal do Titular.
9.  **[Baixa]** API Gateway Mock para receber pedidos de exclusão.

---

## 🏃 Sprint Planning

### Sprint 1: Fundação de Segurança (Semana 1)
**Objetivo:** Garantir que o ambiente de armazenamento e identidade esteja 100% compliance com o Art. 46 da LGPD.

| ID | Tarefa | Responsável | Status |
|----|--------|-------------|--------|
| T-01 | Desenho da Arquitetura de Rede (VPC) | [Eu] | Done |
| T-02 | Configuração do Bucket "Data Lake" (S3) | [Eu] | In Progress |
| T-03 | Criação de Grupos IAM e MFA Enforcement | [Eu] | **Code Ready** (Lab 02) |
| T-04 | Documentação de Requisitos (RF/RNF) | [Eu] | **Done** |

### Sprint 2: Auditoria e Evidência (Semana 2)
**Objetivo:** Implementar os "olhos" do sistema (Logs e Config Rules) para gerar o relatório final.

| ID | Tarefa | Responsável | Status |
|----|--------|-------------|--------|
| T-05 | Ativar CloudTrail e validar logs no S3 | [Eu] | **Code Ready** (Lab 01) |
| T-06 | Criar Regras do AWS Config (Required Tags) | [Eu] | To Do |
| T-07 | Simular Incidente (Acesso não autorizado) | [Eu] | To Do |
| T-08 | Montar Apresentação Final (Pitch) | [Eu] | **Done** (Script Criado) |

---

## 📸 Evidência de Gestão
> *Nota: Para o print do board, sugere-se criar um quadro gratuito no Trello com estas colunas (To Do, Doing, Done) e os cards acima.*
