# Guia de Tarefas: Aluno 1 - Monitoramento EC2 e Resultados

Olá, Aluno 1! 👋

Este guia explica exatamente o que você precisa fazer no projeto Holocron Sentinel. Sua parte é fundamental para garantir que ninguém esqueça "portas abertas" nos servidores (Instâncias EC2).

---

## 📅 Resumo das Atividades

| Atividade | O que é? | Por que é importante? | Quando? |
|-----------|----------|-----------------------|---------|
| **Script EC2** | Criar um código Python que lista servidores e Security Groups. | Evita que hackers entrem por portas inseguras (como a porta 22 aberta para o mundo). | Sprint 2 |
| **Salvar Resultados** | Fazer o código gravar o que achou em um arquivo `.txt`. | Precisamos de provas (evidências) para mostrar no relatório. | Sprint 3 |

---

## 🛠️ Detalhe da Tarefa 1: Script de verificação EC2

Você vai criar um arquivo chamado `check_ec2_security.py`.

**O que o código deve fazer:**
1. Conectar na AWS usando `boto3`.
2. Olhar todas as instâncias EC2 rodando.
3. Verificar os "Security Groups" (o firewall da AWS).
4. Avisar se encontrar a porta 22 (SSH) ou 3389 (RDP) aberta para `0.0.0.0/0` (internet toda).

### 💡 Como fazer (Exemplo Prático)

Use como base o arquivo que o Guilherme já fez:  
📂 `04_CODE/validate_audit_logs.py`

Abra esse arquivo e veja como ele faz a conexão:
```python
import boto3

# Conexão (você vai usar 'ec2' em vez de 's3')
client = boto3.client('ec2', region_name='sa-east-1')
```

**Seu desafio:**
Pesquise como usar o comando `describe_security_groups` no Boto3.
Link útil: [Documentação Boto3 EC2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_groups)

---

## 🛠️ Detalhe da Tarefa 2: Salvar Resultados

Depois que seu código encontrar os problemas, ele não pode só mostrar na tela preta do terminal. Ele precisa salvar em um arquivo.

**Como fazer:**
O Guilherme atualizou o script dele (`validate_audit_logs.py`) para salvar um arquivo `compliance_report.txt`. **Copie a lógica dele!**

Olhe estas linhas no final do arquivo dele:
```python
with open("relatorio_ec2.txt", "w") as f:
    f.write("Relatório de Segurança EC2\n")
    # ... escreva aqui os problemas encontrados
```

---

## 🤝 Dicas Finais

1. **Não tenha medo de errar.** O Python avisa onde está o erro.
2. **Pergunte ao Google:** "How to list security groups boto3 python".
3. **Teste pequeno:** Primeiro tente só listar os nomes dos grupos. Depois tente ver as regras.

Estamos juntos nessa! 🚀
