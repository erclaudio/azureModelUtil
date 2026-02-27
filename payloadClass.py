import datetime
import json
class Payload:

    def __init__(self, pregnancies, plasmaGlucose, diastolicBloodPressure, tricepsThickness, serumInsulin, bmi, diabetesPedigree, age ):
        self.pregnancies = pregnancies
        self.plasmaGlucose = plasmaGlucose
        self.diastolicBloodPressure = diastolicBloodPressure
        self.tricepsThickness = tricepsThickness
        self.serumInsulin = serumInsulin
        self.bmi = bmi
        self.diabetesPedigree = diabetesPedigree
        self.age = age
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.payloadPath = f"payloads/payload_{self.timestamp}.json"
       
      
    @classmethod  
    def userPayloadBuilder(cls):
        pregnancies = int(input("Enter number of pregnancies: "))
        plasmaGlucose = int(input("Enter plasma glucose level: "))
        diastolicBloodPressure = int(input("Enter diastolic blood pressure: "))
        tricepsThickness = int(input("Enter triceps thickness: "))
        serumInsulin = int(input("Enter serum insulin level: "))
        bmi = float(input("Enter BMI: "))
        diabetesPedigree = float(input("Enter diabetes pedigree function: "))
        age = int(input("Enter age: "))
        return cls(pregnancies, plasmaGlucose, diastolicBloodPressure, tricepsThickness, serumInsulin, bmi, diabetesPedigree, age)
        
    def printObject(self):
        print("Payload Object:")
        print(f"Pregnancies: {self.pregnancies}")
        print(f"Plasma Glucose: {self.plasmaGlucose}")
        print(f"Diastolic Blood Pressure: {self.diastolicBloodPressure}")
        print(f"Triceps Thickness: {self.tricepsThickness}")
        print(f"Serum Insulin: {self.serumInsulin}")
        print(f"BMI: {self.bmi}")
        print(f"Diabetes Pedigree Function: {self.diabetesPedigree}")
        print(f"Age: {self.age}")

    def payloadArray(self):
        return [self.pregnancies, self.plasmaGlucose, self.diastolicBloodPressure, self.tricepsThickness, self.serumInsulin, self.bmi, self.diabetesPedigree, self.age] 
    
    def toPayloadFormat(self):
        columns = ["Pregnancies",
                    "PlasmaGlucose",
                    "DiastolicBloodPressure",
                    "TricepsThickness",
                    "SerumInsulin",
                    "BMI",
                    "DiabetesPedigree",
                    "Age"]
        index = [1]
        values = [self.payloadArray()]
        return {
            "input_data":
            {"columns": columns,
             "index": index,
             "data": values
        }}
    
    def makePayload(self):
        data = self.toPayloadFormat()
        with open(f'payloads/payload_{self.timestamp}.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
            print(f"Payload has been saved to payload_{self.timestamp}.json")

    def getPayloadPath(self):
        return self.payloadPath



    