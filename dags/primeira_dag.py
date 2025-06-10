from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def inicio():
    print("🏁 Iniciando o processo...")

def coleta():
    print("📥 Coletando dados...")

def processamento():
    print("⚙️ Processando dados...")

def fim():
    print("✅ Processo finalizado com sucesso!")

with DAG(
    dag_id='exemplo_airflow_simples',
    start_date=datetime(2025, 6, 1),
    schedule_interval='0 * * * *',  # Executa de hora em hora
    catchup=False,
    tags=['exemplo'],
) as dag:

    inicio_processo = PythonOperator(
        task_id='inicio_processo',
        python_callable=inicio,
    )

    coleta_dados = PythonOperator(
        task_id='coleta_dados',
        python_callable=coleta,
    )

    processa_dados = PythonOperator(
        task_id='processa_dados',
        python_callable=processamento,
    )

    fim_processo = PythonOperator(
        task_id='fim_processo',
        python_callable=fim,
    )

    # Encadeando as tarefas na ordem desejada
    inicio_processo >> coleta_dados >> processa_dados >> fim_processo
