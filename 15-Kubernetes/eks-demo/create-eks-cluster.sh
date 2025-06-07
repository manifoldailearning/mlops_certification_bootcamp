#!/bin/bash

# Set variables
CLUSTER_NAME="demo-eks"
REGION="us-east-1"
NODE_TYPE="t3.small"
NODE_COUNT=2

echo "Creating EKS cluster: $CLUSTER_NAME with $NODE_COUNT x $NODE_TYPE Spot nodes in $REGION"

eksctl create cluster \
  --name $CLUSTER_NAME \
  --region $REGION \
  --version 1.30 \
  --nodegroup-name spot-nodes \
  --node-type $NODE_TYPE \
  --nodes $NODE_COUNT \
  --nodes-min $NODE_COUNT \
  --nodes-max $NODE_COUNT \
  --managed \
  --spot \
  --asg-access \
  --full-ecr-access \
  --alb-ingress-access

echo "✅ EKS cluster $CLUSTER_NAME created successfully!"
#!/bin/bash

# Set variables
CLUSTER_NAME="demo-eks"
REGION="us-east-1"
NODE_TYPE="t3.small"
NODE_COUNT=2

echo "Creating EKS cluster: $CLUSTER_NAME with $NODE_COUNT x $NODE_TYPE Spot nodes in $REGION"

eksctl create cluster \
  --name $CLUSTER_NAME \
  --region $REGION \
  --version 1.29 \
  --nodegroup-name spot-nodes \
  --node-type $NODE_TYPE \
  --nodes $NODE_COUNT \
  --nodes-min $NODE_COUNT \
  --nodes-max $NODE_COUNT \
  --managed \
  --spot \
  --asg-access \
  --full-ecr-access \
  --alb-ingress-access

echo "✅ EKS cluster $CLUSTER_NAME created successfully!"
