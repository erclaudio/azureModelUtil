import json
import payloadClass
import datetime
import time
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import modelInvoker
def main():
                                                #first: subscription ID,                 second: resource group name   third: workspace name
    mlClient= MLClient(DefaultAzureCredential(),"686c0da9-2882-4cc2-925d-dda350e5b6c7","rg-dp100-l4067ea96eedb4b81a4","mlw-dp100-l4067ea96eedb4b81a4")
    print("Azure Model Utility is running...")
    payload = payloadClass.Payload.userPayloadBuilder()
    print("Payload object created successfully!")
    time.sleep(2)
    payload.makePayload()
    time.sleep(1)
    print("Invoking the model endpoint with the user payload...")
    response = modelInvoker.ModelInvoker(mlClient,payload.getPayloadPath())
    print(response.getRespone)
 

if __name__ == "__main__":
    main()