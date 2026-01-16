"""
Holocron Sentinel - IAM Security Setup Automation
Script para criação automatizada da estrutura de grupos e usuários IAM
Alinhado com AWS_SECURITY_SETUP.md e LGPD Article 46
"""

import boto3
import json
import sys
import os
from pathlib import Path
from botocore.exceptions import ClientError

class IAMSecuritySetup:
    def __init__(self, profile_name='default'):
        """
        Inicializa cliente IAM com profile AWS CLI
        
        Args:
            profile_name: Nome do profile configurado em ~/.aws/credentials
        """
        session = boto3.Session(profile_name=profile_name)
        self.iam_client = session.client('iam')
        self.account_id = session.client('sts').get_caller_identity()['Account']
        
    def create_group_with_policy(self, group_name, policy_file_path):
        """
        Cria grupo IAM e anexa política customizada
        
        Args:
            group_name: Nome do grupo IAM
            policy_file_path: Caminho para arquivo JSON da política
        """
        try:
            # Criar grupo
            self.iam_client.create_group(GroupName=group_name)
            print(f"[OK] Grupo '{group_name}' criado com sucesso")
            
            # Ler política do arquivo
            with open(policy_file_path, 'r') as policy_file:
                policy_document = json.load(policy_file)
            
            # Criar política inline no grupo
            self.iam_client.put_group_policy(
                GroupName=group_name,
                PolicyName=f'{group_name}Policy',
                PolicyDocument=json.dumps(policy_document)
            )
            print(f"[OK] Política anexada ao grupo '{group_name}'")
            
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print(f"[WARN] Grupo '{group_name}' já existe")
            else:
                print(f"[ERROR] Falha ao criar grupo '{group_name}': {e}")
                raise
    
    def create_user_with_mfa_enforcement(self, username, groups):
        """
        Cria usuário IAM e adiciona aos grupos especificados
        
        Args:
            username: Nome do usuário IAM
            groups: Lista de grupos aos quais adicionar o usuário
        """
        try:
            # Criar usuário
            self.iam_client.create_user(UserName=username)
            print(f"[OK] Usuário '{username}' criado com sucesso")
            
            # Criar login profile
            self.iam_client.create_login_profile(
                UserName=username,
                Password='ChangeMe@12345!',  # Senha temporária
                PasswordResetRequired=True
            )
            print(f"[OK] Login profile criado (senha temporária definida)")
            
            # Adicionar usuário aos grupos
            for group in groups:
                self.iam_client.add_user_to_group(
                    GroupName=group,
                    UserName=username
                )
                print(f"[OK] Usuário adicionado ao grupo '{group}'")
                
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print(f"[WARN] Usuário '{username}' já existe")
            else:
                print(f"[ERROR] Falha ao criar usuário '{username}': {e}")
                raise
    
    def setup_password_policy(self):
        """
        Configura política de senhas global da conta conforme AWS_SECURITY_SETUP.md
        """
        try:
            self.iam_client.update_account_password_policy(
                MinimumPasswordLength=14,
                RequireSymbols=True,
                RequireNumbers=True,
                RequireUppercaseCharacters=True,
                RequireLowercaseCharacters=True,
                AllowUsersToChangePassword=True,
                ExpirePasswords=True,
                MaxPasswordAge=90,
                PasswordReusePrevention=5,
                HardExpiry=False
            )
            print("[OK] Política de senhas configurada: 14 chars, complexidade alta, expiração 90 dias")
            
        except ClientError as e:
            print(f"[ERROR] Falha ao configurar política de senhas: {e}")
            raise
    
    def generate_credential_report(self):
        """
        Gera relatório de credenciais para auditoria de compliance
        """
        try:
            response = self.iam_client.generate_credential_report()
            print(f"[OK] Relatório de credenciais: {response['State']}")
            
            if response['State'] == 'COMPLETE':
                report = self.iam_client.get_credential_report()
                with open('credential_report.csv', 'wb') as f:
                    f.write(report['Content'])
                print("[OK] Relatório salvo em 'credential_report.csv'")
                
        except ClientError as e:
            print(f"[ERROR] Falha ao gerar relatório: {e}")

def main():
    """
    Execução principal do script
    """
    print("="*60)
    print("Holocron Sentinel - IAM Security Setup")
    print("Compliance: LGPD Art. 46 | AWS Well-Architected Security")
    print("="*60)
    
    # Inicializar setup
    setup = IAMSecuritySetup(profile_name='default')
    
    print(f"\nAccount ID: {setup.account_id}")
    print("\nIniciando configuração...\n")
    
    # 1. Configurar política de senhas
    print("[STEP 1] Configurando política de senhas da conta")
    setup.setup_password_policy()
    
    # 2. Criar grupos com políticas
    print("\n[STEP 2] Criando grupos IAM")
    
    # Obter diretório base do script
    script_dir = Path(__file__).parent
    policies_dir = script_dir.parent / 'iam_policies'
    
    groups_config = {
        'Admins': str(policies_dir / 'admin_group_policy.json'),
        'Developers': str(policies_dir / 'developer_group_policy.json'),
        'ReadOnly': str(policies_dir / 'readonly_group_policy.json')
    }
    
    for group_name, policy_path in groups_config.items():
        setup.create_group_with_policy(group_name, policy_path)
    
    # 3. Criar usuário administrativo
    print("\n[STEP 3] Criando usuário administrativo")
    setup.create_user_with_mfa_enforcement('gui-dev-admin', ['Admins'])
    
    # 4. Gerar relatório de credenciais
    print("\n[STEP 4] Gerando relatório de compliance")
    setup.generate_credential_report()
    
    print("\n" + "="*60)
    print("Setup concluído com sucesso!")
    print("\nPRÓXIMOS PASSOS MANUAIS:")
    print("1. Fazer login como 'gui-dev-admin' e trocar senha temporária")
    print("2. Ativar MFA virtual para o usuário no Console AWS")
    print("3. Documentar evidências conforme template em 05_EVIDENCE/")
    print("="*60)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n[FATAL] Execução interrompida: {e}")
        sys.exit(1)
