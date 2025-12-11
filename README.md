# 🚀 CAPSTONE PROJECT – CLOUD-NATIVE APPLICATION DEPLOYMENT

Complete documentation covering:

- GitHub & Branching  
- Docker & Docker Compose  
- Azure ACR  
- Azure AKS (Kubernetes)  
- CI/CD Pipeline (GitHub Actions)  
- Blue-Green Deployment  
- Trivy Image Scanning  

---

# 📘 1. PROJECT OVERVIEW

This capstone project delivers a full **cloud-native microservices architecture**, using:

- **Frontend:** React  
- **Backend:** Python Flask  
- **Containerization:** Docker  
- **Image Registry:** Azure Container Registry (ACR)  
- **Orchestration:** Azure Kubernetes Service (AKS)  
- **CI/CD:** GitHub Actions  
- **Deployment Strategy:** Blue-Green (Zero Downtime)  
- **Security Scanning:** Trivy  

---

# 📁 2. GITHUB – BRANCHING & BASIC COMMANDS

### Initialize repository
```bash
git init
git remote add origin <repo-url>
```

### Create new branches
```bash
git checkout -b dev
git checkout -b main
```

### Push code
```bash
git add .
git commit -m "message"
git push origin dev
git push origin main
```

### View branches
```bash
git branch
```

---

# 🐳 3. DOCKER COMMANDS

### Build images
```bash
docker build -t backend:latest ./backend
docker build -t frontend:latest ./frontend
```

### Tag images for ACR
```bash
docker tag backend:latest <acr>.azurecr.io/backend:latest
docker tag frontend:latest <acr>.azurecr.io/frontend:latest
```

### Login to ACR
```bash
docker login <acr>.azurecr.io -u <username> -p <password>
```

### Push images
```bash
docker push <acr>.azurecr.io/backend:latest
docker push <acr>.azurecr.io/frontend:latest
```

### Multi-arch build
```bash
docker buildx build --platform linux/amd64,linux/arm64 -t <acr>.azurecr.io/backend:latest --push .
```

---

# 📦 4. DOCKER COMPOSE

### docker-compose.yml example
```yaml
version: '3'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
```

### Run
```bash
docker compose up --build
```

---

# 🛡 5. TRIVY – IMAGE SCANNING

### Install
```bash
choco install trivy
```

### Scan Docker image
```bash
trivy image backend:latest
trivy image <acr>.azurecr.io/backend:latest
```

### Scan filesystem
```bash
trivy fs .
```

---

# 🏭 6. AZURE ACR – COMMANDS

### List repositories
```bash
az acr repository list -n <acr>
```

### Attach ACR to AKS
```bash
az aks update -n <cluster> -g <rg> --attach-acr <acr>
```

---

# ☸️ 7. AZURE AKS – KUBERNETES COMMANDS

### Get AKS credentials
```bash
az aks get-credentials -n <cluster> -g <rg>
```

### Check nodes
```bash
kubectl get nodes
```

### Create namespace
```bash
kubectl create namespace capstone
```

### Create ACR pull secret
```bash
kubectl create secret docker-registry acr-secret \
  --docker-server=<acr>.azurecr.io \
  --docker-username=<username> \
  --docker-password=<password> \
  -n capstone
```

---

# 📄 8. KUBERNETES DEPLOYMENT FILES

### backend-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-deployment
  namespace: capstone
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      imagePullSecrets:
        - name: acr-secret
      containers:
        - name: backend
          image: <acr>.azurecr.io/backend:latest
          ports:
            - containerPort: 5000
```

### backend-service.yaml
```yaml
kind: Service
apiVersion: v1
metadata:
  name: backend-service
  namespace: capstone
spec:
  selector:
    app: backend
  ports:
    - port: 5000
  type: ClusterIP
```

### Apply
```bash
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
```

### Check pods
```bash
kubectl get pods -n capstone
```

---

# 🔵🟢 9. BLUE-GREEN DEPLOYMENT (Kubernetes)

### Blue (current version)
`backend-deployment-blue.yaml`

### Green (new version)
`backend-deployment-green.yaml`

### Switch traffic
```bash
kubectl apply -f service-blue.yaml
# OR
kubectl apply -f service-green.yaml
```

### Rollback
```bash
kubectl rollout undo deployment backend-deployment
```

---

# 🔁 10. CI/CD PIPELINE – GITHUB ACTIONS

Pipeline stages:

- Checkout code  
- Login to Azure  
- Build Docker Images  
- Push to ACR  
- Deploy to AKS  

Workflow file:  
`/.github/workflows/ci-cd.yaml`

---

# ✅ END OF DOCUMENTATION



