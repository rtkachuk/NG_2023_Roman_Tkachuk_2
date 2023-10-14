import utils
import json

computer = {
    "CPU": "Ryzen-12500f",
    "RAM": "Hynix-1Tb",
    "Motherboard": "ASUS-M1",
    "HDD": "Hitachi SSD",
    "RamAmount": 1,
    "isWorking": True,
    "GPU": "RivaTNT-8Mb"
}

print ("Gpu: " + computer["GPU"])
utils.drawLine()
print ("Change GPU To Radeon-6500HD RTX")
computer["GPU"] = "Radeon-6500HD RTX"
print ("Now your GPU: " + computer["GPU"])
utils.drawLine()
print ("Your dictionary: ")
print (computer)
utils.drawLine()

cpuDetails = {
    "Name": "Ryzen-12500f",
    "Manufacturer": "AMtel",
    "Architecture": "Amt-128",
    "Socket": "Socket-III"
}

computer["CPUDetails"] = cpuDetails

print ("Dictionary in dictionary: ")
print (computer)
print ("CPU Manufacturer: " + computer["CPUDetails"]["Manufacturer"])
print ("Prettify :3")
print (json.dumps(computer, indent=4))
utils.drawLine()
print ("Remove elements")
del computer["isWorking"]
print (json.dumps(computer, indent=4))
utils.drawLine()
print ("Show all keys from dictionary :3")
for key in computer.keys():
    print (key)
print ("Show all values :3")
for value in computer.values():
    print (value)