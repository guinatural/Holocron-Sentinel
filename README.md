# Holocron Sentinel: Governança Inteligente e Conformidade LGPD na AWS

![AWS Status](https://img.shields.io/badge/AWS-re%2FStart%20%2B%20IA-orange)
![Compliance](https://img.shields.io/badge/LGPD-Artigos%203%2C%206%2C%2018%2C%2037%2C%2046%2C%2048-success)
![Cost](https://img.shields.io/badge/Cost-80%25%20Reduction-blueviolet)

> **Projeto Final (Capstone) - AWS re/Start + Inteligência Artificial**
> Uma solução "Ready for ANPD" que automatiza a segurança na nuvem, reduz custos operacionais e utiliza IA nativa para centralizar a tomada de decisão.

---

## O Diferencial Estratégico
O **Holocron Sentinel** não é apenas uma infraestrutura; é um ecossistema de segurança por design. 
- **Centralização:** IA **Amazon Titan** interpreta sinais do **Macie** e **GuardDuty**.
- **Eficiência:** Redução de **80% nos custos** em comparação a soluções on-premise.
- **Responsabilidade:** Fecha o gap do **Modelo de Responsabilidade Compartilhada**, protegendo o empresário de multas da LGPD.

---

## Arquitetura "Glass Box" (Nativa AWS)
Nossa stack utiliza o **AWS Well-Architected Framework** como bússola técnica:

1.  **Fundação IAM:** Identidade Zero-Trust com MFA Enforcement e Least Privilege.
2.  **Auditabilidade (Art. 37):** Logs imutáveis via **CloudTrail** e **S3 Object Lock**.
3.  **Proteção de Dados (Art. 46):** Criptografia de ponta a ponta com **AWS KMS (AES-256)**.
4.  **Cérebro de IA (Art. 48):** **Amazon Bedrock (Titan)** gerando pareceres executivos automáticos.

---

## Estrutura do Ecossistema
Este repositório está organizado para demonstrar prontidão técnica e gerencial:

*   **[`04_CODE/`](./04_CODE/)**: O motor do projeto em **Python/Boto3** (Identity, Auditoria e Alertas).
*   **[`02_ARCHITECTURE/`](./02_ARCHITECTURE/)**: Mapeamento detalhado LGPD x AWS e Diagramas.
*   **[`06_PRESENTATION/`](./06_PRESENTATION/)**: Dashboard interativo premium (`index.html`) e Roteiro Pitch de 15min.
*   **[`Projeto Final/`](./Projeto%20Final/)**: Plano de projeto individual alinhado com as metas da Escola da Nuvem.
*   **[`05_EVIDENCE/`](./05_EVIDENCE/)**: Provas técnicas de execução e relatórios de auditoria.

---

## Como Navegar no Projeto?
1.  **Visão Executiva:** Abra o arquivo [`COMECE_AQUI.md`](./COMECE_AQUI.md).
2.  **Apresentação Interativa:** Execute o [`06_PRESENTATION/index.html`](./06_PRESENTATION/index.html) no seu navegador (F11 para tela cheia).
3.  **Código Vivo:** Explore os scripts em [`04_CODE/scripts/`](./04_CODE/scripts/) para ver a automação Boto3 em ação.

---

## Autor
**Guilherme Barreto Gomes**
*Arquiteto de Soluções Cloud & Especialista em Compliance de Dados*

---
*"Segurança não é um produto, é um processo automatizado."*
