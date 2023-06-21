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
                self.panel_right.BackColor = Color.LightSlateGray

                self.lbl_sender = self.label_f1("ANDi GUI")
                self.btn_iCAM = self.create_button("Send Packages", self.on_click_btn_Sender)
                self.btn_satCam = self.create_button("Reciever", self.on_click_reciever)
                self.btn_CAN = self.create_button("CAN Reader", self.on_click_btn_CAN)

                l_tbl_content_panel.Controls.Add(self.panel_right, 0,0)

                self.Controls.Add(l_tbl_content_panel)
                
                self.CenterToScreen()
       
        #Methods for label o form 1 
        def label_f1(self,label_name):
                newlab=Label()
                newlab.Name=label_name
                newlab.Height=40
                newlab.Width=185
                newlab.Text=label_name
                newlab.TextAlign=ContentAlignment.MiddleLeft
                newlab.Parent = self.panel_right
                newlab.Location = Point(84,69)
                    
                newlab.Font=Font("SimSun-ExtB",24,FontStyle.Bold,)
                return newlab

   
        #Method to create a label 
        def label_creater_sender(label_name):
                newlab=Label()
                newlab.Name="Mac_address"
                newlab.Height=40
                newlab.Width=200
                newlab.Text=label_name
                newlab.BorderStyle=BorderStyle.Fixed3D
                newlab.TextAlign=ContentAlignment.MiddleLeft
                    
                    
                newlab.Font=Font("Courier New",10,FontStyle.Bold)
                return newlab
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
                
        #listner for send Packets buttons on main form
        def on_click_btn_Sender(self, sender, args):
                
                
                #Packet Sender Form
                f2=Form()
                f2.Text="Send Packages"
                f2.Width=900
                f2.Height=550
                f2.BackColor=Color.LightSlateGray
                f2.MaximizeBox=False
                f2.FormBorderStyle=FormBorderStyle.Fixed3D
                right_panel=TableLayoutPanel()
                #right_panel.Dock=DockStyle.Fill
                right_panel.BackColor=Color.LightSlateGray
                right_panel.AutoScroll=True
                right_panel.AutoSize=True
                right_panel.Dock=DockStyle.Fill  
                right_panel.BorderStyle=BorderStyle.Fixed3D
                right_panel.ColumnCount=2
                right_panel.RowCount=6
                
                
                    
                 #Method to create a label 
                def label_creater_sender(label_name):
                    newlab=Label()
                    newlab.Name="Mac_address"
                    newlab.Height=40
                    newlab.Width=200
                    newlab.Text=label_name
                    newlab.BorderStyle=BorderStyle.Fixed3D
                    newlab.TextAlign=ContentAlignment.MiddleLeft
                    
                    
                    newlab.Font=Font("Courier New",10,FontStyle.Bold)
                    return newlab
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

  
                #Text input for MAC adddress
                mac_label_dest=label_creater_sender("MAC Address Destination:")
                text_box_mac_dst=textbox_creater("",False)
                right_panel.Controls.Add(mac_label_dest)
                right_panel.Controls.Add(text_box_mac_dst)
                
 
                #Text input for MAC adddress
                mac_label_src=label_creater_sender("MAC Address Source:")
                source_mac=Stimulation.get_mac()
                text_box_mac_src=textbox_creater(source_mac,True)
                right_panel.Controls.Add(mac_label_src)
                right_panel.Controls.Add(text_box_mac_src)
                

                ip_label_dst=label_creater_sender("IP Address Destination:")
                text_ip_dst=textbox_creater("",True)
                right_panel.Controls.Add(ip_label_dst)
                right_panel.Controls.Add(text_ip_dst)
                
                
                ip_label_src=label_creater_sender("IP Address Source:")
                source_ip=Stimulation.get_ip()
                
                text_ip_src=textbox_creater(source_ip,True)
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
                    
                    
                    print  (str(layer_2.Checked))
                    pass
                    
                
                    
                layer_2=checkBox_creater("Layer 2(MAC)",on_check_phy_layer)
                layer_2.Checked=True
                
                
                right_panel.Controls.Add(layer_2)
                
                ######################################CHECKBOX IPV4
                def on_checkbox_ip(sender,args):
                    layer_3.Checked=True
                    layer_2.Checked=False
                    text_ip_dst.ReadOnly=False
                    print ("ipcheck")
                    pass
                layer_3=checkBox_creater("Layer 3(IP)",on_checkbox_ip)
                
                right_panel.Controls.Add(layer_3)
                
                ######################################### VISUALIZER BOX
                
                
                
                visual_box=textbox_creater("",False)
                visual_box.Width=510
                visual_box.Multiline=True
                visual_box.Height=220
                visual_box.ScrollBars=ScrollBars.Vertical
                
                right_panel.SetColumnSpan(visual_box,2)
                
                right_panel.Controls.Add(visual_box)
                
                
                ########################################SEND BUTTON LISTNER
                def on_click_send(sender, args):
                    #action
                    
                    Payload=payload_box.Text
                    visual_box.Text=""
                    visual_box.Refresh()
                    visual_box.Text="Sending packets....."
                    visual_box.AppendText(str(Environment.NewLine))
                    

                    #################################### PHY OR NETWROK LAYER CHECKER
                    if layer_2.Checked==True:
                        #Layer 2 (MAC)
                        g_ethernet_msg.payload=  System.Array[Byte](bytearray.fromhex(Payload))
                        g_ethernet_msg.mac_address_destination=text_box_mac_dst.Text
                        g_ethernet_msg.mac_address_source=text_box_mac_src.Text
                        global eth_list
                        eth_list=[]
                        ethernet_visualData=str(g_ethernet_msg)
                        
                        def on_time_elapsed(a,b):
                            global eth_list
                            
                            eth_list.append(ethernet_visualData)
                            
                            g_ethernet_msg.send()
                            pass
                            
                        g_timer_1.on_time_elapsed +=on_time_elapsed
                        g_timer_1.interval=1000
                        g_timer_1.start()
                        sleep(8)
                        g_timer_1.stop()
                        for x in eth_list:
                            visual_box.AppendText(x)
                            visual_box.AppendText(str(Environment.NewLine))
                            
                            
                            pass
                            
                        g_timer_1.on_time_elapsed -=on_time_elapsed
                        visual_box.AppendText("complete......(100%)")
                    else:
                        #Layer 3 IPV4
                        ipv4_msg_1.payload=  System.Array[Byte](bytearray.fromhex(Payload))
                        ipv4_msg_1.ethernet_header.mac_address_source= text_box_mac_src.Text
                        ipv4_msg_1.ethernet_header.mac_address_destination=text_box_mac_dst.Text
                        ipv4_msg_1.ip_header.ip_address_source=text_ip_src.Text
                        ipv4_msg_1.ip_header.ip_address_destination=text_ip_dst.Text
                        
                        visualData=str(ipv4_msg_1)
                        global msg_list
                        msg_list=[]
                        

                            
                        #ON TIME ELAPSED
                        
                        def on_time_elapsed(a,b):
                            
                            global msg_list
                            
                            
                            
                            #SENDING PACKETS
                            msg_list.append(visualData)
                            ipv4_msg_1.send()
                            #visual_box.Text=visualData
                            #visual_box.AppendText(str(Environment.NewLine))
                            pass
                            
    
                        g_timer_1.on_time_elapsed += on_time_elapsed
                        g_timer_1.interval= 1000
                        
                        g_timer_1.start()
                        
                        sleep(6)
                        g_timer_1.stop()
                        
                        #DISPLAYING PACKET INFO ON VISUAL TEXTBOX
                        for x in msg_list:
                            visual_box.AppendText(x)
                            visual_box.AppendText(str(Environment.NewLine))
                            
                            
                            pass
                        
                        g_timer_1.on_time_elapsed -=on_time_elapsed
                        visual_box.AppendText("complete......(100%)")
                        
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

        def on_click_reciever(self, sender, args):
                # RECIEVER WINDOW CREATION
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
                tbl_layout.BackColor=Color.LightSlateGray
                tbl_layout.RowCount=3
                tbl_layout.ColumnCount=2
                
                
                def layer_2_checkbox_listener(sender,args):
                    #Action
                    print ("test")
                    checkbox_phy_layer.Checked=True
                    checkbox_ip_layer.Checked=False
                    pass
                    
                def layer_3_checkbox_listener(sender,args):
                    print ("ip test reciver")
                    checkbox_phy_layer.Checked=False
                    checkbox_ip_layer.Checked=True
                    pass
                
                
                #CEHCK BOX RECIEVER LAYER 2 : MAC
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
                custom_mac = "00:13:3B:B0:0E:66"
                

                def start_recv(sender,args):
                    if checkbox_phy_layer.Checked==True:
                        print ("hey mac")
                        reciever_visual_box.Text="Start Capturing......"
                        reciever_visual_box.AppendText(str(Environment.NewLine))
                        global on_msg_received
                        
                        
                        
                        def on_msg_received(msg):
                            if msg.mac_address_destination==Logging.get_mac():
                                print ("message recd from{0}:{1} ".format(msg.mac_address_source,msg))
                                reciever_visual_box.AppendText(str(msg))
                                reciever_visual_box.AppendText(str(Environment.NewLine))
                                
                            pass
                            
                        g_ethernet_msg.on_message_received+=on_msg_received
                        g_ethernet_msg.start_capture()
                    else:
                        
                        print ("hello ip")
                        reciever_visual_box.Text=""
                        reciever_visual_box.Refresh()
                        reciever_visual_box.Text="Waiting for Packets......"
                        reciever_visual_box.AppendText(str(Environment.NewLine))
                        global on_ip_msg_received
                        
                        def on_ip_msg_received(msg):
                            if msg.ethernet_header.mac_address_destination==Logging.get_mac():
                                sleep(1)
                                print ("message received from {0}:{1}:{2}".format(msg.ethernet_header.mac_address_source,msg,msg.payload))
                                reciever_visual_box.AppendText(str(msg))
                                reciever_visual_box.AppendText(" Payload ")
                                reciever_visual_box.AppendText(str(msg.payload))
                                reciever_visual_box.AppendText(str(Environment.NewLine))
                                
                                
                                
                            pass
                        pass
                        
                        
                        ipv4_msg_1.on_message_received +=on_ip_msg_received
                        ipv4_msg_1.start_capture()
                        pass
     
                    pass
                
                
                #START BUTTON 
                start_button= Button()
                start_button.Text="Start Receiving"
                start_button.Height=30
                start_button.Width=130
                start_button.Click+=start_recv
                tbl_layout.Controls.Add(start_button)
                
                def stop_recv(sender,args):
                    print ("stop")
                    if checkbox_ip_layer.Checked==True:
                        ipv4_msg_1.stop_capture()
                        ipv4_msg_1.on_message_received -=on_ip_msg_received
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
                tbl_layout.BackColor=Color.LightSlateGray
                tbl_layout.RowCount=3
                tbl_layout.ColumnCount=2
                
                                def start_send(sender,args):
                    print("start")
                    
                    g_can_msg.start_capture()

                    sleep(1)

                    print("Ready to capture CAN messages over CANcase")

                    g_can_msg.can_header.message_id = 0x101
                    g_can_msg.can_header.length = 10
                    
                    if checkbox_left.checked==True:
                        g_can_msg.payload = System.Array[Byte]((1,100))

                    if checkbox_stop.checked==True:
                        g_can_msg.payload = System.Array[Byte]((0,100))

                    if checkbox_right.checked==True:
                        g_can_msg.payload = System.Array[Byte]((2,100))

                    print("Sending CAN message to MediaGateway CAN channel A")
                    g_can_msg.send()
                    
                    sleep(2)
                    print("123")
                    g_can_msg.stop_capture()
                    
                #######LEFT BUTTON
                left_button= Button()
                left_button.Text="Rotate Left"
                left_button.Height=30
                left_button.Width=130
                #left_button.Click+=stop_recv
                tbl_layout.Controls.Add(left_button)
                
                #######RIGHT BUTTON
                right_button= Button()
                right_button.Text="Rotate Right"
                right_button.Height=30
                right_button.Width=130
                #right_button.Click+=stop_recv
                tbl_layout.Controls.Add(right_button)
                
                def stop_recv(sender,args):
                    print ("stop")
                    g_can_message.stop_capture()
                    g_can_message.on_can_msg_received -= on_can_msg_received
                    pass
                
                #######STOP BUTTON
                stop_button= Button()
                stop_button.Text="Stop Receiving"
                stop_button.Height=30
                stop_button.Width=130
                stop_button.Click+=stop_recv
                tbl_layout.Controls.Add(stop_button)
                
                #######RECEIVE BUTTON
                rec_button= Button()
                rec_button.Text="Receiving from CAN"
                rec_button.Height=30
                rec_button.Width=130
                #rec_button.Click+=rec_recv
                tbl_layout.Controls.Add(rec_button)
                
                canreciever_window.Controls.Add(tbl_layout)
                canreciever_window.ShowDialog()

#MAIN FORM

Application.Run(GUI_Dialog(900, 503,"ANDi GUI"))