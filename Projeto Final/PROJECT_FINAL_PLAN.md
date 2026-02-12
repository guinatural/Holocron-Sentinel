# Projeto Final - Módulo AWS re/Start

**Grupo:** Holocron Sentinel  
**Curso:** AWS re/Start - Escola da Nuvem  
**Ano:** 2025

**Integrantes:**
- **Guilherme Barreto Gomes** (Apresentador e Coordenador)
- **Aluno 1**
- **Aluno 2**
- **Aluno 3**

---

## Módulo RESTART

### 1. Identificação do Problema

**Ideia do Projeto:** Holocron Sentinel - Sistema Simples de Monitoramento de Segurança na AWS

**Descrição do Problema:**

Pequenas empresas que estão começando a usar a AWS enfrentam dificuldades para saber se suas configurações estão seguras. Muitas vezes não sabem responder perguntas básicas como: "Meus buckets S3 estão públicos sem querer?", "Quem tem acesso de administrador na minha conta?", "Consigo ver quem fez o quê no meu ambiente?".

Essas empresas não têm equipe especializada em segurança na nuvem e ficam com medo de estar fazendo algo errado que possa causar vazamento de dados ou problemas com a LGPD. Além disso, muitas não entendem bem que a AWS cuida de algumas coisas de segurança, mas outras são responsabilidade de quem usa (modelo de responsabilidade compartilhada).

**Stakeholders:**

- **Pequenas empresas** que usam AWS e não têm time de segurança
- **Donos de negócio** que precisam ter certeza que os dados estão seguros
- **Pessoas de TI** que gerenciam a AWS mas têm pouca experiência
- **Auditores** que precisam verificar se está tudo certo

**Justificativa:**

Criar uma ferramenta simples que verifica configurações básicas de segurança pode ajudar essas pequenas empresas a dormirem tranquilas. O sistema vai apenas ler as configurações (sem mexer em nada) e avisar sobre problemas que encontrar, tipo "Você tem um bucket público" ou "Tem usuário sem senha forte". Na segunda fase do curso, vamos usar IA para tornar as recomendações ainda mais úteis e personalizadas.

**Responsável pela Seção:** Guilherme Barreto Gomes

---

### 2. Levantamento de Requisitos

**Requisitos Funcionais (O que o sistema vai fazer):**

- Listar usuários e grupos do IAM e mostrar quem tem muito acesso
- Verificar se tem usuários sem MFA (autenticação em dois fatores)
- Listar buckets S3 e avisar se algum está público
- Mostrar instâncias EC2 e seus grupos de segurança
- Buscar nos logs do CloudTrail quem fez alterações importantes
- Gerar um relatório simples em PDF ou texto com os problemas encontrados

**Requisitos Não Funcionais (Como o sistema deve funcionar):**

- Só pode ler informações, nunca alterar nada (para não quebrar nada)
- Deve ser barato de rodar (usando o nível gratuito da AWS quando possível)
- Precisa ter instruções claras de como usar
- Deve funcionar em menos de 1 minuto para não deixar o usuário esperando
- Os dados coletados devem ficar guardados com segurança

**MVP (Versão Inicial Simples):**

Na primeira fase vamos fazer:
- Um script que coleta informações básicas do IAM, EC2, S3 e CloudTrail
- Uma análise simples que identifica problemas comuns
- Um relatório de texto mostrando o que foi encontrado e sugestões de melhoria

**Evolução Futura (Segunda Fase com IA):**

Depois vamos adicionar:
- IA para analisar os logs e encontrar comportamentos estranhos
- Recomendações personalizadas baseadas no tipo de empresa
- Um chatbot para responder dúvidas sobre segurança
- Relatórios automáticos em linguagem simples

**Responsável pela Seção:** Aluno 1

---

### 3. Planejamento Ágil

**Backlog de Tarefas (Lista de tudo que precisa ser feito):**

1. Estudar sobre segurança básica na AWS
2. Desenhar como o projeto vai funcionar (diagrama simples)
3. Criar conta AWS e configurar permissões básicas
4. Fazer script para pegar dados do IAM
5. Fazer script para pegar dados do EC2
6. Fazer script para pegar dados do S3
7. Fazer script para pegar dados do CloudTrail
8. Criar análise simples dos dados coletados
9. Salvar os resultados em arquivo
10. Fazer as recomendações de segurança
11. Criar o relatório final
12. Escrever documentação explicando o projeto
13. Preparar a apresentação

---

**Sprints (Divisão do trabalho em 4 etapas de 2 semanas cada):**

### **Sprint 1 (Semanas 1-2): Começando o Projeto**

**O que vamos fazer:** Estudar e preparar o ambiente

**Tarefas:**
- Tarefa 1: Estudar sobre segurança na AWS e fazer resumo
- Tarefa 2: Desenhar como o projeto vai funcionar
- Tarefa 3: Criar conta AWS e configurar acessos

**Quem faz o quê:**
- **Aluno 2:** Tarefa 1 - Estudar e fazer resumo sobre segurança
- **Guilherme:** Tarefa 2 e 3 - Desenhar projeto e configurar AWS

**O que entregamos:** Resumo de estudo, desenho do projeto, conta AWS pronta

---

### **Sprint 2 (Semanas 3-4): Coletando Informações**

**O que vamos fazer:** Criar scripts que pegam dados da AWS

**Tarefas:**
- Tarefa 4: Script que lista usuários e permissões do IAM
- Tarefa 5: Script que mostra instâncias e segurança do EC2
- Tarefa 6: Script que verifica buckets do S3

**Quem faz o quê:**
- **Aluno 3:** Tarefa 4 - Script do IAM
- **Aluno 1:** Tarefa 5 - Script do EC2
- **Guilherme:** Tarefa 6 - Script do S3 + ajudar os outros

**O que entregamos:** 3 scripts funcionando

---

### **Sprint 3 (Semanas 5-6): Analisando os Dados**

**O que vamos fazer:** Analisar os dados e criar recomendações

**Tarefas:**
- Tarefa 7: Script que busca logs importantes no CloudTrail
- Tarefa 8: Código que analisa e encontra problemas
- Tarefa 9: Código que salva os resultados
- Tarefa 10: Código que cria recomendações

**Quem faz o quê:**
- **Aluno 2:** Tarefa 7 - Script do CloudTrail
- **Aluno 3:** Tarefa 8 - Análise de problemas
- **Aluno 1:** Tarefa 9 - Salvar resultados
- **Guilherme:** Tarefa 10 - Criar recomendações + juntar tudo

**O que entregamos:** Sistema completo funcionando

---

### **Sprint 4 (Semanas 7-8): Finalizando**

**O que vamos fazer:** Criar relatório e documentação

**Tarefas:**
- Tarefa 11: Criar relatório final bonito
- Tarefa 12: Escrever documentação (como usar)
- Tarefa 13: Preparar apresentação

**Quem faz o quê:**
- **Aluno 3:** Tarefa 11 - Fazer relatório
- **Aluno 2:** Tarefa 12 - Escrever documentação
- **Guilherme:** Tarefa 13 - Preparar apresentação de 15 minutos

**O que entregamos:** Projeto completo, documentado e apresentação pronta

---

**Quadro de Acompanhamento (Trello/Notion):**

Vamos usar um quadro com 4 colunas:
- **Para Fazer:** Tarefas que ainda não começamos
- **Fazendo:** Tarefas em andamento
- **Revisando:** Tarefas prontas esperando aprovação
- **Pronto:** Tarefas finalizadas

Cada tarefa tem:
- Nome simples
- Quem é responsável
- Em qual sprint está
- Prazo

*(Colocar print do quadro aqui)*

**Responsável:** Guilherme Barreto Gomes

---

### 4. Apresentação

**Quem apresenta:** Guilherme Barreto Gomes (15 minutos)

**Como vai ser a apresentação:**

**1. Começando (2 minutos)**
   - Me apresento e apresento o grupo
   - Explico brevemente o que é o Holocron Sentinel
   - Conto por que escolhemos esse projeto

**2. Qual é o problema? (3 minutos)**
   - Explico que pequenas empresas têm medo de usar AWS errado
   - Mostro exemplos de problemas comuns (bucket público, senhas fracas)
   - Falo sobre a LGPD e por que isso importa
   - Mostro que existe muita empresa nessa situação

**3. O que o sistema vai fazer? (3 minutos)**
   - Explico que vai apenas verificar configurações
   - Mostro a lista do que vai checar (IAM, S3, EC2, CloudTrail)
   - Falo sobre a versão simples (MVP) e a versão futura com IA
   - Mostro que é seguro (só lê, não mexe em nada)

**4. Como organizamos o trabalho? (4 minutos)**
   - Mostro a lista de tarefas completa
   - Explico as 4 sprints (2 semanas cada)
   - Mostro o quadro com as tarefas e quem faz cada uma
   - Demonstro como está o progresso atual

**5. Próximos passos (2 minutos)**
   - Falo sobre como vamos implementar tecnicamente
   - Explico como vai funcionar a parte de IA no próximo módulo
   - Mostro o cronograma até terminar

**6. Finalizando (1 minuto)**
   - Reforço os benefícios do projeto
   - Abro para perguntas do instrutor

**O que vou mostrar na tela:**
- Desenho simples da arquitetura AWS
- Print do quadro de tarefas
- Exemplo de como seria o relatório
- Documentos de requisitos

**Responsável:** Guilherme Barreto Gomes

---

## Quem Faz O Quê (Resumo Simples)

| Pessoa | O que vai fazer | Quando |
|--------|-----------------|--------|
| **Guilherme (EU)** | - Escrever o problema<br>- Configurar AWS<br>- Script do S3<br>- Juntar tudo<br>- **APRESENTAÇÃO** | Todas as sprints |
| **Aluno 1** | - Escrever requisitos<br>- Script do EC2<br>- Salvar resultados | Sprints 2 e 3 |
| **Aluno 2** | - Estudar segurança<br>- Script do CloudTrail<br>- Fazer documentação | Sprints 1, 3 e 4 |
| **Aluno 3** | - Script do IAM<br>- Analisar problemas<br>- Fazer relatório | Sprints 2, 3 e 4 |

---

## Tecnologias que Vamos Usar (Bem Simples)

- **Python:** Para fazer os scripts (mais fácil de aprender)
- **AWS CLI:** Ferramenta da AWS para pegar informações
- **Boto3:** Biblioteca Python para AWS (já vem pronta)
- **Serviços AWS:** IAM, EC2, S3, CloudTrail (os básicos que aprendemos)
- **Arquivos de texto/JSON:** Para salvar os resultados

---

## Considerações Finais

Este projeto é uma forma de aplicar o que aprendemos no AWS re/Start de maneira prática e útil. Não estamos tentando criar algo super complexo, mas sim uma ferramenta simples que realmente ajude pequenas empresas a melhorarem sua segurança na AWS.

Dividimos o trabalho entre 4 pessoas para que cada um contribua com uma parte, mas o Guilherme vai coordenar tudo e fazer a apresentação completa. Se alguém não conseguir fazer sua parte, está planejado para que o Guilherme possa assumir as tarefas.

O importante é demonstrar que entendemos os conceitos de AWS, sabemos trabalhar com metodologia ágil e conseguimos pensar em uma solução real para um problema verdadeiro.

**Dica importante:** Vamos manter tudo simples e funcional. É melhor ter algo pequeno que funciona do que algo grande que não sai do papel!