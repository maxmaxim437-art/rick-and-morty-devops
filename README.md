# Rick and Morty DevOps Project

## Project Overview

A containerized Flask REST API that collects character data from the [Rick and Morty API](https://rickandmortyapi.com/), filters the results, and exposes them through HTTP endpoints.

This project demonstrates an end-to-end DevOps workflow, from data collection and application development to containerization, Kubernetes deployment, and automated CI/CD.

## Application Flow

1. **Data Collection** – `main.py` retrieves character data from the Rick and Morty API, including all available pages.
2. **Data Filtering** – Keeps only characters matching the following criteria:
   - Species: Human
   - Status: Alive
   - Origin: Earth
3. **CSV Generation** – Saves the filtered results to `characters.csv`, including character name, current location, and image.
4. **Flask REST API** – `app.py` reads the CSV and exposes:
   - `GET /characters` – Returns the filtered characters as JSON.
   - `GET /healthcheck` – Returns the application health status.

## Containerization – Docker

The application is packaged into a Docker image using a custom Dockerfile.

- Uses Python 3.12 Slim as the base image.
- Installs application dependencies.
- Copies the Flask application and generated CSV file.
- Exposes port `5001`.

## Kubernetes & Helm

The application is deployed and managed on Kubernetes using Helm.

The Helm chart includes:

- **Deployment** – Manages the application Pods and ensures the desired number of replicas.
- **Service** – Exposes the Pods internally using a stable ClusterIP endpoint.
- **Ingress** – Defines external HTTP routing to the application.
- **Values.yaml** – Centralizes deployment configuration, making it easier to customize the deployment.

Helm is used to install and manage the Kubernetes resources as a single release.

## CI/CD – GitHub Actions

An automated pipeline runs on pushes and pull requests targeting the `main` branch.

Pipeline stages:

1. Install Python dependencies.
2. Run automated tests using Pytest.
3. Build the Docker image.
4. Create a temporary Kubernetes cluster using Kind.
5. Load the Docker image into the cluster.
6. Deploy the application using Helm.
7. Wait for the Kubernetes Deployment rollout to complete.
8. Test the API endpoints using `curl`.

The pipeline validates both the application and its Kubernetes deployment.

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── helm/
│   └── rick-and-morty/
│       ├── templates/
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   └── ingress.yaml
│       ├── Chart.yaml
│       └── values.yaml
├── tests/
├── app.py
├── main.py
├── characters.csv
├── Dockerfile
├── requirements.txt
└── requirements-dev.txt
```

## Run Locally

```bash
pip install -r requirements-dev.txt
python main.py
python app.py
```

API available at `http://localhost:5001`.

## Run Tests

```bash
python -m pytest -v
```

## Technologies

Python · Flask · REST API · Docker · Kubernetes · Helm · Kind · GitHub Actions · Pytest
