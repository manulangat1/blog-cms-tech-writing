kubectl apply -f  postgres_vol.yaml
kubectl apply -f  postgres-secret.yaml
kubectl apply -f postgres-depl.yaml
kubectl apply -f app-deploy.yaml