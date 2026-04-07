![image1](../../attachments/1073f8235a754958acc8f1da7aa4f61d.png)

# Router 1 

Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 20.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 10.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#ip route 30.0.0.0 255.0.0.0 10.0.0.1
Router(config)#ip route 60.0.0.0 255.0.0.0 30.0.0.2
Router(config)#ip route 40.0.0.0 255.0.0.0 10.0.0.1
Router(config)#ip route 50.0.0.0 255.0.0.0 40.0.0.2

# Router 2 

Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 60.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 30.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#ip route 10.0.0.0 255.0.0.0 30.0.0.1
Router(config)#ip route 20.0.0.0 255.0.0.0 10.0.0.2
Router(config)#ip route 40.0.0.0 255.0.0.0 30.0.0.1
Router(config)#ip route 50.0.0.0 255.0.0.0 40.0.0.2

# Router 3

Router\>enable
Router#configure
Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 50.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 40.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex
Router(config)#ip route 30.0.0.0 255.0.0.0 40.0.0.1
Router(config)#ip route 60.0.0.0 255.0.0.0 30.0.0.2
Router(config)#ip route 10.0.0.0 255.0.0.0 40.0.0.1
Router(config)#ip route 20.0.0.0 255.0.0.0 10.0.0.2

![image2](../../attachments/72010f2d8f7248baa185b76345d5bfff.png)

![image3](../../attachments/581db481a384422a9938a7452649b65a.png)

![image4](../../attachments/4bbfcf06ac20416488917ca3802a8c5a.png)

