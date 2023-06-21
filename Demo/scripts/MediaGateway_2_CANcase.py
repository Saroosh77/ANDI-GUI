from time import sleep

def on_can_msg_received(msg):
    print("Received following message from the CAncase: {0}".format(msg.can_header.message_id))

g_can_msg.on_message_received += on_can_msg_received
g_can_msg.start_capture()

sleep(1)

print("Ready to capture CAN messages over CANcase")

g_can_msg.can_header.message_id = 0x101
g_can_msg.can_header.length = 10
g_can_msg.payload = System.Array[Byte]((0,100))

print("Sending CAN message to MediaGateway CAN channel A")
g_can_msg.send()

sleep(2)

g_can_msg.stop_capture()
g_can_msg.on_message_received -= on_can_msg_received