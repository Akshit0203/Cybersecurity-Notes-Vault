# Password 

## Enable
Router\>enable
Router#configure terminal
Router(config)#enable password 123
Router(config)#ex
Router#ex
Router\>

Router\>en
Password:
Router#

## Disable

Router\>
Router\>enable
Password:
Router#configure terminal
Router(config)#no enable password
Router(config)#ex
Router#

## Encrypted Password 

Router\>
Router\>enable
Router#configure terminal
Router(config)#enable password 123
Router(config)#enable secret 456
Router(config)#ex
Router#

It will ask you now to enter the secret password only

# Hostname

Router\>
Router\>enable
Router#configure terminal
Router(config)#hostname craw_rack2_d7
craw_rack2_d7(config)#

# Banner

Router(config)#hostname craw_rack2_d7
craw_rack2_d7(config)#banner ?
login Set login banner
motd Set Message of the Day banner
craw_rack2_d7(config)#banner motd 123
Enter TEXT message. End with the character '1'.

CRAW NETWORKING

1

craw_rack2_d7(config)#ex
craw_rack2_d7#ex

