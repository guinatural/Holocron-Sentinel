# Guia de Tarefas: Aluno 2 - Estudos, CloudTrail e Documentação

Olá, Aluno 2! 👋

Sua responsabilidade é ser o "cérebro" da documentação e o "detetive" dos logs. Você vai garantir que tudo esteja escrito e que a gente consiga rastrear o que acontece na conta AWS.

---

## 📅 Resumo das Atividades

| Atividade | O que é? | Por que é importante? | Quando? |
|-----------|----------|-----------------------|---------|
| **Estudo de Segurança** | Resumir os conceitos básicos (IAM, Logs, Criptografia). | Para o grupo todo falar a mesma língua e colocarmos no trabalho escrito. | Sprint 1 |
| **Script CloudTrail** | Código para buscar logs de quem fez login ou apagou coisas. | Se alguém invadir, precisamos saber QUEM foi e QUANDO. | Sprint 3 |
| **Documentação** | Escrever o "manual" de como usar nosso projeto. | Um projeto sem manual ninguém usa. | Sprint 4 |

---

## 🛠️ Detalhe da Tarefa 1: Script CloudTrail

Você vai criar um arquivo chamado `analyze_cloudtrail.py`.

**O que o código deve fazer:**
1. Conectar no serviço CloudTrail.
2. Buscar os últimos eventos (ex: últimos 10 acessos).
3. Filtrar eventos perigosos, como `ConsoleLogin` (quem logou) ou `TerminateInstances` (quem deletou servidor).

### 💡 Como fazer (Exemplo Prático)

Veja o arquivo de exemplo:  
📂 `04_CODE/validate_audit_logs.py`

Você vai mudar o serviço para `cloudtrail`:
```python
client = boto3.client('cloudtrail', region_name='sa-east-1')

# Exemplo de busca de eventos
response = client.lookup_events(
    LookupAttributes=[
        {'AttributeKey': 'EventName', 'AttributeValue': 'ConsoleLogin'}
    ],
    MaxResults=10
)
```

**Dica:** Estude o JSON que volta dessa resposta. Ele tem campos como `Username` e `EventTime`.

---

## 🛠️ Detalhe da Tarefa 2: Documentação

Você é responsável por deixar o projeto profissional.

**O que escrever:**
1. Como instalar o Python e rodar nossos scripts.
2. O que cada script faz.

**Onde olhar:**
Veja a pasta `00-Master`. Lá tem vários exemplos de documentos Markdown (`.md`). Você pode criar um arquivo `MANUAL_DO_USUARIO.md`.

Use o **ChatGPT** ou **Claude** a seu favor: "Gere um manual de usuário para um script Python de segurança AWS". Depois adapte para o nosso!

---

## 🤝 Dicas Finais

*   Use a documentação oficial da AWS (Boto3 CloudTrail).
*   Mantenha a documentação simples. Imagine que está explicando para sua avó.
*   **Capriche na formatação:** Use negrito, títulos e listas.

Bom trabalho! 📚
