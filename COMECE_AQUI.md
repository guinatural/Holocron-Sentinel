# Holocron Sentinel: Direcionamento do Projeto

Bem-vindo ao repositório do **Holocron Sentinel**. Este documento orienta avaliadores e recrutadores sobre a engenharia de segurança aplicada neste projeto de portfólio.

---

## Visão Geral do Arquiteto
Este projeto foi desenvolvido com foco no **Modelo de Responsabilidade Compartilhada**. Como proponente da solução e **AWS Certified Cloud Practitioner**, o objetivo foi automatizar a camada de responsabilidade do cliente ("Segurança NA Nuvem") para garantir conformidade plena com a LGPD.

### Problemas Resolvidos:
- **Exposição de Dados (PII):** Varredura automática via Amazon Macie.
- **Vulnerabilidade de Identidade:** MFA forçado via scripts Python.
- **Risco de Auditoria:** Trilhas do CloudTrail imutáveis e criptografadas.

---

## Pilares Técnicos

### 1. Automação via Boto3
Utilizei o SDK oficial da AWS para criar um kit de ferramentas DevOps que fiscaliza a infraestrutura em tempo real. Isso reduz o custo operacional e elimina o erro humano em configurações de segurança.

### 2. Governança com IA (Amazon Bedrock)
Integração de Inteligência Artificial para traduzir logs complexos em pareceres executivos. O Amazon Titan atua como um assistente de compliance, centralizando a tomada de decisão para CEOs e DPOs.

---

## Guia de Avaliação

| Pasta | Conteúdo de Valor |
| :--- | :--- |
| **04_CODE** | Scripts Python com lógica de auditoria e automação IAM. |
| **06_PRESENTATION** | Dashboard interativo para apresentação executiva. |
| **02_ARCHITECTURE** | Matriz de rastreabilidade (Artigos da LGPD vs Serviços AWS). |
| **05_EVIDENCE** | Exemplos de relatórios gerados pela IA e logs de conformidade. |

---

## Como Validar a Entrega?
1. Abra o arquivo [`index.html`](./06_PRESENTATION/index.html) para visualizar o Storytelling do projeto.
2. Revise o [`PROJECT_FINAL_PLAN.md`](./Projeto%20Final/PROJECT_FINAL_PLAN.md) para entender a metodologia ágil aplicada.
3. Analise o código em [`validate_audit_logs.py`](./04_CODE/validate_audit_logs.py) para confirmar a aplicação de boas práticas de Clean Code.

---
**Guilherme Barreto Gomes**
[AWS Certified Cloud Practitioner](https://www.credly.com/badges/9f28dc2a-d9b8-4774-ab9f-dfe3a8324ff0/public_url)
