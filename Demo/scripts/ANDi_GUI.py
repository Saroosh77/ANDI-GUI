from globals import *
from time import sleep

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("System")

from System.Windows.Forms import Application, Form, TableLayoutPanel, Button, DockStyle, MessageBox,TableLayoutStyleCollection,TableLayoutStyle,TableLayoutColumnStyleCollection,Label,TextBox,CheckBox,BorderStyle,ScrollBars,FormBorderStyle
from System.Drawing import Color,Point,Font,FontStyle,ContentAlignment

from System import *

# --- Functions


class GUI_Dialog(Form):


        def __init__(self, width, height,text):

                self.Text = text
                self.Width = width
                self.Height = height
                


                l_tbl_content_panel = TableLayoutPanel()
                l_tbl_content_panel.AutoSize = True
                l_tbl_content_panel.Dock = DockStyle.Fill
                l_tbl_content_panel.AutoScroll = True

                self.panel_right = TableLayoutPanel()
                self.panel_right.Dock = DockStyle.Fill
                self.panel_right.BackColor = Color.SkyBlue

                self.lbl_sender = self.label_f1("ANDi GUI")
                self.lbl_sender = self.label_f1("By Muhammad Saroosh Asif and Babak Hosseini")
                self.lbl_sender = self.label_f1("")
                self.btn_iCAM = self.create_button("Send Packages", self.on_click_btn_Sender)
                self.btn_satCam = self.create_button("Reciever", self.on_click_reciever)
                self.btn_CAN = self.create_button("CAN Reader", self.on_click_btn_CAN)

                l_tbl_content_panel.Controls.Add(self.panel_right, 0,0)

                self.Controls.Add(l_tbl_content_panel)
                
                self.CenterToScreen()
       
        #Methods for label o form 1 
        def label_f1(self,label_name):
                label1=Label()
                label1.Name=label_name
                label1.Height=40
                label1.Width=1000
                label1.Text=label_name
                label1.TextAlign=ContentAlignment.MiddleLeft
                label1.Parent = self.panel_right
                label1.Location = Point(84,69)
                    
                label1.Font=Font("SimSun-ExtB",24,FontStyle.Bold,)
                return label1

   
        #Method to create a label 
        def label_creater_sender(label_name):
                label2=Label()
                label2.Name="Mac_address"
                label2.Height=40
                label2.Width=200
                label2.Text=label_name
                label2.BorderStyle=BorderStyle.Fixed3D
                label2.TextAlign=ContentAlignment.MiddleLeft
                    
                    
                label2.Font=Font("Courier New",10,FontStyle.Bold)
                return label2
                pass

        #Method to create a button 
        def create_button(self, name, listener):
                btn = Button()
                btn.Click += listener
                btn.Text = name
                btn.Parent = self.panel_right
                btn.Width = 170
                btn.Height = 65
                btn.Font = Font("Sitka Subheading Semibold", 14, FontStyle.Regular)
                return btn
                
        #PACKET SENDER
        def on_click_btn_Sender(self, sender, args):
                
                
                #Packet Sender Form
                f2=Form()
                f2.Text="Send Packages"
                f2.Width=900
                f2.Height=550
                f2.BackColor=Color.SkyBlue
                f2.MaximizeBox=False
                f2.FormBorderStyle=FormBorderStyle.Fixed3D
                right_panel=TableLayoutPanel()
                #right_panel.Dock=DockStyle.Fill
                right_panel.BackColor=Color.SkyBlue
                right_panel.AutoScroll=True
                right_panel.AutoSize=True
                right_panel.Dock=DockStyle.Fill  
                right_panel.BorderStyle=BorderStyle.Fixed3D
                right_panel.ColumnCount=2
                right_panel.RowCount=6
                
                
                    
                 #Method to create a label 
                def label_creater_sender(label_name):
                    label3=Label()
                    label3.Name="Mac_address"
                    label3.Height=40
                    label3.Width=200
                    label3.Text=label_name
                    label3.BorderStyle=BorderStyle.Fixed3D
                    label3.TextAlign=ContentAlignment.MiddleLeft
                    
                    
                    label3.Font=Font("Courier New",10,FontStyle.Bold)
                    return label3
                    pass
                
               #Method to create a label 
                def textbox_creater(textvalue,editable):
                    text_box=TextBox()
                    text_box.Text=textvalue
                    text_box.Height=30
                    text_box.Width=270
                    text_box.Font=Font("Courier New",10)
                    
                    text_box.ReadOnly=editable
                    return text_box
                    pass
                
               
                    
                #Method to create a CHECKBOX 
                
                def checkBox_creater(text,hearl):
                    new_checkbox=CheckBox()
                    new_checkbox.Text=text
                    new_checkbox.Height=30
                    new_checkbox.Width=190
                    new_checkbox.Click +=hearl
                    new_checkbox.Font=Font("Courier New",10,FontStyle.Bold) 
                    return new_checkbox
                    pass

  
                #Text input for dest MAC adddress
                mac_label_dest=label_creater_sender("MAC Address Destination:")
                text_box_mac_dst=textbox_creater("",False)
                right_panel.Controls.Add(mac_label_dest)
                right_panel.Controls.Add(text_box_mac_dst)
                
 
                #Text input for source MAC adddress
                mac_label_src=label_creater_sender("MAC Address Source:")
                text_box_mac_src=textbox_creater("",False)
                right_panel.Controls.Add(mac_label_src)
                right_panel.Controls.Add(text_box_mac_src)
                
                #Text input for dest IP adddress
                ip_label_dst=label_creater_sender("IP Address Destination:")
                text_ip_dst=textbox_creater("",False)
                right_panel.Controls.Add(ip_label_dst)
                right_panel.Controls.Add(text_ip_dst)
                
                #Text input for source IP adddress
                ip_label_src=label_creater_sender("IP Address Source:")
                text_ip_src=textbox_creater("",False)
                right_panel.Controls.Add(ip_label_src)
                right_panel.Controls.Add(text_ip_src)

                
                #Input PayLoad box
                payload_box=TextBox()
                payload_box.Text=""
               
                payload_box.Height=30
                payload_box.Width=270
                payload_box.Font=Font("Courier New",10)
                payload_label=label_creater_sender("Payload (hex):")
                right_panel.Controls.Add(payload_label)
                right_panel.Controls.Add(payload_box)
                
                #listner for clicked checkbox Ethernet
                def on_check_phy_layer(sender,args):
                    layer_2.Checked=True
                    layer_3.Checked=False
                    text_ip_dst.ReadOnly=True
                    text_ip_src.ReadOnly=True

                    pass

                    
                layer_2=checkBox_creater("Layer 2(MAC)",on_check_phy_layer)
                layer_2.Checked=True
                
                
                right_panel.Controls.Add(layer_2)
                
                #CHECKBOX IPV4
                def on_checkbox_ip(sender,args):
                    layer_3.Checked=True
                    layer_2.Checked=False
                    text_ip_dst.ReadOnly=False
                    
                    pass
                layer_3=checkBox_creater("Layer 3(IP)",on_checkbox_ip)
                
                right_panel.Controls.Add(layer_3)
                
          
                visual_box=textbox_creater("",False)
                visual_box.Width=510
                visual_box.Multiline=True
                visual_box.Height=220
                visual_box.ScrollBars=ScrollBars.Vertical
                
                right_panel.SetColumnSpan(visual_box,2)
                
                right_panel.Controls.Add(visual_box)
                

                def on_click_send(sender, args):
                    #action
                    
                    Payload=payload_box.Text
                    visual_box.Text=""
                    visual_box.Refresh()
                    visual_box.Text="Sending packets....."
                    visual_box.AppendText(str(Environment.NewLine))
                    
                    
                    #Layer 2 (MAC)
                    if layer_2.Checked==True:

                        g_ethernet_msg.payload=  System.Array[Byte](bytearray.fromhex(Payload))
                        g_ethernet_msg.mac_address_destination=text_box_mac_dst.Text
                        g_ethernet_msg.mac_address_source=text_box_mac_src.Text
                        g_ethernet_msg.send()
                        
                        visual_box.AppendText("Payload Sent via Layer 2 (MAC)")
                        
                    else:
                        #Layer 3 IPV4
                        ipv4_msg.payload=  System.Array[Byte](bytearray.fromhex(Payload))
                        ipv4_msg.ethernet_header.mac_address_source= text_box_mac_src.Text
                        ipv4_msg.ethernet_header.mac_address_destination=text_box_mac_dst.Text
                        ipv4_msg.ip_header.ip_address_source=text_ip_src.Text
                        ipv4_msg.ip_header.ip_address_destination=text_ip_dst.Text
                        ipv4_msg.send()
                        
                        visual_box.AppendText("Payload Sent via Layer 3 (IP)")
                        
                        pass
                        
                        

                    pass
                

                
                #SEND BUTTON
                
                newbtn=Button()
                newbtn.Click +=on_click_send
                newbtn.Width=160
                newbtn.Height=30
                newbtn.Text="send packet"
                right_panel.Controls.Add(newbtn)
                

                f2.Controls.Add(right_panel)

                f2.ShowDialog()
                pass

         #PACKET RECIEVER
        def on_click_reciever(self, sender, args):
                
                reciever_window=Form()
                reciever_window.Text="Reciever"
                reciever_window.Width=900
                reciever_window.Height=550
                reciever_window.FormBorderStyle=FormBorderStyle.Fixed3D
                reciever_window.MaximizeBox=False
                tbl_layout=TableLayoutPanel()
                tbl_layout.Dock=DockStyle.Fill
                tbl_layout.AutoSize=True
                tbl_layout.AutoScroll=True
                tbl_layout.BackColor=Color.SkyBlue
                tbl_layout.RowCount=3
                tbl_layout.ColumnCount=2
                
                
                def layer_2_checkbox_listener(sender,args):
                    
                    checkbox_phy_layer.Checked=True
                    checkbox_ip_layer.Checked=False
                    pass
                    
                def layer_3_checkbox_listener(sender,args):
                    
                    checkbox_phy_layer.Checked=False
                    checkbox_ip_layer.Checked=True
                    pass
                
                
                #CHECK BOX RECIEVER LAYER 2 : MAC
                checkbox_phy_layer=CheckBox()
                
                checkbox_phy_layer.Text="Layer 2(MAC)"
                checkbox_phy_layer.Height=30
                checkbox_phy_layer.Width=190
                checkbox_phy_layer.Click +=layer_2_checkbox_listener
                checkbox_phy_layer.Checked=True
                checkbox_phy_layer.Font=Font("Courier New",10,FontStyle.Bold)
                tbl_layout.Controls.Add(checkbox_phy_layer)
                
                #CHECK BOX  RECIEVER LAYER 3: IP
                checkbox_ip_layer=CheckBox()
                
                checkbox_ip_layer.Text="Layer 3 (IP)"
                checkbox_ip_layer.Height=30
                checkbox_ip_layer.Width=190
                checkbox_ip_layer.Click +=layer_3_checkbox_listener
                checkbox_ip_layer.Checked=False
                checkbox_ip_layer.Font=Font("Courier New",10,FontStyle.Bold)
                tbl_layout.Controls.Add(checkbox_ip_layer)
                
                
                #RECIEVER VISUAL BOX
                
                reciever_visual_box=TextBox()
                reciever_visual_box.Text=""
                reciever_visual_box.Width=510
                reciever_visual_box.Multiline=True
                reciever_visual_box.Height=220
                reciever_visual_box.ScrollBars=ScrollBars.Vertical
                reciever_visual_box.Font=Font("Courier New",10,FontStyle.Bold)
                
                tbl_layout.SetColumnSpan(reciever_visual_box,2)
                tbl_layout.Controls.Add(reciever_visual_box)
                

                def start_recv(sender,args):
                    if checkbox_phy_layer.Checked==True:
                        
                        reciever_visual_box.Text="Start Capturing......"
                        reciever_visual_box.AppendText(str(Environment.NewLine))
                        global on_msg_received

                        def on_msg_received(msg):

                            print ("message recd from{0}:{1} ".format(msg.mac_address_source,msg))
                            reciever_visual_box.AppendText(str(msg))
                            reciever_visual_box.AppendText(str(Environment.NewLine))
                                

                            
                        g_ethernet_msg.on_message_received+=on_msg_received
                        g_ethernet_msg.start_capture()
                        
                    if checkbox_ip_layer.Checked==True:
                        
                        reciever_visual_box.Text=""
                        reciever_visual_box.Refresh()
                        reciever_visual_box.Text="Waiting for Packets......"
                        reciever_visual_box.AppendText(str(Environment.NewLine))
                        global on_ip_msg_received
                        
                        def on_ip_msg_received(msg):

                            print ("message received from {0}:{1}".format(msg.ip_header.ip_address_source,msg,msg.payload))
                            reciever_visual_box.AppendText(str(msg))
                            reciever_visual_box.AppendText(" Payload ")
                            reciever_visual_box.AppendText(str(msg.payload))
                            reciever_visual_box.AppendText(str(Environment.NewLine))


                        ipv4_msg.on_message_received +=on_ip_msg_received
                        ipv4_msg.start_capture()

                
                
                #START BUTTON 
                start_button= Button()
                start_button.Text="Start Receiving"
                start_button.Height=30
                start_button.Width=130
                start_button.Click+=start_recv
                tbl_layout.Controls.Add(start_button)
                
                def stop_recv(sender,args):
                   
                    if checkbox_ip_layer.Checked==True:
                        ipv4_msg.stop_capture()
                        ipv4_msg.on_message_received -=on_ip_msg_received
                        pass
                    else:
                        
                        g_ethernet_msg.stop_capture()
                        g_ethernet_msg.on_message_received -=on_msg_received
                    pass
                

                #######STOP BUTTON
                stop_button= Button()
                stop_button.Text="Stop Receiving"
                stop_button.Height=30
                stop_button.Width=130
                stop_button.Click+=stop_recv
                tbl_layout.Controls.Add(stop_button)

                reciever_window.Controls.Add(tbl_layout)
                reciever_window.ShowDialog()
                
        #CAN Reader
        
        def on_click_btn_CAN(self, sender, args):
                canreciever_window=Form()
                canreciever_window.Text="CAN Reader"
                canreciever_window.Width=900
                canreciever_window.Height=550
                canreciever_window.FormBorderStyle=FormBorderStyle.Fixed3D
                canreciever_window.MaximizeBox=False
                tbl_layout=TableLayoutPanel()
                tbl_layout.Dock=DockStyle.Fill
                tbl_layout.AutoSize=True
                tbl_layout.AutoScroll=True
                tbl_layout.BackColor=Color.SkyBlue
                tbl_layout.RowCount=3
                tbl_layout.ColumnCount=3
                
                def start_send(sender,args):

                    print(speed_box.Text)
                    def on_can_msg_received(msg):
                        print("Received following message from the CAncase: {0}".format(msg.can_header.message_id))

                    g_can_msg.on_message_received += on_can_msg_received
                    g_can_msg.start_capture()

                    sleep(1)

                    print("Ready to capture CAN messages over CANcase")

                    g_can_msg.can_header.message_id = 0x101
                    g_can_msg.can_header.length = 10
                    
                    if checkbox_left.Checked==True:
                        g_can_msg.payload = System.Array[Byte]((1,int(speed_box.Text)))

                    if checkbox_stop.Checked==True:
                        g_can_msg.payload = System.Array[Byte]((0,0))

                    if checkbox_right.Checked==True:
                        g_can_msg.payload = System.Array[Byte]((2,int(speed_box.Text)))

                    print("Sending CAN message to MediaGateway CAN channel A")
                    g_can_msg.send()

                    sleep(2)

                    g_can_msg.stop_capture()
                    g_can_msg.on_message_received -= on_can_msg_received
                
                def left_checkbox_listener(sender,args):
                    
                    print ("Left")
                    checkbox_left.Checked=True
                    checkbox_stop.Checked=False
                    checkbox_right.Checked=False
                    pass
                    
                def stop_checkbox_listener(sender,args):
                    
                    print ("Stop")
                    checkbox_left.Checked=False
                    checkbox_stop.Checked=True
                    checkbox_right.Checked=False
                    pass
                    
                def right_checkbox_listener(sender,args):
                    
                    print ("Right")
                    checkbox_left.Checked=False
                    checkbox_stop.Checked=False
                    checkbox_right.Checked=True
                    pass
                    
                                
                #CHECK BOX FOR LEFT ROTATE
                checkbox_left=CheckBox()
                
                checkbox_left.Text="LEFT"
                checkbox_left.Height=30
                checkbox_left.Width=190
                checkbox_left.Checked=False
                checkbox_left.Click +=left_checkbox_listener
                checkbox_left.Font=Font("Courier New",10,FontStyle.Bold)
                tbl_layout.Controls.Add(checkbox_left)
                
                                
                #CHECK BOX FOR STOP ROTATE
                checkbox_stop=CheckBox()
                
                checkbox_stop.Text="STOP"
                checkbox_stop.Height=30
                checkbox_stop.Width=190
                checkbox_stop.Click +=stop_checkbox_listener
                checkbox_stop.Checked=True
                checkbox_stop.Font=Font("Courier New",10,FontStyle.Bold)
                tbl_layout.Controls.Add(checkbox_stop)
                
                                
                #CHECK BOX FOR RIGHT ROTATE
                checkbox_right=CheckBox()
                
                checkbox_right.Text="RIGHT"
                checkbox_right.Height=30
                checkbox_right.Width=190
                checkbox_right.Click +=right_checkbox_listener
                checkbox_right.Checked=False
                checkbox_right.Font=Font("Courier New",10,FontStyle.Bold)
                tbl_layout.Controls.Add(checkbox_right)
                
                #CHECK BOX FOR LEFT ROTATE
                speed_box=TextBox()
                
                speed_box.Text=""
                speed_box.Height=50
                speed_box.Width=70
                speed_box.Font=Font("Courier New",10,FontStyle.Bold)
                tbl_layout.Controls.Add(speed_box)
                                    
                #SEND BUTTON
                send_button= Button()
                send_button.Text="SEND"
                send_button.Height=30
                send_button.Width=130
                send_button.Click+=start_send
                tbl_layout.Controls.Add(send_button)
                
                canreciever_window.Controls.Add(tbl_layout)
                canreciever_window.ShowDialog()


Application.Run(GUI_Dialog(900, 503,"ANDi GUI"))