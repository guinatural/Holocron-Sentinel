"""
Holocron Sentinel - AI Compliance Analyst
Modulo de Inteligencia Artificial para analise de conformidade LGPD.

Servico AWS de producao: Amazon GuardDuty + Amazon Bedrock
Implementacao de demonstracao: Google Gemini API (gratuita)

Como funciona:
  1. Le o relatorio de auditoria gerado pelo validate_audit_logs.py
  2. Envia o conteudo para um modelo de linguagem (LLM)
  3. Recebe um parecer executivo em portugues, como faria um analista de seguranca

Requisitos:
  pip install google-generativeai

Chave gratuita em: https://aistudio.google.com/app/apikey
"""

import google.generativeai as genai
import os
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# CONFIGURACAO
# Cole sua chave gratuita do Google AI Studio abaixo
# (obtenha em: https://aistudio.google.com/app/apikey)
# ─────────────────────────────────────────────────────────────
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")

# Dados simulados do relatorio de auditoria (normalmente viriam do validate_audit_logs.py)
SIMULATED_AUDIT_REPORT = """
AUDIT REPORT - Holocron Sentinel
Data: {date}
Bucket: holocron-sentinel-audit-logs-br-sao
Regiao: sa-east-1 (Brasil - Sao Paulo)

======================================
RESULTADOS DA VARREDURA IAM
======================================
- Usuario: admin-root | MFA: NAO CONFIGURADO | Status: CRITICO
- Usuario: gui-dev-admin | MFA: ATIVO | Status: OK
- Usuario: dev-pipeline | MFA: NAO CONFIGURADO | Status: ALTO RISCO
- Politica de senhas: 14 caracteres, expiracao 90 dias | Status: OK

======================================
RESULTADOS DA VARREDURA S3
======================================
- Bucket: dados-clientes-br | Criptografia: aws:kms | Status: COMPLIANT
- Bucket: backups-sistema | Criptografia: NENHUMA | Status: VIOLACAO LGPD Art.46
- Bucket: logs-auditoria | Criptografia: aws:kms | Status: COMPLIANT
- Acesso Publico Bloqueado: SIM em 2/3 buckets

======================================
RESULTADOS DO CLOUDTRAIL
======================================
- CloudTrail ativo em sa-east-1: SIM
- Log de integridade (digest): ATIVO
- Ultimo evento suspeito: ConsoleLogin de IP 187.42.x.x as 02:34 (fora do horario comercial)
- Tentativas de login falhas: 7 nos ultimos 3 dias

======================================
SCORE DE CONFORMIDADE: 68/100
""".format(date=datetime.now().strftime("%Y-%m-%d %H:%M"))


def analisar_com_ia(relatorio: str) -> str:
    """
    Envia o relatorio de auditoria para o modelo de IA e recebe
    um parecer executivo estruturado.

    Em producao (AWS), isso seria substituido por:
    - Amazon Bedrock (modelo Claude ou Titan)
    - Amazon GuardDuty Findings via API
    """

    prompt = f"""
Voce e um Analista Senior de Segurança em Nuvem especializado em conformidade LGPD e AWS.

Analise o seguinte relatorio de auditoria tecnica e produza um PARECER EXECUTIVO estruturado.
O parecer deve ser escrito em português formal, adequado para ser entregue a um Diretor de TI.

REGRAS DO PARECER:
1. Identifique os 3 riscos mais criticos em ordem de prioridade.
2. Para cada risco, explique o impacto real para o negocio (nao apenas tecnico).
3. Recomende a acao corretiva especifica, citando o servico AWS que resolve o problema.
4. Ao final, escreva uma conclusao de 2 linhas para o executivo.
5. Use linguagem clara. Evite jargoes tecnicos excessivos.

RELATORIO DE AUDITORIA:
{relatorio}

FORMATO DE SAIDA:
# Parecer Executivo - Conformidade LGPD
**Data da Analise:** [data]
**Score de Conformidade:** [X/100]

## Riscos Identificados (por prioridade)
[lista formatada]

## Conclusao para a Diretoria
[texto]
"""

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

    print("[*] Enviando relatorio para analise de IA...")
    print("[*] Modelo: Google Gemini 1.5 Flash (equivalente AWS: Amazon Bedrock Claude)")
    print("-" * 60)

    response = model.generate_content(prompt)
    return response.text


def executar_analise():
    print("=" * 60)
    print("Holocron Sentinel - AI Compliance Analyst")
    print("Conformidade LGPD com Inteligencia Artificial")
    print("=" * 60)

    if GEMINI_API_KEY == "SUA_CHAVE_AQUI":
        print("\n[DEMO MODE] Chave de API nao configurada.")
        print("Para usar com IA real:")
        print("  1. Acesse: https://aistudio.google.com/app/apikey")
        print("  2. Gere uma chave gratuita")
        print("  3. Substitua 'SUA_CHAVE_AQUI' neste script")
        print("\n[DEMO] Simulando parecer de IA para demonstracao:\n")
        exibir_parecer_simulado()
        return

    # Tenta carregar relatorio real, usa simulado se nao encontrar
    try:
        with open("compliance_report.txt", "r") as f:
            relatorio = f.read()
        print("[*] Relatorio real carregado: compliance_report.txt")
    except FileNotFoundError:
        relatorio = SIMULATED_AUDIT_REPORT
        print("[*] Usando relatorio simulado para demonstracao.")

    parecer = analisar_com_ia(relatorio)

    # Salvar parecer
    output_file = f"parecer_executivo_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(parecer)

    print(parecer)
    print("-" * 60)
    print(f"\n[OK] Parecer salvo em '{output_file}'")
    print("[*] Em producao AWS: este parecer seria gerado pelo Amazon Bedrock")
    print("[*] Deteccao continua: Amazon GuardDuty monitora 24/7 automaticamente")


def exibir_parecer_simulado():
    """Exibe um parecer simulado para demonstracao sem chave de API."""
    parecer = """
# Parecer Executivo - Conformidade LGPD
**Data da Analise:** {date}
**Score de Conformidade:** 68/100 — ATENCAO NECESSARIA

---

## Riscos Identificados (por prioridade)

**1. CRITICO — Bucket S3 sem criptografia (LGPD Art. 46)**
   - Impacto para o negocio: Dados de clientes armazenados sem protecao.
     Em caso de vazamento, a empresa esta sujeita a multa de ate 2% do
     faturamento anual (LGPD, Art. 52).
   - Acao corretiva: Ativar SSE-KMS no bucket 'backups-sistema' via
     AWS Console ou executar o script validate_audit_logs.py com correcao.

**2. ALTO RISCO — 2 usuarios sem MFA (LGPD Art. 46 + AWS Best Practices)**
   - Impacto para o negocio: Uma credencial vazada em phishing pode
     comprometer toda a infraestrutura da empresa sem qualquer barreira.
   - Acao corretiva: Ativar politica IAM de MFA obrigatorio (arquivo
     iam_mfa_enforcement.json ja esta disponivel no repositorio).

**3. MEDIO — Acesso suspeito fora do horario comercial**
   - Impacto para o negocio: Login detectado as 02:34 de IP nao
     catalogado. Pode indicar credencial comprometida ou acesso nao
     autorizado de terceiro.
   - Acao corretiva: Revisar o usuario responsavel pelo evento no
     CloudTrail e, se necessario, revogar e renovar as credenciais.

---

## Conclusao para a Diretoria
O ambiente apresenta bases solidas de seguranca, porem dois pontos criticos
precisam de correcao imediata para garantir conformidade plena com a LGPD e
evitar exposicao legal. As correcoes podem ser executadas em menos de 2 horas
com os scripts automatizados disponibilizados pela equipe Holocron Sentinel.
""".format(date=datetime.now().strftime("%d/%m/%Y %H:%M"))

    print(parecer)
    output_file = f"parecer_executivo_demo_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(parecer)
    print(f"[OK] Parecer de demonstracao salvo em '{output_file}'")
    print("\n[*] Servico equivalente em producao AWS: Amazon Bedrock (Claude 3)")
    print("[*] Deteccao de ameacas em tempo real: Amazon GuardDuty")
    print("[*] Descoberta de dados sensiveis: Amazon Macie")


if __name__ == "__main__":
    executar_analise()
