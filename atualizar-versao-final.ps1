# Holocron Sentinel - GitHub Update Script
# Version: 1.0

Write-Host "Holocron Sentinel - Atualização Versão Final" -ForegroundColor Cyan
Write-Host "GitHub: https://github.com/guinatural/Holocron-Sentinel" -ForegroundColor Gray
Write-Host "========================================`n" -ForegroundColor Cyan

# Verificar instalação do Git
Write-Host "Verificando pré-requisitos..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "Git encontrado: $gitVersion`n" -ForegroundColor Green
}
catch {
    Write-Host "ERRO: Git não instalado!" -ForegroundColor Red
    Write-Host "Instale em: https://git-scm.com/downloads" -ForegroundColor Yellow
    Write-Host "Após instalar, reinicie o PowerShell.`n"
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Configurar diretório do projeto
$projectDir = "c:\Users\barre\AWS-reStart-Compliance-Portfolio\AWS-re-Start\P - Holocron-Sentinel"
Set-Location $projectDir
Write-Host "Diretório: $projectDir`n" -ForegroundColor Cyan

# Verificar repositório Git
$isGitRepo = Test-Path ".git"

if (-not $isGitRepo) {
    Write-Host "Configurando repositório Git..." -ForegroundColor Yellow
    git init
    git branch -M main
    git remote add origin https://github.com/guinatural/Holocron-Sentinel.git
    Write-Host "Repositório configurado!`n" -ForegroundColor Green
}
else {
    Write-Host "Repositório existente detectado`n" -ForegroundColor Green
    
    $remoteUrl = git remote get-url origin 2>$null
    if ($remoteUrl -ne "https://github.com/guinatural/Holocron-Sentinel.git") {
        Write-Host "Atualizando URL do repositório..." -ForegroundColor Yellow
        git remote set-url origin https://github.com/guinatural/Holocron-Sentinel.git
        Write-Host "Remote atualizado!`n" -ForegroundColor Green
    }
    else {
        Write-Host "Remote configurado: $remoteUrl`n" -ForegroundColor Green
    }
}

# Exibir status
Write-Host "Status do repositório:" -ForegroundColor Cyan
git status --short
Write-Host ""

# Menu de opções
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Opções de Atualização:" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  [1] Atualização Completa (Versão Final 1.0)" -ForegroundColor Green
Write-Host "  [2] Atualização Incremental (Múltiplos Commits)" -ForegroundColor Yellow
Write-Host "  [3] Verificar Diferenças" -ForegroundColor Blue
Write-Host "  [4] Sincronizar (Pull + Push)" -ForegroundColor Magenta
Write-Host "  [5] Ver Histórico" -ForegroundColor Cyan
Write-Host "  [6] Cancelar" -ForegroundColor Red
Write-Host "========================================`n" -ForegroundColor Cyan

$choice = Read-Host "Escolha uma opção"

switch ($choice) {
    "1" {
        Write-Host "`nCriando atualização completa...`n" -ForegroundColor Green
        
        git add .
        
        $currentDate = Get-Date -Format "yyyy-MM-dd"
        $currentTime = Get-Date -Format "HH:mm"
        
        $commitMessage = @"
feat: Release Holocron Sentinel v1.0 - Final Production Version

PROJETO FINALIZADO - AWS re/Start Capstone Project

Esta atualização marca a conclusão do Holocron Sentinel,
sistema completo de conformidade LGPD em infraestrutura AWS.

Atualizações Principais:

Documentação Completa
- README.md otimizado para recrutadores
- Guias de execução detalhados
- Documentação técnica em 00-Master/
- Orientações de publicação

Arquitetura
- Diagramas em 02_ARCHITECTURE/
- Mapeamento LGPD (Art. 37, 46, 48)
- Glass Box Architecture documentada
- AWS Well-Architected Framework alignment

Implementação Técnica
- Scripts Python em 04_CODE/
- Validação criptografia S3 (Art. 46)
- Auditoria CloudTrail automatizada
- Políticas IAM com MFA

Evidências
- Screenshots em 05_EVIDENCE/
- Logs de auditoria
- Testes documentados
- Provas de conformidade

Apresentação
- Materiais em 06_PRESENTATION/
- Portfolio em 07_PORTFOLIO/
- Templates para divulgação
- Guias de publicação

Ferramentas
- Scripts PowerShell
- Checklists de finalização
- Workflows automatizados

Stack Técnica:

Cloud Infrastructure:
- AWS IAM (RBAC + MFA)
- Amazon S3 (encryption at rest)
- AWS CloudTrail (audit logging)
- AWS KMS (key management)
- AWS Config (compliance validation)
- Amazon CloudWatch (monitoring)

Development:
- Python 3.8+ (automation)
- Boto3 SDK (AWS integration)
- PowerShell (deployment scripts)

Compliance:
- LGPD (Lei 13.709/2018)
- Data residency: sa-east-1
- Zero-trust architecture

Métricas:
- Código: ~2.500+ linhas
- Documentos: 30+ arquivos
- Scripts: 15+ arquivos
- Evidências: 20+ screenshots
- Sprints: 5 sprints ágeis
- Duração: 10 semanas

Status: PRODUCTION READY

Desenvolvedor: Guilherme Natural
AWS re/Start - Turma 2026
Especialização: Cloud Security & Compliance

Release Information:
Version: 1.0.0 (Final Release)
Data: $currentDate às $currentTime
Status: Complete and Ready for Presentation

"Only through visibility can we achieve security."
Holocron Sentinel Project Motto

Desenvolvido com excelência, documentado com clareza, entregue com orgulho.
"@
        
        git commit -m $commitMessage
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`nCommit criado com sucesso!" -ForegroundColor Green
            Write-Host "Preparando push para GitHub...`n" -ForegroundColor Cyan
            
            $confirmPush = Read-Host "Fazer push agora? (S/N)"
            
            if ($confirmPush -eq "S" -or $confirmPush -eq "s") {
                Write-Host "`nEnviando para GitHub..." -ForegroundColor Yellow
                Write-Host "Você precisará autenticar`n" -ForegroundColor Gray
                
                git push origin main
                
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "`nATUALIZAÇÃO CONCLUÍDA!" -ForegroundColor Green
                    Write-Host "Verifique: https://github.com/guinatural/Holocron-Sentinel`n" -ForegroundColor Cyan
                }
                else {
                    Write-Host "`nErro ao fazer push. Tente novamente.`n" -ForegroundColor Yellow
                }
            }
        }
        else {
            Write-Host "`nErro ao criar commit`n" -ForegroundColor Red
        }
    }
    
    "2" {
        Write-Host "`nCriando atualização incremental...`n" -ForegroundColor Yellow
        
        $currentDate = Get-Date -Format "yyyy-MM-dd"
        
        Write-Host "[1/5] Documentação..." -ForegroundColor Cyan
        git add README.md 00-Master/ GUIA_*.md 2>$null
        git commit -m "docs: Update project documentation to final version

- Enhanced README with professional formatting
- Updated master documentation
- Added quick start guides
- Improved technical clarity

Project Phase: Documentation Update
Date: $currentDate" 2>$null
        
        Write-Host "[2/5] Código e automação..." -ForegroundColor Cyan
        git add 04_CODE/ *.ps1 2>$null
        git commit -m "feat: Add automation scripts and code updates

- Enhanced Python validation scripts
- Added PowerShell automation
- Improved error handling
- Updated boto3 implementations

Project Phase: Code Enhancement
Date: $currentDate" 2>$null
        
        Write-Host "[3/5] Arquitetura e evidências..." -ForegroundColor Cyan
        git add 02_ARCHITECTURE/ 05_EVIDENCE/ 2>$null
        git commit -m "arch: Update architecture and evidence

- Refined architecture documentation
- Added execution evidence
- Updated compliance proofs
- Enhanced diagrams

Project Phase: Architecture & Evidence
Date: $currentDate" 2>$null
        
        Write-Host "[4/5] Apresentação e portfolio..." -ForegroundColor Cyan
        git add 06_PRESENTATION/ 07_PORTFOLIO/ TEMPLATES_*.md CHECKLIST_*.md 2>$null
        git commit -m "docs: Finalize presentation materials

- Completed presentation slides
- Added portfolio documentation
- Created templates
- Added checklists

Project Phase: Presentation Ready
Date: $currentDate" 2>$null
        
        Write-Host "[5/5] Finalização..." -ForegroundColor Cyan
        git add . 2>$null
        git commit -m "polish: Final touches and version 1.0

- Verified documentation links
- Optimized file structure
- Added guides
- Ensured consistency

Status: READY FOR PRESENTATION

AWS re/Start - Holocron Sentinel v1.0
Date: $currentDate" 2>$null
        
        Write-Host "`nCommits criados!`n" -ForegroundColor Green
        
        $confirmPush = Read-Host "Fazer push agora? (S/N)"
        
        if ($confirmPush -eq "S" -or $confirmPush -eq "s") {
            Write-Host "`nEnviando para GitHub..." -ForegroundColor Yellow
            git push origin main
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "`nATUALIZAÇÃO CONCLUÍDA!" -ForegroundColor Green
                Write-Host "Verifique: https://github.com/guinatural/Holocron-Sentinel`n" -ForegroundColor Cyan
            }
        }
    }
    
    "3" {
        Write-Host "`nVerificando diferenças...`n" -ForegroundColor Blue
        git status
        Write-Host "`nArquivos modificados:" -ForegroundColor Cyan
        git diff --stat
        Write-Host "`nDica: Use 'git diff arquivo' para detalhes`n" -ForegroundColor Yellow
    }
    
    "4" {
        Write-Host "`nSincronizando com GitHub...`n" -ForegroundColor Magenta
        Write-Host "Baixando atualizações..." -ForegroundColor Cyan
        git pull origin main
        Write-Host "`nEnviando atualizações locais..." -ForegroundColor Cyan
        git push origin main
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`nSincronização completa!`n" -ForegroundColor Green
        }
    }
    
    "5" {
        Write-Host "`nHistórico de Commits:`n" -ForegroundColor Cyan
        git log --oneline --graph --decorate --all -20
        Write-Host ""
    }
    
    "6" {
        Write-Host "`nOperação cancelada.`n" -ForegroundColor Yellow
        exit 0
    }
    
    default {
        Write-Host "`nOpção inválida!`n" -ForegroundColor Red
        exit 1
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Próximos Passos:" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  1. Verificar repositório no GitHub" -ForegroundColor Yellow
Write-Host "     https://github.com/guinatural/Holocron-Sentinel" -ForegroundColor Gray
Write-Host "  2. Criar Release v1.0.0" -ForegroundColor Yellow
Write-Host "  3. Configurar 'About' (topics)" -ForegroundColor Yellow
Write-Host "  4. Compartilhar no LinkedIn" -ForegroundColor Yellow
Write-Host "  5. Preparar apresentação" -ForegroundColor Yellow
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Recursos disponíveis:" -ForegroundColor Cyan
Write-Host "  - GUIA_ATUALIZACAO_GITHUB.md" -ForegroundColor Gray
Write-Host "  - CHECKLIST_FINALIZACAO.md" -ForegroundColor Gray
Write-Host "  - TEMPLATES_DIVULGACAO.md`n" -ForegroundColor Gray

Read-Host "Pressione Enter para sair"
