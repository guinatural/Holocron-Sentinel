# Relatório de Evidência: Controle de Acesso e Identidade (IAM)

**Experimento:** Bloqueio Rígido de MFA (LGPD Art. 6 - Segurança)
**Data:** [Data de Hoje]
**Status:** Aguardando Evidências

---

## 1. Objetivo
Implementar o princípio de **"Secure Default"**.
Nenhum usuário, por mais privilegiado que seja (Admin), deve conseguir executar ações críticas se não estiver autenticado com duplo fator. Isso mitiga riscos de vazamento de credenciais (Phishing).

## 2. Configuração Realizada
*   **Recurso:** Customer Managed Policy `ForceMFA-Holocron`.
*   **Lógica:** Condicional `BoolIfExists: aws:MultiFactorAuthPresent == "false"`.
*   **Efeito:** `Deny` explícito em todas as ações exceto configuração de self-MFA.

## 3. Evidência (Proof of Value)

### Evidência A: A Política "Malvada"
*Criação da política no console usando o JSON do repositório.*
[COLE AQUI SEU PRINT 1 - TELA DA POLICY CRIADA]

### Evidência B: O Bloqueio (Security in Action)
*Usuário COM permissão de Admin, mas SEM MFA, tentando acessar o S3 e sendo bloqueado.*
[COLE AQUI SEU PRINT 2 - TELA DE ERRO 'ACCESS DENIED']

### Evidência C: Acesso Concedido
*O mesmo usuário, após configurar MFA e relogar, acessando os recursos normalmente.*
[COLE AQUI SEU PRINT 3 - LISTA DE BUCKETS VISÍVEL]

---

## 4. Pitch para Entrevista
> "Implementei uma política baseada em identidade que atua como um 'Firewall de Autenticação'. Diferente de apenas pedir para os usuários usarem MFA, eu **forcei tecnicamente** o uso. Isso garante que, mesmo se uma credencial vazar no GitHub, o atacante não consegue fazer nada sem o token físico."
