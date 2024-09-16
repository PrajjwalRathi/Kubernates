## Overview

This repository contains services that need to be deployed to a local Kubernetes cluster and tested to ensure proper communication between the frontend and backend services. Follow the steps below to set up the environment, deploy the services, and run the automated tests.

## Prerequisites

Before you start, make sure you have the following installed:

1. **Docker**: To build and run containerized applications.
2. **Kubernetes**: You can use Minikube or Kind for a local Kubernetes cluster.
3. **kubectl**: The command-line tool to interact with the Kubernetes cluster.
4. **Python**: For writing and running the automated test script.
5. **pytest**: Python testing framework (for running the test script).

## Setup and Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/Vengatesh-m/qa-test
cd qa-test
```

### 2. Start Minikube

If you are using Minikube:

```bash
minikube start
```

### 3. Deploy Services

Make sure you have the Kubernetes manifests for your services in the repository. Apply the manifests using `kubectl`:

```bash
kubectl apply -f kubernetes/
```

This command will deploy all the services defined in the `kubernetes` directory.

### 4. Verify Deployment

Ensure that all pods are running:

```bash
kubectl get pods
```

Check if the frontend and backend services are exposed:

```bash
kubectl get svc
```

### 5. Access the Frontend

Get the URL for the frontend service. For Minikube:

```bash
minikube service frontend --url
```

Open `http://localhost:8080` in your web browser. You should see the greeting message fetched from the backend.

## Automated Testing

### 1. Install Dependencies

Make sure you have Python and `pytest` installed. You can install `pytest` using pip:

```bash
pip install pytest requests
```

### 2. Create Test Script

Create a file named `test.py` with the following content:

```python
import requests

def test_frontend_backend_integration():
    frontend_url = url  # Update with the correct URL if needed

    response = requests.get(frontend_url)
    
    assert response.status_code == 200
    assert 'Greeting message' in response.text  # Update this to match the actual message
```

### 3. Run Tests

Execute the test script using `python3 test.py`:

```bash
pytest test_integration.py
```