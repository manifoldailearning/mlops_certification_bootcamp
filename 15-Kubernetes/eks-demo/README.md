# Installation
- Configure the cli with : `aws configure`
- Install eksctl - https://eksctl.io/installation/

```bash
- Create Kubernetes cluster

chmod +x create-eks-cluster.sh
./create-eks-cluster.sh


eksctl delete cluster --name demo-eks --region us-east-1
```

# Demo 2
- Create ECR 
- Push Docker Image to ECR