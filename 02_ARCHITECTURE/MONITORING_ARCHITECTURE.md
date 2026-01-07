# Arquitetura de Monitoramento e Auditoria (Módulo LGPD: Art. 37)

## 🏗️ Visão Geral da Arquitetura
Este módulo implementa o **Requisito RF-003 (Auditoria de Acesso)** do Sistema de Conformidade LGPD. Ele garante que todas as operações nos servidores de aplicação sejam registradas e auditáveis, atendendo ao **Artigo 37 da LGPD** (Obrigação de registro de operações).

## 🧩 Componentes da Solução

### 1. Coleta Avançada (CloudWatch Agent)
As métricas padrão do EC2 (Hypervisor level) são insuficientes para uma visão operacional completa (cegas para Memória e Disco).
- **Componente**: Amazon CloudWatch Agent.
- **Instalação**: Gerenciada via **AWS Systems Manager (Run Command)** para garantir consistência e evitar acesso manual (SSH).
- **Configuração**: Armazenada centralmente no **SSM Parameter Store** (`Monitor-Web-Server`).
    - *Infrastructure as Code*: A configuração não fica "solta" na instância.

### 2. Centralização de Logs
Os logs não devem morrer com a instância.
- **Log Groups**:
    - `HttpAccessLog`: Rastreamento de acessos ao servidor web.
    - `HttpErrorLog`: Diagnóstico de falhas de aplicação.
- **Fluxo**: EC2 File System -> CloudWatch Agent -> CloudWatch Logs Service.

### 3. Log-Based Metrics & Alarmes
Transformação de dados não estruturados (logs) em inteligência acionável.
- **Filtro Métrico**: `[ip, id, user, timestamp, request, status_code=404, size]`
- **Alarme**: "404 Errors" (> 5 erros em 1 minuto).
- **Ação**: Notificação via SNS (Email) para resposta a incidentes de segurança (ex: Varredura de vulnerabilidades/Directory Traversal).

### 4. Eventos em Tempo Real (EventBridge)
Monitoramento de ciclo de vida da infraestrutura.
- **Regra**: `EC2 Instance State-change Notification` (Stopped/Terminated).
- **Objetivo**: Detectar desligamentos não autorizados ou falhas críticas instantaneamente, sem aguardar pooling de métricas.

### 5. Compliance Contínuo (AWS Config)
Garantia de governança e padrões.
- **Regras Ativas**:
    1. `required-tags`: Garante que todo recurso tenha a tag `project`. (Governança de Custos).
    2. `ec2-volume-inuse-check`: Detecta volumes EBS "órfãos" gerando custos desnecessários. (FinOps).

---

## 📐 Diagrama de Fluxo de Dados

```mermaid
graph TD
    subgraph "EC2 Instance (Web Server)"
        A[Application Logs] -->|Read by| B[CloudWatch Agent]
        C[OS Metrics (Mem/Disk)] -->|Read by| B
    end

    subgraph "AWS Systems Manager"
        D[Parameter Store] -->|Config JSON| B
    end

    B -->|Push| E[CloudWatch Logs]
    B -->|Push| F[CloudWatch Metrics]

    E -->|Metric Filter| G[Alarm: 404 Errors]
    G -->|Trigger| H[SNS Topic]

    I[EC2 State Change] -->|Event| J[EventBridge Rule]
    J -->|Trigger| H

    K[AWS Config] -->|Audit| L[Compliance Dashboard]
```

## 🛡️ Justificativa de Conformidade (LGPD)
Esta arquitetura resolve o gap de **Rastreabilidade**.
*   **Art. 37 (Registro):** Logs de acesso (`HttpAccessLog`) provam *quem* acessou *o quê*.
*   **Art. 46 (Segurança):** O Alarme de Erros 404 atua como um *Detect* no framework de segurança, identificando varreduras maliciosas antes que dados vazem.
*   **Imutabilidade:** O envio para o CloudWatch Logs garante que um atacante não possa apagar seus rastros localmente na máquina (Anti-Forensics).
