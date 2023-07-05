from time import sleep

custom_mac = "6C:3C:8C:12:0D:17"

ethernet_msg_1.mac_address_source = custom_mac
ethernet_msg_1.mac_address_destination = Logging.get_mac()
ethernet_msg_1.payload = System.Array[Byte](bytearray.fromhex("01 02 03 04 09"))

count=20

while(count>0):
    ethernet_msg_1.send()
    count=count-1
    sleep(1)


