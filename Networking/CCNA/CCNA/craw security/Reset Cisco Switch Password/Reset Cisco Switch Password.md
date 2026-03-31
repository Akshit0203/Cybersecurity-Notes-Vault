![image1](../../attachments/19e477564ff840a1bfaecbbd077edf12.png)

Switch\>
Switch\>enable
Switch#configure terminal
Switch(config)#enable password 123
Switch(config)#hostname craw
craw(config)#ex
craw#
craw#wr
Building configuration...
\[OK\]
craw#
craw#ex

craw\>
craw\>enable
Password:

Now asks for password

We press the mode button physically present
![image2](../../attachments/518ed5c6624b4255918a194ec14b63a3.jpeg)

On cisco packet tracer , we reset the network
![image3](../../attachments/971a20e6126448a881767c9eedad561c.png)

![image4](../../attachments/8ace156a2ea94b378a8fe39c8a928a1a.png)

![image5](../../attachments/a0e502e92bb84f118cab9570f9450704.png)

And press the mode button

switch: flash_init
switch: dir flash:

![image6](../../attachments/78ca11ee5fef4203846b9db0ad7a5196.png)

switch: rename flash:config.text flash:config.asd
switch: boot

We rename the config file which had the passwords in it

![image7](../../attachments/32ebae49bf544dab98bfe09a25e82b89.png)

Switch\>enable
Switch#show flash:
Directory of flash:/

1 -rw- 4414921 \<no date\> 2960-lanbase-mz.122-25.FX.bin
2 -rw- 1100 \<no date\> config.asd

64016384 bytes total (59600363 bytes free)
Switch#copy flash: running-config
Source filename \[\]? config.asd
Destination filename \[running-config\]?

1100 bytes copied in 0.416 secs (2644 bytes/sec)
craw#
%SYS-5-CONFIG_I: Configured from console by console

craw#

All the previous configuration like hostname has come back

![image8](../../attachments/07d52c01a5214dfbaaf45557b2352e61.png)

We can set new password now

To delete a flash

Switch# Delete flash:

