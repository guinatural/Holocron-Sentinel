# Guia de Tarefas: Aluno 3 - IAM, Análise e Relatório Final

Olá, Aluno 3! 👋

Você tem uma missão crítica: cuidar das identidades (usuários) e juntar todas as peças no final. Se o IAM estiver errado, nada mais funciona.

---

## 📅 Resumo das Atividades

| Atividade | O que é? | Por que é importante? | Quando? |
|-----------|----------|-----------------------|---------|
| **Script IAM** | Código que lista usuários e grupos. | Para achar usuários com permissão demais (Admin) ou sem MFA. | Sprint 2 |
| **Análise de Problemas** | Criar a lógica que diz "Isso é perigoso" ou "Isso está OK". | O script não pode só listar, tem que julgar se está seguro. | Sprint 3 |
| **Relatório Final** | Juntar os dados de todos (EC2, S3, IAM) num texto final. | É o produto final que entregamos pro cliente. | Sprint 4 |

---

## 🛠️ Detalhe da Tarefa 1: Script IAM

Você vai criar/melhorar o arquivo `audit_iam.py`.

**O que o código deve fazer:**
1. Listar todos os usuários.
2. Verificar se o usuário tem MFA ativado (`MFAEnabled`).
3. Verificar se o usuário senha antiga demais.

### 💡 Onde já tem coisa pronta?

Já existe um script muito bom na pasta:  
📂 `04_CODE/scripts/setup_iam_structure.py`

Esse script *cria* usuários. Você precisa fazer um que *lê* usuários.
Mas a lógica de conexão é a mesma!

```python
iam = boto3.client('iam')
users = iam.list_users()

for user in users['Users']:
    print(user['UserName'])
    # Agora pesquise: como ver se tem MFA?
```

---

## 🛠️ Detalhe da Tarefa 2: Juntar o Relatório

No final, você vai pegar os arquivos de texto gerados pelo script do Aluno 1 (EC2) e do Guilherme (S3) e criar um "Relatórionem" único.

**Ideia de lógica:**
```python
def gerar_relatorio_final():
    # Ler arquivo do Aluno 1
    with open("relatorio_ec2.txt") as f:
        dados_ec2 = f.read()
        
    # Ler arquivo do Guilherme
    with open("relatorio_s3.txt") as f:
        dados_s3 = f.read()
        
    # Salvar tudo num só
    with open("RELATORIO_COMPLETO_DIRETORIA.txt", "w") as final:
        final.write(dados_ec2)
        final.write("\n---\n")
        final.write(dados_s3)
```

---

## 🤝 Dicas Finais

*   IAM é cheio de detalhes. Foque no básico: "Tem MFA?" e "É Admin?".
*   O relatório final é a "cara" do projeto. Capriche no texto que vai dentro dele.
*   Trabalhe junto com o Aluno 1 e 2 para combinar os nomes dos arquivos.

Vamos nessa! 🛡️
