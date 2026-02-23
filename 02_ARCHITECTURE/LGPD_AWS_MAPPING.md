# Matriz de Conformidade: LGPD x AWS (Holocron Sentinel)

O Holocron Sentinel traduz a complexidade jurídica da Lei Geral de Proteção de Dados (13.709/2018) em controles técnicos automatizados na nuvem AWS.

---

## 1. Soberania de Dados (Artigo 3º)
*   **Requisito:** Aplicabilidade da lei para dados coletados ou tratados no território nacional.
*   **Controle Holocron:** Configuração de residência de dados (Data Residency) fixada na região **São Paulo (`sa-east-1`)**. Isso garante que a custódia física dos dados permaneça sob jurisdição brasileira primária.

## 2. Segurança e Proteção (Artigo 46)
*   **Requisito:** Medidas técnicas e administrativas aptas a proteger os dados de acessos não autorizados ou destruição.
*   **Controles Holocron:**
    *   **Criptografia Crítica:** Uso do AWS KMS com algoritmo AES-256 para dados em repouso.
    *   **Identidade Zero-Trust:** Implementação de MFA obrigatório e Políticas de Menor Privilégio (IAM) para garantir que apenas o necessário seja acessado.
    *   **Descoberta Automatizada:** Uso do Amazon Macie para encontrar dados sensíveis "esquecidos" em buckets comuns.

## 3. Registro e Auditoria (Artigo 37)
*   **Requisito:** O controlador deve manter registros das operações de tratamento de dados pessoais.
*   **Controle Holocron:** Ativação universal do **AWS CloudTrail** com armazenamento imutável no S3 (Object Lock). Isso cria uma trilha de evidências periciais que não pode ser apagada por invasores, vital para comprovar compliance em auditorias da ANPD.

## 4. Gestão de Incidentes (Artigo 48)
*   **Requisito:** Comunicação célere de incidentes de segurança ao titular e à autoridade nacional.
*   **Controles Holocron:**
    *   **Detecção via Machine Learning:** Uso do Amazon GuardDuty para identificar ataques em tempo real.
    *   **Inteligência Centralizada (IA):** Amazon Titan processa os alertas complexos e gera pareceres em linguagem natural para facilitar a comunicação imediata de incidentes, conforme exigido pela lei.

---

## Conclusão de Auditoria
Diferente de soluções manuais, o Holocron Sentinel integra estas quatro frentes em um único ecossistema automatizado. A empresa deixa de ser "vulnerável por omissão" e passa a ser "segura por design".

---
*Documento Técnico: Matriz de Rastreabilidade LGPD v1.0*
