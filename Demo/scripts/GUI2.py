# --- Imports

from globals import *

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, TableLayoutPanel, Button, DockStyle, MessageBox
from System.Drawing import Color
from time import sleep


# --- Functions


class GUI_Dialog(Form):


        def __init__(self, width, height):

                self.Text = "GUI MENU"
                self.Width = width
                self.Height = height


                l_tbl_content_panel = TableLayoutPanel()
                l_tbl_content_panel.AutoSize = True
                l_tbl_content_panel.Dock = DockStyle.Fill
                l_tbl_content_panel.AutoScroll = True

                self.panel_right = TableLayoutPanel()
                self.panel_right.Dock = DockStyle.Fill
                self.panel_right.BackColor = Color.LightGray

                self.btn_iCAM = self.create_button("Send", self.on_click_btn_send)
                self.btn_satCam = self.create_button("Show Message", self.on_click_btn_show_message)
                self.btn_satCam = self.create_button("Receive", self.on_click_btn_receive)

                l_tbl_content_panel.Controls.Add(self.panel_right, 0,0)

                self.Controls.Add(l_tbl_content_panel)
                self.CenterToScreen()


        def create_button(self, name, listener):
                btn = Button()
                btn.Click += listener
                btn.Text = name
                btn.Parent = self.panel_right
                btn.Width = 160
                btn.Height = 35
                return btn

        def on_click_btn_send(self, sender, args):
                custom_mac = "11:22:33:44:55:66"

                def on_eth_msg_received(msg):
                    if msg.mac_address_source == custom_mac:
                        print("Received following message from {0}: {1}".format(custom_mac, msg))


                g_ethernet_msg.mac_address_source = custom_mac
                g_ethernet_msg.mac_address_destination = Logging.get_mac()

                g_ethernet_msg.payload = System.Array[Byte](bytearray.fromhex("01 02 03 04 09"))

                g_ethernet_msg.on_message_received += on_eth_msg_received
                g_ethernet_msg.start_capture()

                sleep(1)

                g_ethernet_msg.send()

                sleep(1)

                g_ethernet_msg.stop_capture()
                g_ethernet_msg.on_message_received -= on_eth_msg_received
                

        def on_click_btn_show_message(self, sender, args):
                MessageBox.Show(msg)
               


                
        def on_click_btn_receive(self, sender, args):
            
                
                def on_eth_msg_received(msg):
                    print("Received following message from {0}".format(msg))
                
               
                ethernet_msg_1.on_message_received += on_eth_msg_received


                ethernet_msg_1.start_capture()
                


                sleep(15)


                ethernet_msg_1.stop_capture()


                ethernet_msg_1.on_message_received -= on_eth_msg_received
                

                

                


#----  MAIN  ----#

Application.Run(GUI_Dialog(250, 250))