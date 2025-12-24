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



