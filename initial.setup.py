# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Create a simple index file to make sure the web server functions
echo "<h1>Howdy!</h1>" > index.html

# Check the server
python -m http.server 8000 

# Install Azure SDK for Python
pip install azure-identity azure-mgmt-resource azure-memt-storage azure-storage-blob 

# Download Azure CLI 
# This example assumes MacOS, but you can download the CLI for other platforms as well via the Azure website. Here's I'll use Homebrew to install it
brew install azure-cli

# Login to Azure CLI
az login

# This will open a web browser 
# and prompt you to log in with your Azure credentials

# You wil then need to register the Microsoft.Storage namespace using 
az provider register --namespace Microsoft.Storage
# This step is necessary to ensure that you can create and manage Azure Storage resources.
# You can check the registration status with:
az provider show --namespace Microsoft.Storage --query "registrationState"

# After registration is complete, you can continue setup by running python3 azure_manager.py 