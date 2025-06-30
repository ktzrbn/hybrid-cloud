import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient

# Load environment variables from .env file
load_dotenv()

# Get subscription ID from environment variable
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
if not subscription_id:
    raise ValueError("AZURE_SUBSCRIPTION_ID environment variable is required")

resource_group_name = "hcloud" # you can change this name if needed
location = "eastus"
storage_account_name = "hcloud" + str(abs(hash(resource_group_name)))[:8] # Ensure the name is unique and valid by adding random digits to the name

# Create a .env file and a .gitignore file
# .env file should contain: AZURE_SUBSCRIPTION_ID=your_subscription_id_here
# .gitignore file should contain: .env and *.env

# Set the environment variable in your terminal or IDE:
# export AZURE_SUBSCRIPTION_ID=your_subscription_id_here

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()

# Initialize Resource Manager client
resource_client = ResourceManagementClient(credential, subscription_id)

# Create Resource Group
print(f"Creating resource group '{resource_group_name}' in '{location}'...")
resource_group = resource_client.resource_groups.create_or_update(
    resource_group_name,
    {"location": location}
)
print(f"Resource Group created: {resource_group.name}")

# Initialize Storage Account client
storage_client = StorageManagementClient(credential, subscription_id)

# Create Storage Account
print(f"Creating storage account '{storage_account_name}'...")
poller = storage_client.storage_accounts.begin_create(
    resource_group_name,
    storage_account_name,
    {
        "location": location,
        "sku": {"name": "Standard_LRS"},
        "kind": "StorageV2"
    }
)
storage_account = poller.result()
print(f"Storage Account created: {storage_account.name}")

# Later, for blob operations, you'd use BlobServiceClient
# blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=credential)
# container_client = blob_service_client.get_container_client("mycontainer")
