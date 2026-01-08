# Setup inicial de segurança AWS — Holocron Sentinel

Documento resumido com as medidas iniciais de segurança aplicadas à conta AWS do projeto.

Principais ações:
- Proteger a conta root: MFA ativado, senha forte e remoção de chaves de acesso.
- Criar usuário administrativo `gui-dev-admin` com MFA e pertencer ao grupo Admins.
- Aplicar princípio do menor privilégio para access keys; rotacionar a cada 90 dias.
- Configurar alertas de faturamento e um Budget inicial (ex.: $100).
- Definir política de senhas (mín. 14 caracteres, expiração 90 dias, histórico 5).
- Ativar CloudTrail (management-events-trail) com bucket S3 criptografado para logs.
- Padronizar tags: Environment, Project, Owner, CostCenter, ManagedBy.

Checklist:
- [x] Root protegido e MFA instruído
- [x] Usuário administrativo criado e MFA obrigatório
- [x] Diretrizes de access keys e rotação
- [x] Alertas de custo e budget configurados
- [x] Política de senhas definida
- [x] CloudTrail ativado com armazenamento seguro
- [x] Convenção de tags definida

Observação:
Este é o setup inicial. Recomenda-se automatizar e revisar periodicamente (ex.: Terraform, auditorias).
