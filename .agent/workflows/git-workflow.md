---
description: Workflow para versionamento e publicação no GitHub
---

# Git Workflow — Holocron Sentinel

Este documento descreve o processo de versionamento e publicação do projeto no GitHub.

---

## Pré-requisitos

### 1. Instalar Git
- **Download:** [https://git-scm.com/downloads](https://git-scm.com/downloads)
- **Instalação Windows:** Aceitar configurações padrões
- **Verificação:** Abrir novo terminal e executar `git --version`

### 2. Configurar Identidade Git (Primeira vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

---

## Setup Inicial do Repositório

### 1. Inicializar Repositório Local

```bash
# Navegar até a pasta do projeto
cd "c:\Users\barre\AWS-reStart-Compliance-Portfolio\AWS-re-Start\P - Holocron-Sentinel"

# Inicializar Git
git init
```

### 2. Adicionar Arquivos ao Staging

```bash
# Adicionar todos os arquivos
git add .

# Ou adicionar arquivos específicos
git add 00-Master/AWS_SECURITY_SETUP.md
git add 00-Master/PROJECT_OVERVIEW.md
git add 00-Master/FOLDER_STRUCTURE.md
```

### 3. Criar Primeiro Commit

```bash
git commit -m "docs: Add AWS Security Setup initial documentation

- Created AWS_SECURITY_SETUP.md with comprehensive security checklist
- Updated PROJECT_OVERVIEW.md with security setup reference
- Updated FOLDER_STRUCTURE.md to include security documentation
- Follows AWS Well-Architected Framework Security Pillar

Related to: Holocron Sentinel Phase 1 - Security Foundation"
```

---

## Criar Repositório no GitHub

### Opção A: Via GitHub Web Interface

1. Acessar [https://github.com/new](https://github.com/new)
2. **Repository name:** `holocron-sentinel-lgpd-aws`
3. **Description:** "Sistema de Conformidade LGPD na AWS — Projeto Final AWS re/Start"
4. **Visibility:** Public (para portfolio) ou Private
5. **NÃO** inicializar com README (já temos um)
6. Clicar em **Create repository**

### Opção B: Via GitHub CLI (se instalado)

```bash
gh repo create holocron-sentinel-lgpd-aws --public --source=. --remote=origin
```

---

## Conectar Repositório Local ao GitHub

```bash
# Adicionar remote origin (substituir SEU-USERNAME)
git remote add origin https://github.com/SEU-USERNAME/holocron-sentinel-lgpd-aws.git

# Renomear branch para main (padrão atual do GitHub)
git branch -M main

# Fazer push inicial
git push -u origin main
```

---

## Workflow Diário de Commits

### Padrão de Mensagens (Conventional Commits)

```bash
# Documentação
git commit -m "docs: descrição da mudança"

# Nova funcionalidade
git commit -m "feat: descrição da feature"

# Correção de bug
git commit -m "fix: descrição da correção"

# Refatoração
git commit -m "refactor: descrição da refatoração"

# Testes
git commit -m "test: descrição dos testes"

# Arquitetura
git commit -m "arch: descrição da mudança arquitetural"
```

### Exemplo Completo de Ciclo de Trabalho

```bash
# 1. Verificar status
git status

# 2. Adicionar mudanças
git add arquivo1.md arquivo2.py

# 3. Commit com mensagem descritiva
git commit -m "docs: Update IAM security model documentation"

# 4. Enviar para GitHub
git push origin main
```

---

## Boas Práticas

1. **Commits Atômicos:** Cada commit deve representar UMA mudança lógica.
2. **Mensagens Descritivas:** Explicar o "o quê" e o "porquê", não o "como".
3. **Commits Frequentes:** Melhor 5 commits pequenos que 1 commit gigante.
4. **Revisar Antes de Commitar:** Sempre usar `git status` e `git diff` antes.

---

## Estrutura de Branches (Opcional para Projeto Solo)

Se quiser trabalhar com branches:

```bash
# Criar branch de feature
git checkout -b feature/cloudtrail-setup

# Fazer mudanças e commits
git add .
git commit -m "feat: Configure CloudTrail audit logging"

# Voltar para main e fazer merge
git checkout main
git merge feature/cloudtrail-setup

# Deletar branch após merge
git branch -d feature/cloudtrail-setup
```

---

## Comandos de Emergência

### Desfazer Último Commit (SEM perder mudanças)

```bash
git reset --soft HEAD~1
```

### Ver Histórico de Commits

```bash
git log --oneline --graph --decorate
```

### Ver Mudanças Antes de Commitar

```bash
git diff
```

---

## Autenticação GitHub

### Opção 1: Personal Access Token (Recomendado)

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Selecionar escopo: `repo` (acesso completo a repositórios)
4. Usar o token como senha quando fazer `git push`

### Opção 2: SSH Keys

```bash
# Gerar chave SSH
ssh-keygen -t ed25519 -C "seu-email@exemplo.com"

# Adicionar chave ao ssh-agent
ssh-add ~/.ssh/id_ed25519

# Copiar chave pública para GitHub
cat ~/.ssh/id_ed25519.pub
# Colar em: GitHub → Settings → SSH and GPG keys → New SSH key
```

---

## README Badge para Portfolio

Adicionar ao `README.md` para profissionalismo:

```markdown
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)
![LGPD](https://img.shields.io/badge/Compliance-LGPD-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
```
