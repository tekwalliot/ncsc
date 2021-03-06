import json
import requests
import random
from datetime import datetime, timedelta
from swpsdata.models import cl_DeviceData

headers = {'Content-Type': 'text/json'}                                                                          
url = "https://nredcap-api.smartcenter.co.in/api/FarmerInstallationData"
url1 = 'https://nredcap-api.smartcenter.co.in/api/DayWiseData'                                
url2 = 'https://nredcap-api.smartcenter.co.in/api/AgencyDeviceData'                                                  
cl = "$F9C4D@Central!27^"     

serial_no=['EZMCI18120681','EZMCI19010340','EZMCI19010341','EZMCI18120697','EZMCI18120688','EZMCI18120698','EZMCI18120711','EZMCI18120684','EZMCI19010054','EZMCI18120687','EZMCI18120704','EZMCI18120713','EZMCI18120682','EZMCI18120708','EZMCI19010337','EZMCI19010343','EZMCI18120693','EZMCI19010344','EZMCI19010339','EZMCI19010347','EZMCI19010358','EZMCI19010348','EZMCI19010345','EZMCI19010383','EZMCI19010391','EZMCI19010357','EZMCI19010349','EZMCI19010353','EZMCI19010390','EZMCI19010350','EZMCI19010351','EZMCI19010402','EZMCI19010388','EZMCI19010346','EZMCI19010389','EZMCI19010356','EZMCI18120715','EZMCI18120712','EZMCI18120699','EZMCI19010392','EZMCI18120686','EZMCI18120694','EZMCI18120689','EZMCI18120714','EZMCI18120696','EZMCI19010375','EZMCI19010369','EZMCI18120691','EZMCI19010376','EZMCI19010367','EZMCI19010382','EZMCI18120778','EZMCI18120710','EZMCI19010342','EZMCI19010372','EZMCI18120683','EZMCI19010363','EZMCI18120706','EZMCI18120716','EZMCI19010377','EZMCI18120707','EZMCI19010338','EZMCI19010381','EZMCI19010387','EZMCI19010366','EZMCI19010362','EZMCI19010378','EZMCI19010379','EZMCI19010374','EZMCI19010361','EZMCI19010360','EZMCI18120705','EZMCI18120717','EZMCI18120695','EZMCI19010373','EZMCI19010395','EZMCI19010371','EZMCI19010385','EZMCI19010384','EZMCI19010380','EZMCI19010370','EZMCI19010364','EZMCI19010365','EZMCI19010410']                                                                                                                                                     

for i in range(len(serial_no)):
  try:
     a = cl_DeviceData.objects.values( ).get(devNo = serial_no[i])
     fardet = {
          "agencykey": cl,
          "first_Name": str(a['name']),
          "last_Name": ".",
          "gender": str(a['gender']),
          "dob":"{}-{}-{}".format(random.randint(1970,1988),random.randint(1,12),random.randint(1,28)),
          #"dob":str(a['dob']),
          "aadhar_No":a['adhaarNo'],
          "contactno": str(a['contactNo']),
          "address_1": str(a['address']),
          "address_2": str(a['address']),
          "village": str(a['village']),
          "mandal": str(a['mandal']),
          "district": str(a['district']),
          "pin_Code": str(a['pincode']),
          "purchase_Order_Number": a['poNo'],
          "longitude": str(a['longitude']),
          "latitude": str(a['latitude']),
          "deviceid": str(a['devNo']),
          "mfg": "Ecozen",
          #"mfg": "Kirlosker",
          #"mfg": str(a['conMake'] ),
          "sno": str(a['devNo']) ,
          "controller_Capacity": "5HP",
          "controller_Version": "",
          "no_Of_Stages": "7",
          "type": "AC",
          "aC_Voltage": 415,
          "aC_Current": 9.5,
          "date_Of_Installation": str(a['dateInst']),
          #"installer_Name": str(a['InstName']),
          "installer_Name": "Central Electronics Ltd",
          "installer_Serial_No": 0,
          #"motor_Manufacturer": str(a['pumpMfg']),
          "motor_Manufacturer": "Ecozen",
          #"motor_Manufacturer": "Kirlosker",
          "motor_Depth": 150,
          "motor_Capacity": "5 HP",
          "controller_Motor_Distance": 20,
          "no_of_Panels_in_series": 16,
          "no_of_Panels_in_Parallal":  1,
          "panel_Wattage": 300,
          "total_Power": 4800,
          "voc": 720,
          "vmp": 576,
          "imp": 8.4, 
	     "isc": 9.3,
          "rotating_Frequency": "50 Hz",
          "controllerPowerCapacity": "4.8 KW",
          "solarDCV": 750,
          "pvModuleMake": "Central Electronics Ltd",
          #"pvModuleMake": str(a['pvMake']),
     }

     data = json.dumps(fardet)
     r = requests.post(url,data=data,headers=headers)
     print(i,r.status_code,r.text)
  except Exception as e:
       print(i,e)