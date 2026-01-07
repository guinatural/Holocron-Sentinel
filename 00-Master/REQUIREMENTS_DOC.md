# Documento de Especificação de Requisitos (Sistemática LGPD)

**Projeto:** Holocron Sentinel - Sistema de Conformidade LGPD na AWS
**Versão:** 1.0
**Responsável:** [Seu Nome]

---

## 1. 📝 Identificação do Problema

### Contexto
Empresas brasileiras enfrentam multas de até R$ 50 milhões por violações da LGPD. O problema não é apenas "vazamento de dados", mas a **falta de governança e rastreabilidade**. Atualmente, muitas empresas não sabem onde os dados pessoais estão armazenados nem quem os acessa.

### Justificativa
A implementação de uma arquitetura centralizada na AWS permite automatizar controles de segurança, reduzindo o risco humano e garantindo auditoria contínua a um custo fracionado de soluções on-premise.

### Stakeholders
*   **Encarregado de Dados (DPO):** Precisa de relatórios para a ANPD.
*   **Equipe de TI/DevOps:** Precisa de ferramentas que não atrapalhem o deploy.
*   **Titulares dos Dados (Clientes):** Precisam de transparência e portal de requisição.

---

## 2. 📋 Requisitos do Sistema

### 2.1 Requisitos Funcionais (O que o sistema FAZ)
*   **[RF-001] Ingestão Segura:** O sistema deve permitir o upload de arquivos contendo PII (Personally Identifiable Information) apenas via canais criptografados.
*   **[RF-002] Classificação Automática:** O sistema deve identificar cpf, e-mail e telefone em novos arquivos (Simulação Macie).
*   **[RF-003] Auditoria de Acesso:** O sistema deve registrar logs de todas as operações de leitura/escrita em dados sensíveis.
*   **[RF-004] Bloqueio Geográfico:** O sistema deve negar acessos oriundos de países fora da lista branca de compliance.
*   **[RF-005] Exclusão Lógica:** O sistema deve permitir a anonimização de dados mediante solicitação (Direito ao Esquecimento).

### 2.2 Requisitos Não-Funcionais (Como o sistema SE COMPORTA)
*   **[RNF-001] Segurança:** Criptografia em repouso (AES-256) é obrigatória para 100% dos dados.
*   **[RNF-002] Retenção:** Logs de auditoria devem ser imutáveis e retidos por 5 anos.
*   **[RNF-003] Disponibilidade:** O data lake deve ter durabilidade de 99.999999999% (S3 Standard).
*   **[RNF-004] Performance:** O tempo para indexação de novos arquivos de log deve ser inferior a 5 minutos.

---

## 3. 🎯 Definição de MVP vs Evolução

### MVP (Minimum Viable Product) - Entrega do Curso
*   Arquitetura Base (VPC, S3, IAM).
*   Logs Centralizados (CloudTrail).
*   Criptografia Básica (SSE-S3).
*   Dashboard de Conformidade (Simulado com AWS Config).

### Roadmap (Evolução V2)
*   Portal do Titular (Frontend Web).
*   Automação com Lambda para exclusão de dados.
*   Integração com Security Hub.
