![image1](../../attachments/4994e51859964e57bf4ed957833fb96d.png)

# Router 0

Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 20.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex

Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 10.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex

Router(config)#ip route 30.0.0.0 255.0.0.0 10.0.0.2

# Router 1 

Router\>enable
Router#configure terminal
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 10.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#ex

Router(config)#interface gigabitEthernet 0/1
Router(config-if)#ip address 30.0.0.1 255.0.0.0
Router(config-if)#no shutdown

Router(config)#ip route 20.0.0.0 255.0.0.0 10.0.0.1

![image2](../../attachments/b0c52522e1fd43adb1d34fbb6b38dd81.png)

![image3](../../attachments/a8a337a3e1e243c68b0bf84fb1a7973a.png)

![image4](../../attachments/a1d7fda11bae4d8881b3d93c7d0a2d9d.png)

![image5](../../attachments/c408abfdff724bce9479bfd79375a599.png)

![image6](../../attachments/4b465425331f41918770cde981da0f0e.png)

