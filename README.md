# 🛡️ Holocron Sentinel: Sistema de Conformidade LGPD na AWS

![AWS Status](https://img.shields.io/badge/AWS-re%2FStart-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Capstone%20Project-blue)
![Compliance](https://img.shields.io/badge/LGPD-Compliant-success)

> **Projeto Final (Capstone) - AWS re/Start**
> Solução de arquitetura em nuvem para governança de dados, auditoria e segurança, alinhada à Lei Geral de Proteção de Dados (13.709/2018).

---

## 🎯 O Problema
Empresas brasileiras enfrentam desafios críticos de **soberania de dados** e **rastreabilidade** (Art. 37 LGPD). Soluções on-premise são caras e difíceis de auditar. Este projeto implementa uma **"Glass Box Architecture"** (Caixa de Vidro), onde cada acesso a dados sensíveis é registrado, criptografado e monitorado.

## 🏗️ A Solução (Arquitetura)
O sistema é composto por 3 módulos principais:
1.  **Governança:** IAM RBAC com MFA obrigatório e Segregação de Funções.
2.  **Monitoramento:** CloudTrail e Config garantindo "Auditability by Design".
3.  **Defesa:** Criptografia KMS e Detecção de Ameaças (Logs de Acesso).

### 📂 Estrutura do Repositório
Este portfólio está organizado como um projeto de engenharia real:

*   **[`00-Master/`](./00-Master/)**: Visão Geral, Requisitos e Alinhamento com o Curso.
*   **[`01_SPRINTS/`](./01_SPRINTS/)**: Gestão Ágil (Backlog e Planejamento).
*   **[`02_ARCHITECTURE/`](./02_ARCHITECTURE/)**: Diagramas Técnicos e Mapeamento LGPD.
*   **[`04_CODE/`](./04_CODE/)**: Scripts de Automação (Python/Boto3) e Políticas JSON.
*   **[`05_EVIDENCE/`](./05_EVIDENCE/)**: Logs de Auditoria e Provas de Execução (Screenshots).
*   **[`06_PRESENTATION/`](./06_PRESENTATION/)**: Pitch Executivo para Stakeholders.

---

## 🚀 Como Executar (Simulação)

### Pré-requisitos
*   Python 3.8+
*   AWS CLI Configurado (`sa-east-1`)

### Auditoria de Logs
Para validar se os arquivos no S3 estão criptografados conforme o Art. 46:
```bash
python 04_CODE/validate_audit_logs.py
```

---

## 👨‍💻 Autor
Desenvolvido como parte do programa **AWS re/Start**.
*   **Foco:** Cloud Infrastructure & Security Compliance.
*   **Tech Stack:** EC2, S3, IAM, CloudWatch, Python.

---
*"Only through visibility can we achieve security."*
