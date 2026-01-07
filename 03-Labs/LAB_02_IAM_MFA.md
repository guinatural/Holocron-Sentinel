# Lab Prático 02: Identidade Blindada (IAM MFA)

**Objetivo:** Implementar a política de "Zero Trust" onde usuários sem MFA não conseguem fazer nada na conta. Vamos usar o arquivo JSON que criamos na pasta `04_CODE`.

**Tempo Estimado:** 20 min
**Custo:** Grátis.

---

## 🛡️ Parte 1: Criando a "Lei" (IAM Policy)
Vamos pegar nosso código e colocar na AWS.

1.  Acesse o **IAM Console** > **Policies**.
2.  Clique em **Create policy**.
3.  Abra a aba **JSON**.
4.  Copie o conteúdo do arquivo local: `04_CODE/iam_mfa_enforcement.json`.
5.  Cole no console.
6.  Nombe: `ForceMFA-Holocron`.
7.  Description: "Bloqueia todas ações exceto self-managed MFA se não estiver autenticado com token."
8.  Clique em **Create policy**.

> 📸 **PRINT 1:** Print da tela de Policies mostrando a `ForceMFA-Holocron` criada.

---

## 🧪 Parte 2: A Cobai...digo, Usuário de Teste
Vamos criar um usuário para testar se a trava funciona.

1.  Vá em **Users** > **Create user**.
2.  Nome: `test-mfa-user`.
3.  Marque "Provide user access to the AWS Management Console".
4.  Marque "I want to create an IAM user" (Sim, opções antigas).
5.  Senha customizada fácil (ex: `Teste123!`). Desmarque "User must create a new password".
6.  **Permissions:** Selecione "Attach policies directly".
7.  Adicione DUAS políticas:
    *   `AmazonS3FullAccess` (Dê poder total para provar que a trava bloqueia até admins).
    *   `ForceMFA-Holocron` (Nossa trava).
8.  Crie o usuário.

---

## 🚫 Parte 3: O Bloqueio (Teste Negativo)
1.  Abra uma **Janela Anônima** no navegador.
2.  Faça login com `test-mfa-user`.
3.  Tente entrar no **S3 Console**.
4.  **Resultado Esperado:** Você verá mensagens de "Access Denied" ou "You don't have permission" em tudo, mesmo tendo `S3FullAccess`.

> 📸 **PRINT 2:** Tire um print dessa tela vermelha de erro. Isso prova que a política funciona!

---

## 🔓 Parte 4: A Conformidade (Configurando MFA)
Ainda como `test-mfa-user`:
1.  Vá no menu do usuário (canto superior direito) > **Security credentials**.
2.  Em **MFA**, clique em **Assign MFA device**.
3.  Dê um nome (ex: `MyPhone`) e use o Microsoft Authenticator ou Google Authenticator do seu celular para ler o QR Code.
4.  Digite os 2 códigos e ative.
5.  **IMPORTANTE:** Faça **Logout** e **Login novamente** (agora usando o código MFA).

---

## ✅ Parte 5: O Sucesso (Teste Positivo)
1.  Tente acessar o **S3 Console** novamente.
2.  Agora você deve ver a lista de buckets normalmente.

> 📸 **PRINT 3:** Print da lista de buckets visível, provando que com MFA o acesso é liberado.

---

## 🧹 Parte 6: Limpeza
*   Exclua o usuário `test-mfa-user` para não deixar brechas.
*   (Não exclua a política, ela é parte do projeto).
