# Roteiro de Apresentação Individual: Holocron Sentinel (15 Minutos)

**Ferramenta Visual:** `06_PRESENTATION/index.html` (Navegue pelos slides via scroll).
**Apresentador:** Arquiteto de Cloud Guilherme Barreto Gomes.

---

## ⏱️ 0-1.5 MIN: Introdução (Slide 1: Início)
*   **Posicionamento:** Tela no Slide 1 (Capa).
*   **Foco:** Quem você é e qual a grande ideia.
*   **Discurso:**
    *   "Bom dia. Sou Guilherme Barreto Gomes e hoje apresento o **Holocron Sentinel**. Meu objetivo é demonstrar como transformamos um dos maiores medos jurídicos das empresas brasileiras hoje — a LGPD — em uma vantagem competitiva através de automação e Inteligência Artificial nativa da AWS."
    *   "Este projeto protege o maior ativo de uma empresa moderna: o dado pessoal."

---

## ⏱️ 1.5-3.5 MIN: A Crise Invisível (Slide 2: Problema)
*   **Posicionamento:** Role para o Slide 2.
*   **Foco:** O custo da falha (Valor de Negócio).
*   **Discurso:**
    *   "80% das falhas de segurança acontecem por configuração errada. Pequenas empresas sofrem de **cegueira técnica**: elas têm o dado, mas não sabem quem os acessa. Multas de **R$ 50 milhões** não são ficção. O diferencial do Holocron? Pronta-resposta automática com custo **80% menor** que o modelo tradicional."

---

## ⏱️ 3.5-5.5 MIN: Fundações & Requisitos (Slide 3: Requisitos)
*   **Posicionamento:** Role para o Slide 3.
*   **Foco:** Engenharia e Rigor.
*   **Discurso:**
    *   "Para resolver isso, definimos requisitos rígidos: identificação de PII via Macie e logs imutáveis. Mas nossa excelência está na soberania nacional (sa-east-1) e no MFA forçado. É segurança por design."

---

## ⏱️ 5.5-7.5 MIN: A Responsabilidade do Empresário (Slide 4: Risco)
*   **Posicionamento:** Role para o Slide 4.
*   **Foco:** O "gap" de responsabilidade.
*   **Discurso:**
    *   "Aqui está o ponto vital para qualquer empresário: o **Modelo de Responsabilidade Compartilhada**. Muitos acreditam que ao colocar dados na AWS, a Amazon é responsável por tudo. **Isso é um erro perigoso.**"
    *   "A AWS garante a segurança **DA** nuvem (o hardware). Mas a segurança **NA** nuvem — configurar a criptografia, gerir as chaves e proteger o dado — é responsabilidade **SUA**, o empresário."
    *   "Se um dado vazar por um bucket aberto, a responsabilidade jurídica perante a ANPD é da sua empresa. O Holocron Sentinel nasce justamente para blindar a sua parte dessa responsabilidade."

---

## ⏱️ 7.5-9.5 MIN: Agilidade & Gestão (Slide 5: Planejamento)
*   **Posicionamento:** Role para o Slide 5.
*   **Foco:** Organização Ágil.
*   **Discurso:**
    *   "Organizamos este projeto em Sprints. Priorizamos o 'Hardening' de identidade e auditoria. Como podem ver no Board, cada tarefa técnica está amarrada a um requisito de lei."

---

## ⏱️ 9.5-11.5 MIN: O Motor do Sentinel (Slide 6: Automação)
*   **Posicionamento:** Role para o Slide 6.
*   **Foco:** O coração técnico (Python/Boto3).
*   **Discurso:**
    *   "O diferencial é que o Sentinel é movido por automação real via **SDK Boto3**. Nossos scripts, como este que veem na tela, fiscalizam a criptografia em milissegundos. É a tecnologia eliminando o erro humano."

---

## ⏱️ 11.5-13.5 MIN: O Cérebro da Auditoria (Slide 7: Solução IA)
*   **Posicionamento:** Role para o Slide 7.
*   **Foco:** Inteligência Centralizada.
*   **Discurso:**
    *   "Adicionamos o cérebro: **Amazon Bedrock com Titan**. Ele interpreta logs do Macie e GuardDuty e gera um parecer em português claro, permitindo decisões rápidas e centralizadas para a diretoria."

---

## ⏱️ 13.5-15 MIN: Conclusão & Resumo (Slide 8: Resumo)
*   **Posicionamento:** Role para o slide final.
*   **Foco:** Encerramento.
*   **Discurso:**
    *   "O Sentinel prova que segurança automatizada é 80% mais barata e infinitamente mais segura. Seguimos o AWS Well-Architected Framework, incluindo otimização de custos com Lifecycle Rules do S3, garantindo que sua empresa esteja sempre pronta para auditorias com o menor investimento possível."
    *   "Obrigado e estou aberto a perguntas."
