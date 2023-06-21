from time import sleep

def on_eth_msg_received(msg):
        print("Received following message from {0}".format(msg))


ipv4_msg.on_message_received += on_eth_msg_received


ipv4_msg.start_capture()

sleep(150)


ipv4_msg.stop_capture()

ipv4_msg.on_message_received -= on_eth_msg_received