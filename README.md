# Python Azure Functions with GitHub Actions

This repository demonstrates a simple Python Azure Functions application with automated CI/CD using GitHub Actions.

## Features

- **HTTP Trigger Function**: A simple HTTP-triggered Azure Function that responds to GET and POST requests
- **GitHub Actions CI**: Automated testing and validation on pull requests and pushes
- **GitHub Actions CD**: Automated deployment to Azure Functions
- **Testing**: Unit tests using pytest with coverage reporting

## Project Structure

```
.
├── HttpTrigger/              # Azure Function (HTTP Trigger)
│   ├── __init__.py          # Function implementation
│   └── function.json        # Function configuration
├── tests/                    # Unit tests
│   └── test_http_trigger.py
├── .github/
│   └── workflows/
│       ├── python-ci.yml            # CI workflow
│       └── azure-functions-deploy.yml  # CD workflow
├── host.json                # Function app host configuration
├── local.settings.json      # Local development settings
└── requirements.txt         # Python dependencies
```

## Prerequisites

- Python 3.9 or higher
- Azure Account with an Azure Functions App created
- Azure Functions Core Tools (for local development)

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Archbas-Ch/test-py-gh-action-az.git
   cd test-py-gh-action-az
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pip install pytest pytest-cov
   pytest tests/ -v
   ```

4. Run the function locally (requires Azure Functions Core Tools):
   ```bash
   func start
   ```

5. Test the function:
   ```bash
   # Without parameters
   curl http://localhost:7071/api/HttpTrigger
   
   # With name parameter
   curl "http://localhost:7071/api/HttpTrigger?name=YourName"
   ```

## GitHub Actions Setup

### CI Workflow (python-ci.yml)

Automatically runs on pull requests and pushes to main:
- Tests against Python 3.9, 3.10, and 3.11
- Runs unit tests with coverage reporting

### CD Workflow (azure-functions-deploy.yml)

Deploys to Azure Functions on push to main branch.

**Setup Steps:**

1. Create an Azure Function App in the Azure Portal
2. Download the publish profile from your Function App in Azure Portal
3. Add the following secrets to your GitHub repository:
   - `AZURE_FUNCTIONAPP_PUBLISH_PROFILE`: The publish profile content

4. Update the workflow file `.github/workflows/azure-functions-deploy.yml`:
   - Set `AZURE_FUNCTIONAPP_NAME` to your function app name
   - Adjust `PYTHON_VERSION` if needed (default: 3.11)

## Function Endpoint

Once deployed, your function will be available at:
```
https://<your-function-app-name>.azurewebsites.net/api/HttpTrigger?name=YourName
```

## Testing

Run tests locally:
```bash
pip install pytest pytest-cov
pytest tests/ -v --cov=HttpTrigger
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure everything works
5. Submit a pull request

## License

MIT License