from time import sleep

def on_eth_msg_received(msg):
        print("Received following message from {0}".format(msg))


ethernet_msg_1.on_message_received += on_eth_msg_received


ethernet_msg_1.start_capture()

sleep(20)


ethernet_msg_1.stop_capture()

ethernet_msg_1.on_message_received -= on_eth_msg_received
