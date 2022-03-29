# FIAP Applying Analytics Arquitecture

## Grupo

* Bernardo Couto
* Raphael Freixo
* Ronaldo Nolasco

## Anaconda

Iniciando Anaconda:

```shel
$ conda init
```

Listando ambientes virtuais:

```shel
$ conda env list
```

Criando ambiente virtual:

```shel
$ conda env create --name fiap --file requirements.txt
```

Ativando ambiente virtual:

```shel
$ conda activate fiap
```

Ambiente virtual:

![Anaconda Environment](./docs/anaconda-env.png)

Anaconda Jupyter local:

![Anaconda Jupyter](./docs/anaconda-jupyter.png)

## AWS

### EC2

Instância criada no AWS EC2:

![AWS EC2 Instance](./docs/ec2-instance.png)

Consumo da Aplicação através do AWS EC2:

![AWS EC2 Application](./docs/ec2-app.png)

Acesso via SSH na instância do AWS EC2:

![AWS EC2 Terminal](./docs/ec2-terminal.png)

Inicialização do Jupyter na instência do AWS EC2:

![AWS EC2 Terminal](./docs/ec2-jupyter.png)

Acesso ao Jupyter:

![AWS EC2 Jupyter Login](./docs/ec2-jupyter-login.png)

Jupyter:

![AWS EC2 Jupyter Area](./docs/ec2-jupyter-area.png)

### ECR

Imagem do container Docker enviada para o AWS ECR:

![AWS ECR](./docs/ecr.png)

### EKS

Cluster criado no AWS EKS:

![AWS EKS Cluster](./docs/eks-cluster.png)
