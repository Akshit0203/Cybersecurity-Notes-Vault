![image1](../../attachments/6dd514607d5d496196f5fce042090a3f.png)

Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 20.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#
Router(config)#enable password 123
Router(config)#ex
Router#
Router#wr
Building configuration...
\[OK\]
Router#

Turn off the router physically and then turn it on
When decompressing image ,
Press ctrl+c
To enter romon mode

![image2](../../attachments/71ae76a53f5f4b25b029111885233abf.png)

![image3](../../attachments/ec169224d0a04aedb0e2654982bb38e9.png)

The configuration code by default is 2102
We change it so that the startup configurations are not read , when booting up

![image4](../../attachments/6e04c3accd9649af9bf291980b60fe2f.png)

Router\>enable
Router#show run
Router#show running-config

![image5](../../attachments/79cd45036b854763863c38e1288f3ab5.png)

All our configuration has been shifted to startup-config instead of running-config

![image6](../../attachments/c0a3cfac778e41bdb6ae43a3338978ef.png)

![image7](../../attachments/7020415b8a0b42ce81203ade3278bbc1.png)

![image8](../../attachments/f8dd02b8f1864539999a99999293c08a.png)

Now the startup-config commands are saved to running-config

Router#copy startup-config running-config

