#!/bin/bash

mkdir -p logs

echo "aplicando manifiesto de Kubernetes..." | tee logs/apply.log
kubectl apply -f kubernetes/deployment.yaml >> logs/apply.log 2>&1

echo "actualizando imagen..." | tee logs/update.log
kubectl set image deployment/my-python-app app=myuser/myapp:latest >> logs/update.log 2>&1

echo "historial de despliegue:" | tee logs/history.log
kubectl rollout history deployment/my-python-app >> logs/history.log 2>&1

echo "revirtiendo despliegue..." | tee logs/rollback.log
kubectl rollout undo deployment/my-python-app >> logs/rollback.log 2>&1

echo "estado actual de pods:" | tee logs/status.log
kubectl get pods -l app=my-python-app >> logs/status.log 2>&1
