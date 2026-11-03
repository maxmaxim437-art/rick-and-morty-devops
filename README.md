# Rick and Morty – DevOps Project

A containerized Rick and Morty application deployed on Kubernetes using Docker and Helm, with automated testing and deployment validation through GitHub Actions.

## Overview

This project retrieves character data from the [Rick and Morty API](https://rickandmortyapi.com/), filters the characters according to specific criteria, stores the results in a CSV file, and exposes the data through a Flask web application.

The application includes a web interface for browsing characters, searching and filtering results, and checking application health.

The project demonstrates an end-to-end DevOps workflow, from data collection and application development to containerization, Kubernetes deployment, and CI/CD automation.

## Architecture

```text
Rick and Morty API
        |
        v
  Python Data Fetcher
        |
        v
  characters.csv
        |
        v
   Flask Application
        |
        v
    Docker Image
        |
        v
    Kubernetes
        |
        +------ Deployment
        |
        +------ Service
        |
        +------ Ingress
        |
        v
    Web Application
```

### CI/CD Workflow

GitHub Actions automatically validates the project:

```text
GitHub Push / Pull Request
          |
          v
    Checkout Code
          |
          v
    Setup Python
          |
          v
 Install Dependencies
          |
          v
      Run Tests
          |
          v
   Build Docker Image
          |
          v
   Create Kind Cluster
          |
          v
     Deploy with Helm
          |
          v
    Verify Deployment
          |
          v
   Test Application API
```

## Technologies

| Technology | Purpose |
|---|---|
| Python | Data collection and backend |
| Flask | Web application and REST API |
| Docker | Application containerization |
| Kubernetes | Container orchestration |
| Minikube | Local Kubernetes environment |
| Helm | Kubernetes package management |
| NGINX Ingress | HTTP routing |
| GitHub Actions | CI/CD automation |
| Kind | Kubernetes testing in CI |
| Pytest | Automated testing |

## Application Features

- Fetches character data from the Rick and Morty API.
- Filters characters by:
  - Species: Human
  - Status: Alive
  - Origin: Earth
- Exports character data to `characters.csv`.
- Provides a Flask web application.
- Displays character information and images.
- Supports searching and filtering through the interface.
- Provides application health monitoring.

### API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Main web interface |
| `/characters` | Returns character data in JSON |
| `/healthcheck` | Application health check |

## Project Structure

```text
rick-and-morty-devops/
│
├── app.py
├── main.py
├── characters.csv
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── tests/
│   ├── test_characters.py
│   └── test_healthcheck.py
│
├── helm/
│   └── rick-and-morty/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│
├── yamls/
│   └── yamls/
│       ├── Deployment.yaml
│       ├── Service.yaml
│       └── Ingress.yaml
│
└── .github/
    └── workflows/
        └── ci-cd.yaml
```

## Prerequisites

Before running the project, make sure the following tools are installed:

- Git
- Python 3.12
- Docker
- kubectl
- Minikube
- Helm

For the local Kubernetes deployment, Docker Desktop must be running if you are using the Docker driver.

## Installation and Local Development

### 1. Clone the repository

```bash
git clone https://github.com/maxmaxim437-art/rick-and-morty-devops.git

cd rick-and-morty-devops
```

### 2. Create a Python virtual environment

```bash
python3 -m venv .venv

source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

For development and testing:

```bash
pip install -r requirements-dev.txt
```

### 4. Fetch character data

```bash
python main.py
```

This script retrieves character data from the Rick and Morty API and generates `characters.csv`.

### 5. Run the application

```bash
python app.py
```

Open:

```text
http://localhost:5001
```

### 6. Run tests

```bash
python -m pytest -v
```

## Docker Deployment

### 1. Build the Docker image

```bash
docker build -t rick-and-morty-api:1.0 .
```

### 2. Run the container

```bash
docker run -d \
  --name rick-and-morty-api \
  -p 5001:5001 \
  rick-and-morty-api:1.0
```

Open:

```text
http://localhost:5001
```

To stop the container:

```bash
docker stop rick-and-morty-api
```

To remove it:

```bash
docker rm rick-and-morty-api
```

## Kubernetes Deployment with Minikube and Helm

### 1. Start Minikube

```bash
minikube start --driver=docker
```

### 2. Build the Docker image

```bash
docker build -t rick-and-morty-api:1.0 .
```

### 3. Load the image into Minikube

```bash
minikube image load rick-and-morty-api:1.0
```

### 4. Deploy using Helm

```bash
helm upgrade --install my-rick-app ./helm/rick-and-morty
```

### 5. Verify the deployment

```bash
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get ingress
```

### 6. Check the application

```bash
kubectl rollout status deployment/my-rick-app-api
```

The application is configured with an NGINX Ingress resource.

For local access, configure the Ingress hostname according to your local environment and make sure it resolves to the Minikube ingress endpoint.

## Kubernetes Configuration

The Helm chart manages the following resources and settings:

- Deployment and replica configuration.
- ClusterIP Service.
- NGINX Ingress routing.
- Readiness Probe using `/healthcheck`.
- Liveness Probe using `/healthcheck`.
- CPU and memory requests.
- CPU and memory limits.
- Configurable image repository and tag.

Configuration is managed through `helm/rick-and-morty/values.yaml`.

## CI/CD – GitHub Actions

The GitHub Actions workflow is triggered by:

- Push events to `main`.
- Pull requests targeting `main`.

The pipeline performs:

1. Repository checkout.
2. Python environment setup.
3. Dependency installation.
4. Automated test execution.
5. Docker image build.
6. Temporary Kubernetes cluster creation using Kind.
7. Helm deployment.
8. Kubernetes rollout validation.
9. HTTP endpoint verification.

The pipeline validates that the application can be built, deployed, and accessed inside a Kubernetes environment.

## Health Checks

The application exposes:

```text
GET /healthcheck
```

Expected response:

```json
{
  "status": "healthy"
}
```

Kubernetes uses this endpoint for readiness and liveness probes.

## Cleanup

To remove the Helm deployment:

```bash
helm uninstall my-rick-app
```

To stop Minikube:

```bash
minikube stop
```

## Author

**Maxim Gonik**

DevOps Engineering Project

---

*This project was built as a hands-on demonstration of Python application development, Docker containerization, Kubernetes orchestration, Helm-based deployments, and CI/CD automation.*
