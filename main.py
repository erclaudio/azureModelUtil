import json
import payloadClass
import datetime
import time
def main():
    print("Azure Model Utility is running...")
    payload = payloadClass.Payload.userPayloadBuilder()
    print("Payload object created successfully!")
    time.sleep(2)
    payload.makePayload()


if __name__ == "__main__":
    main()