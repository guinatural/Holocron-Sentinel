# Projeto Final: Holocron Sentinel — Segurança e Conformidade na Nuvem
## Módulo 1: AWS re/Start + Inteligência Artificial

**Grupo:** Holocron Sentinel  
**Ano:** 2025  
**Integrante (Apresentação Individual):** Guilherme Barreto Gomes  

---

## 1. Identificação do Problema

**Ideia do Projeto:** Holocron Sentinel — Sistema Automatizado de Governança de Dados Sensíveis e Auditoria para Conformidade LGPD.

**Descrição do Problema:**
O cenário corporativo brasileiro enfrenta um desafio crítico com a Lei Geral de Proteção de Dados (LGPD). Pequenas e médias empresas operam com "cegueira técnica": possuem dados de clientes (PII) na nuvem, mas não sabem quem os acessa nem se estão protegidos por criptografia. Auditorias da ANPD podem ocorrer a qualquer momento, e a falta de registros (logs) imutáveis pode resultar em multas de até R$ 50 milhões. Atualmente, as soluções de segurança são caras, manuais e lentas, dependendo de especialistas humanos para conferir logs exaustivamente.

**Stakeholders:**
*   **Donos de Empresas (CEOs):** Buscam redução de risco jurídico e continuidade do negócio.
*   **Diretores de TI (CTOs):** Precisam de visibilidade total da infraestrutura sem aumentar o quadro de funcionários.
*   **Encarregado de Dados (DPOs):** Necessitam de evidências rápidas e automáticas para comprovar compliance à ANPD.
*   **Titulares dos Dados (Clientes):** Exigem que sua privacidade seja preservada por design.

**Justificativa:**
O Holocron Sentinel automatiza a segurança desde o design. Diferente de processos manuais lentos, nossa solução detecta violações em milissegundos. Ao utilizar a infraestrutura nativa da AWS, garantimos que a empresa esteja pronta para auditorias instantâneas, com um **custo 80% menor** que soluções tradicionais *on-premise*, utilizando IA para centralizar a tomada de decisão.

---

## 2. Levantamento de Requisitos

**Requisitos Funcionais (O que o sistema faz):**
*   **[RF-001] Detecção de PII:** Identificar CPFs e documentos sensíveis em buckets S3.
*   **[RF-002] Monitoramento de Acesso:** Registrar todas as chamadas de API feitas no ambiente.
*   **[RF-003] Criptografia de Dados:** Garantir que 100% dos dados em repouso utilizem AES-256.
*   **[RF-004] Geração de Parecer:** Criar relatórios executivos automáticos sobre o status de conformidade.

**Requisitos Não Funcionais (Como o sistema se comporta):**
*   **Segurança (Pilar #1):** Utilizar criptografia em trânsito (TLS) e em repouso (KMS).
*   **Disponibilidade:** A solução deve operar de forma ininterrupta em sa-east-1.
*   **Auditabilidade:** Logs devem ser imutáveis e retidos por no mínimo 5 anos.
*   **Economia:** Priorizar serviços serverless para otimização de custos (Pay-as-you-go).

**MVP (Produto Mínimo Viável):**
Uma infraestrutura segura na AWS composta por:
1.  **Fundação IAM:** Usuários com menor privilégio e MFA forçado.
2.  **Trilha de Auditoria:** CloudTrail ativo gerando logs no S3.
3.  **Segurança de Dados:** Buckets S3 com *Block Public Access* e Criptografia.
4.  **Automação de Auditoria:** Script Python de validação de logs.

**Evolução (Módulo IA):**
Implementação do Cérebro Central via **Amazon Bedrock (Titan)** integrando **Amazon Macie** (descoberta de dados) e **Amazon GuardDuty** (ameaças), centralizando a governança no **AWS Security Hub**.

---

## 3. Planejamento Ágil

**Backlog de Tarefas:**
1.  Pesquisa técnica sobre artigos da LGPD (Art. 37, 46, 48).
2.  Configuração da infraestrutura de Identidade (IAM & MFA).
3.  Implementação do Data Lake Seguro (S3 & KMS).
4.  Ativação da Trilha de Auditoria Universal (CloudTrail).
5.  Desenvolvimento do script de fiscalização automatizada.
6.  Integração do protótipo de IA para análise de logs.
7.  Criação do Painel de Apresentação Final.

**Sprints (Ciclos de 1 Semana):**
*   **Sprint 1:** Planejamento, Requisitos e Desenho da Arquitetura.
*   **Sprint 2:** Implementação do Hardening IAM e S3 Secure.
*   **Sprint 3:** Ativação dos logs de conformidade e Script de Auditoria.
*   **Sprint 4:** Finalização do Storytelling e Preparação da Apresentação Individual.

**Quadro (Board):**
Utilizamos o GitHub Projects para gerir as tarefas, garantindo que cada requisito LGPD fosse mapeado para uma tarefa técnica específica.
*(Ver print do board na pasta 01_SPRINTS)*

---

## 4. Arquitetura de Excelência AWS (Deep Dive)

Nossa solução centraliza a segurança na nuvem utilizando os pilares do **AWS Well-Architected**:

*   **IA Centralizada:** O **Amazon Titan** processa dados do **Macie** e **GuardDuty**, centralizando alertas em um único local.
*   **Zero-Trust:** Nenhum acesso é permitido sem MFA e validação via IAM Policy restritiva.
*   **Imutabilidade:** O uso de **S3 Object Lock** impede a deleção de registros de auditoria por invasores.
*   **Eficiência de Custo:** Ao rodar apenas sob demanda, o Holocron custa apenas frações de um servidor de segurança tradicional.

---
*Assinado: Guilherme Barreto Gomes — Arquiteto de Soluções em Cloud*