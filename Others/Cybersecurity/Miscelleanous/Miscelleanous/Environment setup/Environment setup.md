**Download virtual box :**
1\. Download virtual box (windows64) \[<https://www.virtualbox.org/wiki/Downloads>\]
vmware pro : <https://softwareupdate.vmware.com/cds/vmw-desktop/ws/17.5.2/23775571/windows/core/>
2.  Download extension pack also
3.  Install the vm
4.  Install the extension pack after opening vm

**Download kali :**
1.  Go to kali.org (<https://www.kali.org/get-kali/#kali-installer-images>)
2.  Select your desired vm (vmware or virtualbox)
3.  Download file
4.  Username :kali
5.  Password: kali
6.  On monitor : go to display from search and set resolution to 1920x1080 for scaling ; other options lag
**Install updates**
1.  sudo apt update && sudo apt upgrade -y
2.  Sudo su (goes to root user)
3.  Get-apt update
4.  Get-apt upgrade
5.  Apt install && apt upgrade (for both at once)
6.  dpkg-reconfigure kali-grant-root (to grant permanent root access)
ok

Enable password less privilege escalation
7.  nano .zshrc
8.  After the last line on the next line type "sudo su"
9.  Control+O to save
10. Enter
11. Ctrl+X to exit
12. Restart vm


**Download windows**

14.  Search for windows ova file/virtual machine
15.  Windows 11 ([**https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/**](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)) (password : Akshit\*\*11)
16.  Windows 10 (<https://drive.google.com/file/d/1KR-dVmA89d9eWY933iWbOl649PIfyR-1/view>)
17.  Password : Passw0rd! (password)
**License key for windows**
1.  You press Win + R to open run (<https://appsforpcfree.net/upgrade-windows-10-evaluation-full-version-easily/>)
2.  Type: C:\Windows\System32\spp\tokens\skus
3.  You download new SKUs of Windows 10 Enterprise (<https://appsforpcfree.net/skus-Windows-10.zip>)
4.  Then you extract it and copy it to C:\Windows\System32\spp\tokens\skus (The local you open at step 2)
5.  You open cmd (run as administrator)
6.  Then you copy and paste these codes:
cscript.exe %windir%\system32\slmgr.vbs /rilc
cscript.exe %windir%\system32\slmgr.vbs /upk \>nul 2\>&1
cscript.exe %windir%\system32\slmgr.vbs /ckms \>nul 2\>&1
cscript.exe %windir%\system32\slmgr.vbs /cpky \>nul 2\>&1
cscript.exe %windir%\system32\slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43
sc config LicenseManager start= auto & net start LicenseManager
sc config wuauserv start= auto & net start wuauserv
clipup -v -o -altto c:\\
Echo

**Install custom kali by zsecurity (wifi pentesting)**
1.  download (<https://zsecurity.org/download-custom-kali/>)
2.  Username : root
3.  Password : toor
4.  Don’t apt update and upgrade cause its custom already(comes with drivers installed)

**Convert zsecurity vmware file to virtualbox file(vmdk to ovf)**
1.  Download ovf tool (<https://developer.vmware.com/web/tool/ovf/>)
2.  ovftool "c:pathtooriginal_vm.vmx""c:pathtoexport.ovf"
3.  Right click on folders and copy path
4.  open ovftool folder
5.  Open cmd
6.  Write : a.) ovftool
7.  b.)"paste vmx file path"
8.  c.)"paste destination folder path"
9.  Example : E:\miscelleanous\virtual box extras\VMware-ovftool-4.4.3-18663434-win.x86_64\ovftool\>ovftool "E:\miscelleanous\virtual box extras\Kali 2022 x64 Customized by zSecurity 1.0.12.vmwarevm\Kali 2022 x64 Customized by zSecurity 1.0.12.vmwarevm\Kali 2022 x64 Customized by zSecurity 1.0.12.vmx" E:export.ovf
10. Run the file in destination folder with vm

**Downloading and running metasploitable**
1.  Search for download (<https://sourceforge.net/projects/metasploitable/>)
2.  Unzip and convert (vmdk to ovf)\[same steps as above\]
3.  for metasploitable error : a.)open folder where there is virtual box installed
4.  b.)open cmd
5.  c.) .\vboxmanage modifyvm Metasploitable --acpi off
6.  d.) .\vboxmanage modifyvm Metasploitable --ioapic off
7.  Username and Password - msfadmin

**BlackArch Linux install :**
<https://blackarch.org/downloads.html>

**Dragon os install for vmware :**
<https://sourceforge.net/projects/dragonos-focal/>
Password : dragon

**Dragon os install for Raspberry pi (pi64)**
<https://sourceforge.net/projects/dragonos-pi64/>

Sudo raspi-config
Enable ssh
Enable vnc
Sudo apt-get xrdp
Sudo apt-get update
Sudo apt-get upgrade

**Flipper zero :**
1.  Download and run qflipper application <https://flipperzero.one/update>

**HackRF one :**
1.  <https://hackrf.app/>
2.  For custom splash screen
3.  Go on canva , make a custom design of 240x304px
4.  Convert it to .bmp file
5.  Take out sd card and add made .bmp file in splash folder
6.  Right click to select

**For exporting - use " " when there is space between words**

**For screenshot of vm : press host key(right control) + E**

**Setiings of all vm**
1.  General \> advanced \> shared clipboard \> bidirectional
2.  General \> advanced \> drag n drop \> bidirectional
3.  Network \> enable network adapter \> attached to: nat network

**Network adapters troubeshoot**
Search for : realtek rtl8812au driver windows 11
<https://www.realtek.com/Download/List?cate_id=660&menu_id=297>
Deleted this registry key

HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\\3d09c1ca-2bcc-40b7-b9bb-3f3ec143a87b}

And then I removed the "vmware bridge protocol" element from main network adapter.
Afterwards you can add or remove network adapters and they work correctly, (or leave them by default or reinstall vmware, everything works)
If vmware doesn’t install network adapters automatically
Vmci.sys download manually ans paste in c-windows - system 32 - driver
And install certificate manually

**RHEL 10**
download from official website 
root :: redhat
admin :: redhat


**Step-by-Step Recovery After Deleting HP Registry Keys**
1. Try System Restore Right Now**
If System Protection was on, this is your best chance to bring everything back.
2. Press **Windows + R**, type:
    
    `rstrui.exe`
    
3. Choose **“Choose a different restore point”** → select a date **before** you deleted the keys.
    
4. Click **Next → Finish**.  
    Your PC will reboot and attempt to restore the registry snapshot.
    
If this works, you’re done — all HP keys and software references should return automatically.

---
2. **If System Restore Fails or Was Disabled**

Then we’ll manually rebuild what you lost:
#### a) Run these repair commands

Open **Command Prompt as Administrator**, then run:

`sfc /scannow DISM /Online /Cleanup-Image /RestoreHealth`

These will repair Windows components that might have broken when registry links disappeared.

b) Reinstall HP utilities

Go to HP Support → Drivers & Software, enter your **exact model name** (for example _HP Envy x360 13-ay1036AU_).  
Download and install in this order:

1. **HP System Event Utility** → restores model and hotkey info.
    
2. **HP Hardware Diagnostics UEFI** → for future system checks.
    
3. **HP Command Center / HP Support Assistant** → for updates and thermal control.
    
4. **Chipset Drivers + BIOS Update** (latest versions).
    

Reboot **twice** afterward — first boot registers the services, second boot confirms them.

