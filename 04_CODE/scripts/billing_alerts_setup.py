"""
Holocron Sentinel - Billing Alerts Automation
Script para configuração automatizada de alarmes de faturamento CloudWatch
Alinhado com AWS_SECURITY_SETUP.md seção 4
"""

import boto3
import sys
from botocore.exceptions import ClientError

class BillingAlertsSetup:
    def __init__(self, email_address, profile_name='default'):
        """
        Inicializa clientes AWS para configuração de billing alerts
        
        Args:
            email_address: Email para receber notificações de billing
            profile_name: Profile AWS CLI configurado
        """
        session = boto3.Session(profile_name=profile_name)
        
        # CloudWatch e SNS devem ser criados em us-east-1 para billing metrics
        self.cloudwatch = session.client('cloudwatch', region_name='us-east-1')
        self.sns = session.client('sns', region_name='us-east-1')
        self.email = email_address
        self.topic_arn = None
        
    def create_sns_topic(self):
        """
        Cria tópico SNS para envio de alertas de billing
        """
        try:
            response = self.sns.create_topic(
                Name='BillingAlerts-HolocronSentinel'
            )
            self.topic_arn = response['TopicArn']
            print(f"[OK] Tópico SNS criado: {self.topic_arn}")
            
            # Criar subscription via email
            self.sns.subscribe(
                TopicArn=self.topic_arn,
                Protocol='email',
                Endpoint=self.email
            )
            print(f"[OK] Subscription criado para {self.email}")
            print("[INFO] Verifique seu email e confirme a subscription")
            
        except ClientError as e:
            print(f"[ERROR] Falha ao criar tópico SNS: {e}")
            raise
    
    def create_billing_alarm(self, threshold_usd, alarm_name):
        """
        Cria alarme de billing no CloudWatch
        
        Args:
            threshold_usd: Valor em USD para disparar alarme
            alarm_name: Nome identificador do alarme
        """
        try:
            self.cloudwatch.put_metric_alarm(
                AlarmName=alarm_name,
                AlarmDescription=f'Alerta quando custo estimado excede ${threshold_usd}',
                ActionsEnabled=True,
                AlarmActions=[self.topic_arn],
                MetricName='EstimatedCharges',
                Namespace='AWS/Billing',
                Statistic='Maximum',
                Dimensions=[
                    {
                        'Name': 'Currency',
                        'Value': 'USD'
                    }
                ],
                Period=21600,  # 6 horas
                EvaluationPeriods=1,
                Threshold=threshold_usd,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                TreatMissingData='notBreaching'
            )
            print(f"[OK] Alarme '{alarm_name}' criado para threshold ${threshold_usd}")
            
        except ClientError as e:
            print(f"[ERROR] Falha ao criar alarme '{alarm_name}': {e}")
            raise
    
    def setup_all_alarms(self):
        """
        Configura todos os alarmes conforme especificação do projeto
        """
        alarms_config = [
            (10, 'Billing-Alert-10USD-Initial'),
            (50, 'Billing-Alert-50USD-Moderate'),
            (95, 'Billing-Alert-95USD-Critical')
        ]
        
        for threshold, alarm_name in alarms_config:
            self.create_billing_alarm(threshold, alarm_name)

def main():
    """
    Execução principal do script
    """
    print("="*60)
    print("Holocron Sentinel - Billing Alerts Setup")
    print("="*60)
    
    # CONFIGURAÇÃO: Alterar email antes de executar
    EMAIL_ADDRESS = "seu-email@exemplo.com"
    
    if EMAIL_ADDRESS == "seu-email@exemplo.com":
        print("[ERROR] Configure o email no script antes de executar")
        print("Edite a variável EMAIL_ADDRESS na função main()")
        sys.exit(1)
    
    print(f"\nConfigurando alertas para: {EMAIL_ADDRESS}\n")
    
    # Inicializar setup
    setup = BillingAlertsSetup(email_address=EMAIL_ADDRESS)
    
    # 1. Criar tópico SNS
    print("[STEP 1] Criando tópico SNS")
    setup.create_sns_topic()
    
    # 2. Criar alarmes
    print("\n[STEP 2] Criando alarmes de billing")
    setup.setup_all_alarms()
    
    print("\n" + "="*60)
    print("Setup de billing alerts concluído!")
    print("\nPRÓXIMOS PASSOS:")
    print("1. Verificar email e confirmar subscription SNS")
    print("2. Validar no Console: CloudWatch > Alarms")
    print("3. Habilitar 'Receive Billing Alerts' em:")
    print("   Billing Dashboard > Billing Preferences")
    print("="*60)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n[FATAL] Execução interrompida: {e}")

