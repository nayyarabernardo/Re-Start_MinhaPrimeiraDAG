# 👩🏽‍💻 Bootcamp [Re]Start - Data Girls! — Aula: Pipelines de Dados com Airflow

Seja bem-vinda! 💜

Este repositório faz parte da parte prática da aula que estou ministrando no **Bootcamp [Re]Start - Data Girls!**, com foco na construção de **pipelines de dados utilizando o Apache Airflow**.

Nesta aula, vamos trabalhar com a `primeira_dag`, uma DAG simples, mas poderosa, para você entender o funcionamento básico de tarefas no Airflow.

---

## 🎯 Objetivo da aula

- Apresentar a estrutura de uma DAG no Airflow
- Entender o ciclo de vida de uma tarefa
- Executar uma DAG localmente usando Docker
- Conhecer a interface de monitoramento do Airflow (Airflow UI)

---

## 📂 O que este repositório contém

- `dags/primeira_dag.py`: código da DAG introdutória
- `docker-compose.yaml`: configuração dos serviços do Airflow com Docker
- Este `README.md` com o passo a passo completo

---

## 🚀 Passo a passo para executar a DAG `primeira_dag` com Docker + Airflow

### ✔️ Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados no seu computador:

- [Git](https://git-scm.com/downloads)
- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop) e [Docker Compose](https://docs.docker.com/compose/)
- Sistema operacional:
  - Linux ou macOS
  - Ou **Windows com WSL2 habilitado**

---

### 🧭 Etapas para execução

#### 1. Clonar o repositório do projeto

```bash
git clone https://github.com/nayyarabernardo/Re-Start_MinhaPrimeiraDAG.git
cd -Re-Start_MinhaPrimeiraDAG
````

Neste repositório, você encontrará:

* `docker-compose.yaml`
* A pasta `dags/` com o arquivo `primeira_dag.py`

---

#### 2. Criar e ativar um ambiente virtual (recomendado)

Para manter o ambiente Python isolado:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

* **No Linux/macOS:**

  ```bash
  source venv/bin/activate
  ```

* **No Windows:**

  ```cmd
  venv\Scripts\activate
  ```

---

#### 3. Instalar o Docker

* **No Linux (Ubuntu/Debian):**

  ```bash
  sudo apt update
  sudo apt install docker.io docker-compose -y
  sudo usermod -aG docker $USER
  newgrp docker
  ```

* **No Windows:**

  * Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop)
  * Ative o WSL2 e instale uma distribuição Linux (recomendado: Ubuntu)
  * Use o terminal do Ubuntu (WSL) para rodar os comandos

---

#### 4. Subir o ambiente Airflow com Docker

Na raiz do projeto clonado, rode:

```bash
docker-compose up
```

> Na primeira execução, o Airflow será baixado e configurado. Isso pode levar alguns minutos.

---

#### 5. Acessar a interface web do Airflow

Abra seu navegador e acesse:

```
http://localhost:8080
```

Credenciais padrão:

* **Usuário:** `admin`
* **Senha:** `admin`

---

#### 6. Ativar e executar a DAG

* Na interface do Airflow, localize a DAG chamada `exemplo_airflow_simples`
* Ative a DAG (botão de ativação no canto esquerdo)
* Clique no botão ▶️ (Trigger DAG) para executar manualmente
* Clique no nome da DAG e acesse a tarefa `exemplo_airflow_simples`
* Clique no círculo colorido e selecione **View Log** para visualizar os logs de execução

Você deverá ver a seguinte mensagem no log:

```
Executando tarefa simples com Airflow!
```

Parabéns! 🎉 Você executou sua primeira DAG com sucesso!

---

#### 7. Parar o ambiente quando terminar

```bash
docker-compose down
```

---

## 🧠 Conceitos aprendidos até aqui

* O que é uma DAG no Airflow
* Como tarefas são orquestradas e monitoradas
* Como executar uma DAG usando Docker
* Como navegar pela interface do Airflow

---

## 🫶 Dúvidas?

Me chama no LinkedIn ou abra uma issue aqui no GitHub! Vamos juntas 💜

Com carinho,
**Nayara Bernardo**

```
