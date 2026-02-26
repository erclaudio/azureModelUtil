from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

mlClient= MLClient(DefaultAzureCredential(),"686c0da9-2882-4cc2-925d-dda350e5b6c7","rg-dp100-l4067ea96eedb4b81a4","mlw-dp100-l4067ea96eedb4b81a4")
