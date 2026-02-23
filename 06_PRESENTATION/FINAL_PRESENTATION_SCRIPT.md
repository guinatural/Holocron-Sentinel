# Guia de Performance: Apresentação Holocron Sentinel (15 Minutos)

**Ferramenta Principal:** `index.html` (Apresentação Web Interativa)
**Objetivo:** Contar uma história técnica e impactante sobre segurança na AWS e conformidade LGPD.

---

## BLOCO 1: Abertura
**Visual:** Slide 1 - Capa (Holocron Sentinel)

*   **Ação:** Mantenha a tela na capa. Deixe o efeito de brilho do fundo agir.
*   **O que dizer:**
    *   "Bom dia. Sou Guilherme Barreto Gomes. Hoje, não vou apenas lhes mostrar um projeto técnico; vou lhes mostrar como transformamos o **medo jurídico da LGPD** em **confiança técnica** usando a nuvem da AWS."
    *   "Este é o Holocron Sentinel – nossa 'Sentinela' para a proteção de dados sensíveis."

---

## BLOCO 2: Identificação do Cenário
**Visual:** Slide 2 - A Crise Invisível (Seção de Gráfico)

*   **Ação:** Role para o segundo slide. Aponte para as barras de gráfico à direita.
*   **O que dizer:**
    *   "Vejam estes dados. 85% das empresas brasileiras falham na auditabilidade (Art. 37). Isso significa que elas tratam dados pessoais, mas não conseguem provar ao governo QUEM acessou esses dados."
    *   "O risco não é abstrato: são multas de 50 milhões de reais. O Holocron Sentinel nasceu para iluminar essas áreas cinzentas, transformando a opacidade em transparência absoluta."

---

## BLOCO 3: Mapeamento de Conformidade
**Visual:** Slide 3 - Os Pilares da Lei (Grade de Artigos)

*   **Ação:** Role para o terceiro slide. Passe o mouse sobre os cards (eles têm efeito de destaque).
*   **O que dizer:**
    *   "A conformidade não é um checklist; é arquitetura. Traduzimos a lei em tecnologia em 6 frentes fundamentais."
    *   "Destaque para o **Artigo 46 (Segurança)**: Garantimos criptografia AES-256 em 100% do Data Lake."
    *   "E o **Artigo 3º (Soberania)**: Nossos dados nunca saem de solo brasileiro; estão fixados na região de São Paulo (`sa-east-1`)."

---

## BLOCO 4: Arquitetura de Segurança e Deep Dive Técnico
**Visual:** Slide 4 - Arquitetura Glass Box (Mapa AWS)

*   **Ação:** Role para o quarto slide. Mostre os badges de serviços AWS e a nova tabela lateral de detalhes.
*   **O que dizer:**
    *   "Como este é um projeto de Cloud Practitioner, quero dar um mergulho profundo na nossa stack tecnológica. Não apenas usamos os serviços, nós os configuramos para segurança máxima."
    *   "No **IAM**, não apenas criamos usuários; implementamos o princípio do menor privilégio e forçamos o MFA via API (MFA Enforcement)."
    *   "Nosso **S3** é blindado com 'Block Public Access' e usamos 'Object Lock' nos logs para garantir que a trilha de auditoria seja legalmente imutável."
    *   "Toda a criptografia é gerida pelo **KMS** usando Chaves Gerenciadas pelo Cliente (CMK) com AES-256."
    *   "E o **AWS Config** monitora tudo em tempo real, garantindo que se alguém desativar uma criptografia, sejamos alertados instantaneamente via SNS."

---

## BLOCO 5: Engenharia e Automação
**Visual:** Slide 5 - Segurança como Código (Seção Terminal)

*   **Ação:** Role para o quinto slide. Mostre o snippet de código Python.
*   **O que dizer:**
    *   "Para nós, segurança não é uma configuração manual; é código. Desenvolvi scripts em Python usando `boto3` que automatizam a fiscalização."
    *   "Este script que vocês veem não apenas verifica se o bucket está criptografado (Art. 46); ele pode disparar uma auto-remediação em milissegundos se encontrar uma vulnerabilidade."

---

## BLOCO 6: Inteligência Artificial
**Visual:** Slide 6 - Analista IA (Visualização de Dados)

*   **Ação:** Role para o sexto slide. Mostre o "Cérebro" e o Parecer da IA.
*   **O que dizer:**
    *   "O próximo passo do Sentinel é o cérebro. No módulo de IA, integraremos o **Amazon Bedrock**."
    *   "A IA analisará milhões de linhas de logs do CloudTrail e escreverá, como vocês podem ver na tela, um **Parecer Executivo** pronto para o Diretor de TI, identificando comportamentos anômalos que o olho humano jamais perceberia."

---

## BLOCO 7: Conclusão e Resultados
**Visual:** Slide 7 - Impacto (Grade de Métricas)

*   **Ação:** Role para o final. Agradeça e mantenha o contato visual.
*   **O que dizer:**
    *   "Nossos resultados são claros: 100% de compliance, zero dados expostos e um tempo de resposta inferior a 5 minutos."
    *   "A privacidade não é mais opcional. O Holocron Sentinel prova que com AWS e IA, o compliance se torna uma vantagem estratégica. Obrigado e estou aberto a perguntas."

---

### 💡 Dicas de Sucesso para Guilherme:
1.  **Ritmo do Scroll:** Não role rápido demais. Espere os olhos da banca focarem nos títulos.
2.  **Mouse como Laser:** Use o ponteiro do mouse para circular termos importantes como "AES-256" ou "sa-east-1".
3.  **Paixão Técnica:** Nas partes de Código e IA, mostre autoridade. Você é o Arquiteto.
4.  **Hardware:** Se puder, apresente o `index.html` em modo tela cheia (F11).
