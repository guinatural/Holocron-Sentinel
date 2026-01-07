# Lab Prático 01: Implementando a Auditoria LGPD (Art. 37)

**Objetivo:** Criar a infraestrutura de "Caixa de Vidro" do Holocron. Vamos configurar o AWS CloudTrail para registrar todas as ações da conta em um Bucket S3 criptografado.

**Tempo Estimado:** 30 min
**Custo:** Free Tier (se dentro dos limites) ou centavos de dólar.

---

## 🏗️ Parte 1: O Cofre Seguro (S3)
A LGPD (Art. 46) exige segurança desde a concepção (Security by Design).

1.  Acesse o **S3 Console**.
2.  Clique em **Create Bucket**.
3.  **Name:** `holocron-audit-logs-[seu-nome]` (Ex: `holocron-audit-logs-barreto`).
4.  **Region:** `us-east-1` (N. Virginia) ou `sa-east-1` (São Paulo - Ideal LGPD, mas mais caro). *Recomendado: us-east-1 para o curso*.
5.  **Block Public Access:** ✅ Mantenha **TUDO BLOQUEADO**.
6.  **Bucket Versioning:** ✅ **Enable** (Para garantir integridade dos logs).
7.  **Default Encryption:** ✅ **Enable** (Server-side encryption with Amazon S3 managed keys - SSE-S3).
8.  Clique em **Create Bucket**.

> 📸 **PRINT 1:** Tire um print da lista de buckets mostrando o cadeado ou status "Access: Bucket and objects not public".

---

## 🕵️‍♂️ Parte 2: O Auditor (CloudTrail)
Vamos ativar o registro de quem faz o que.

1.  Acesse o **CloudTrail Console**.
2.  Clique em **Create trail**.
3.  **Trail name:** `holocron-master-trail`.
4.  **Storage location:** Selecione "Use existing S3 bucket" e escolha o bucket criado na Parte 1.
5.  **Log file SSE-KMS encryption:** Desmarque (para economizar) ou Marque (para ganhar pontos extras, custa um pouco mais). *Para o lab, pode deixar desmarcado (usa SSE-S3 do bucket).*
6.  **Log file validation:** ✅ **Enable** (Isso cria um digest file para provar que ninguém alterou os logs - Crítico para LGPD).
7.  **Management Events:** ✅ Read & Write (All).
8.  Clique em **Create trail**.

> 📸 **PRINT 2:** Tire um print da tela de status do Trail mostrando "Logging status: Logging".

---

## 🧪 Parte 3: Gerando Evidência (O Incidente)
Vamos simular uma ação para ser auditada.

1.  Vá ao **EC2 Console** ou **IAM Console**.
2.  Crie uma tag em qualquer recurso ou crie um usuário IAM falso chamado `hacker-simulation`.
3.  Exclua o usuário logo em seguida.
4.  Espere cerca de 15 minutos (o CloudTrail tem um delay).

---

## 🔍 Parte 4: A Auditoria (Validando)
1.  Vá ao seu **Bucket S3** criado na Parte 1.
2.  Navegue pelas pastas: `AWSLogs` -> `[Account ID]` -> `CloudTrail`... até chegar nos arquivos `.json.gz`.
3.  Baixe um arquivo e abra. Procure pelo evento `CreateUser` ou a ação que você fez.

> 📸 **PRINT 3:** Tire um print do arquivo JSON aberto (pode ser no VS Code) mostrando o campo `"eventName": "CreateUser"` e `"userName": "seu-usuario"`. **Isso prova Rastreabilidade (Art. 37).**

---

## 📝 Parte 5: Documentando
Após tirar os prints, preencha o arquivo `03-Labs/LAB_TEMPLATE.md` com as imagens e mova para `05_EVIDENCE/AUDIT_LAB.md`.
