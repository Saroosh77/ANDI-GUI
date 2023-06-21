from time import sleep

custom_ip = "192.168.101.57"

ipv4_msg.ip_header.ip_address_source = custom_ip
ipv4_msg.ip_header.ip_address_destination = Logging.get_ip()
print(Logging.get_ip())
ipv4_msg.payload = System.Array[Byte](bytearray.fromhex("01 02 03 04 09"))


while(True):
    ipv4_msg.send()
    sleep(1)


