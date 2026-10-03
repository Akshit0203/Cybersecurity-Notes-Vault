![image1](../../attachments/6d89d8155442472ca2b14bdde16f6c53.png)

Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 10.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#

![image2](../../attachments/3da696ec5de94ec590dcaac471b6e9b6.png)

![image3](../../attachments/92905fd436a5406a9f3e791dd4734c40.png)

Router#
Router#configure terminal
Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 20.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#

Router(config)#
Router(config)#interface vlan 1
Router(config-if)#ip address 30.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#ex
Router#

![image4](../../attachments/8dfe6a0530534dd6bd8fe561a8cb5ab5.png)

Router#
Router#copy running-config tftp:
Address or name of remote host \[\]? 10.0.0.2
Destination filename \[Router-confg\]? jio_saket_rack4_d8

Writing running-config....!!
\[OK - 707 bytes\]

707 bytes copied in 3.004 secs (235 bytes/sec)
Router#

![image5](../../attachments/e1d45cc400474b1ea9f6c151bff5b02e.png)

INSTALL NEW ROUTER

![image6](../../attachments/f5d97c0dc2dd45949cbd3ffd67dd96fb.png)

![image7](../../attachments/902fc0832407471b9d49dc6e98561e61.png)

Router#
Router#configure terminal
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 10.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#ex
Router#

Router#
Router#copy tftp: running-config
Address or name of remote host \[\]? 10.0.0.2
Source filename \[\]? jio_saket_rack4_d8
Destination filename \[running-config\]?

Accessing tftp://10.0.0.2/jio_saket_rack4_d8....
Loading jio_saket_rack4_d8 from 10.0.0.2: !
\[OK - 707 bytes\]

707 bytes copied in 3.002 secs (235 bytes/sec)
Router#

Router#show ip interface brief
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0/0 10.0.0.1 YES manual up up
GigabitEthernet0/1 20.0.0.1 YES manual administratively down down
GigabitEthernet0/2 unassigned YES unset administratively down down
Vlan1 30.0.0.1 YES manual administratively down down
Router#

COPIED ALL THE CONFIGURATION

