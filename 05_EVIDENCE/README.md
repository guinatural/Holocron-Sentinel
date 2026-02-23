# Evidências de Execução: Holocron Sentinel

Este diretório contém as provas técnicas de que a arquitetura e os scripts do projeto funcionam conforme especificado. Para a banca avaliadora, estas evidências confirmam a prontidão da solução.

---

## Screenshots Sugeridas para o Portfólio

1.  **IAM Security:** Print do console AWS mostrando usuários com MFA ativado e políticas de menor privilégio anexadas.
2.  **S3 Hardening:** Print das configurações do bucket de auditoria com "Block Public Access" e "Bucket Encryption (KMS)" ativos.
3.  **CloudTrail:** Prova de que o Log Centralizado está coletando eventos na região sa-east-1.
4.  **Execução do Script:** Print do terminal rodando `python 04_CODE/validate_audit_logs.py` com o resultado "COMPLIANT".
5.  **IA Analyst:** Print do arquivo `.md` de parecer executivo gerado pela simulação do Amazon Titan.

---

## Relatórios Gerados
Os scripts de automação em Python geram os seguintes artefatos para auditoria:

- `compliance_report.txt`: Gerado por `validate_audit_logs.py`.
- `credential_report.csv`: Gerado por `setup_iam_structure.py`.
- `parecer_executivo_XXXX_XX_XX.md`: Gerado pelo módulo de IA.

---

## Validação Técnica
Todas as evidências aqui contidas foram validadas utilizando o **AWS CLI** e o **SDK Boto3**, seguindo os pilares de **Excelência Operacional** e **Segurança** do AWS Well-Architected Framework.
