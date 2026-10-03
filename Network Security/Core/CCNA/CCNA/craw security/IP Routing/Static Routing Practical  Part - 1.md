![image1](../../attachments/6c85f63cc870497fb3fba4ce2ecca523.png)

# 
# Router 0

Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 20.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex

Router(config)#
Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 10.0.0.1 255.0.0.0
Router(config-if)#no shutdown
# 
# Router 1 
# 
Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 10.0.0.2 255.0.0.0
Router(config-if)#no shutdown

Router(config)#ip route 20.0.0.0 255.0.0.0 10.0.0.1
# 
# Pc 0 

Set default gateway too
Which the ip of router of your network connecting the other network

![image2](../../attachments/fba06827f09b432a9de043709566ac88.png)
# 
# 
# Pc 1
![image3](../../attachments/99ffa75b39724dddb3866111a870c179.png)

![image4](../../attachments/e5c5931e792b4d2681718d41c25f80a6.png)

