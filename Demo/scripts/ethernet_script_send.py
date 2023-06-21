from time import sleep

custom_mac = "6C:3C:8C:12:0D:17"


ethernet_msg_1.mac_address_source = custom_mac
ethernet_msg_1.mac_address_destination = Logging.get_mac()
print(Logging.get_mac())
ethernet_msg_1.payload = System.Array[Byte](bytearray.fromhex("01 02 03 04 09"))

while(True):
    
    ethernet_msg_1.send()
    sleep(1)


