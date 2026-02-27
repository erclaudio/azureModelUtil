class ModelInvoker:
    def __init__(self,client, payloadPath):
        self.client = client
        self.response = client.online_endpoints.invoke(
            endpoint_name="endpoint-02261441765725",
            deployment_name="blue",
            request_file=payloadPath
        )
    def getRespone(self):
        if self.response == [1]:
            return("Has Diabetes")
        else: 
            return("Doesn't have diabetes")