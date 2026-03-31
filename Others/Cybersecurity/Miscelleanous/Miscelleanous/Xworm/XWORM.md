
Xworm tutorial

make rdp win 11
open port destination 7000 / specified in rat

turn off virus protection
and all folder/drive in exclusion

download .ico file of the desired payload
You can make custom ico file on canva or any photo editing app

make a new folder with
the ico file
the file which is to be sent ex. pdf , xlsx
payload

first open loader.exe
then application xworm.exe
if xworm doesn't open first open xworm then close
then open loader , this time xworm will automatically open

enter Client name
enter bin - @ReverseEngineeringLab
enter port 7000 or your desired port
leave key as it is
notification off

start

add host - enter ip of rdp
then click on plus +
click on local ip then click minus -
port 7000

settings
antikill on
tbotnotify off (telegram bot notifications)
clipper off (only for crypto transactions - pastes your wallet address instead of what is typed)
wdex off
keylogger on
anti analysis on

sleep/sec : 3

registry - on
schtasks off
startup on

%AppData%
enter name of payload - this will be shown in the task manager (which is main)
ex. Service_host.exe

usb - on if you want payload to be transferred if someone connects his pendrive/usb to the victim pc

obfuscator - crypts
assembly - language
icon - icon for service host , shows in task manager
Turn all 3 off if don’t know

download win rar
select both the payload and the exploit ( pdf , jpeg) by selecting ctrl and other file
When selecting both remove their type/extension - just keep their name without any .exe or .pdf

left click
win rar - add to archive

1\. select archive format as zip
2\. in archive name , enter the name of file with malware (example Mumbai (pdf) , so Mumbai.pdf)
there should be no spelling error

then select archiving options

create SFX arcive
let the archive name change automatically

go to advanced (besides general on top)

SFX options

general - leave blank ( can enter app data , by clicking on view on top of folder and selecting show hidden files)

text and icon
scroll down to last - load sfx icon from the file
select the ico file

setup
run after extraction - name the payload file ex. service_host.exe
run before extraction - name the malware file ex. Mumbai.pdf
add the file types at last ( .pdf , .exe )
no spelling error

modes
silent mode - hide all

update
update mode - extract and update files
overwrite mode - overwrite all files

ok 2 times

done
