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

## Future Application Enhancements

The application can be extended to support additional functionality and more flexible data retrieval.

Potential improvements include:

- **Dynamic Filtering** – Allow users to filter characters by species, status, origin, gender, or location.
- **Search Parameters** – Support query parameters such as `?species=Human&status=Alive`.
- **Additional Endpoints** – Add endpoints for searching individual characters, locations, and episodes.
- **Pagination** – Allow clients to retrieve results in smaller pages.
- **Data Refresh** – Automate data collection and refresh the CSV or database periodically.
- **Database Integration** – Replace CSV storage with PostgreSQL for more scalable data management.

These enhancements would introduce application code changes, new dependencies, API behavior changes, and potentially infrastructure configuration updates.

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
- **Ingress** – Defines HTTP routing to the application.
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

### Why Does This Project Need CI/CD?

CI/CD becomes increasingly important as the application evolves and new features are introduced.

For example, future changes may include:

- Adding new search parameters to the API.
- Changing the character filtering logic.
- Introducing new REST API endpoints.
- Updating Python dependencies.
- Modifying the Dockerfile or base image.
- Changing Kubernetes resources or Helm configuration.
- Integrating a database instead of CSV storage.

Without CI/CD, these changes would require repeated manual testing and deployment. A developer could introduce a bug, break an existing endpoint, or deploy an incorrectly configured application without noticing.

The automated pipeline helps prevent these issues by validating every relevant code change before it is considered ready.

**CI/CD provides the following benefits:**

- **Automated Testing** – Ensures that new features do not break existing functionality.
- **Build Validation** – Verifies that the Docker image can be built successfully.
- **Deployment Validation** – Checks that Kubernetes resources can be deployed correctly.
- **API Validation** – Tests that the application endpoints respond as expected.
- **Faster Development** – Allows developers to introduce changes with greater confidence.
- **Reduced Human Errors** – Minimizes manual steps during testing and deployment.

As the project grows, CI/CD provides a repeatable and reliable process for delivering new application versions.

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
├── requirements-dev.txt
├── .gitignore
└── .dockerignore
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
