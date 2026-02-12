# Relatório de Evidência: Auditoria de Conformidade (CloudTrail)

**Experimento:** Implementação de Rastreabilidade Centralizada (LGPD Art. 37)
**Data:** [Data de Hoje]
**Status:** Aguardando Evidências

---

## 1. Objetivo
Implementar um mecanismo de **"Audit Trail" (Trilha de Auditoria)** inviolável.
Para estar em conformidade com a LGPD, a empresa precisa provar *quem* acessou os dados, *quando* e *de onde*. Sem isso, não há defesa jurídica em caso de vazamento.

## 2. Configuração Realizada
*   **Serviço:** AWS CloudTrail + Amazon S3.
*   **Recurso:** Trail `holocron-master-trail` logando para `holocron-audit-logs`.
*   **Segurança:**
    *   ✅ Block Public Access (Ativado).
    *   ✅ Server-Side Encryption (Ativado).
    *   ✅ Log File Validation (Ativado - Garante integridade).

## 3. Evidência (Proof of Value)

### Evidência A: O "Cofre" Seguro (Bucket S3)
*O bucket onde os logs são armazenados está fechado para o público e criptografado.*
[COLE AQUI SEU PRINT 1 - LISTA DE BUCKETS COM CADEADO]

### Evidência B: O "Vigia" Ativo (CloudTrail)
*O serviço está logando ativamente em todas as regiões.*
[COLE AQUI SEU PRINT 2 - STATUS DO TRAIL 'LOGGING']

### Evidência C: A Prova Forense (JSON Log)
*Captura de uma ação administrativa (Ex: Criação de Usuário) registrada no log.*
```json
// Cole um trecho do seu JSON aqui se quiser, ou o print abaixo
```
[COLE AQUI SEU PRINT 3 - ARQUIVO JSON DO LOG]

---

## 4. Pitch para Entrevista
> "Neste lab, eu configurei não apenas um log, mas uma **Cadeia de Custódia**. Ativei a validação de integridade do CloudTrail, o que significa que se um hacker tentar apagar os rastros modificando o arquivo de log, o hash não baterá e saberemos. É assim que se garante conformidade real, não apenas checkboxes."
