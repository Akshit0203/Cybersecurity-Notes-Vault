
go to https://www.sublimetext.com/

Linux > apt

Install the GPG key:
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo tee /etc/apt/keyrings/sublimehq-pub.asc > /dev/null
```

Select the channel to use:
stable
```
echo -e 'Types: deb\nURIs: https://download.sublimetext.com/\nSuites: apt/stable/\nSigned-By: /etc/apt/keyrings/sublimehq-pub.asc' | sudo tee /etc/apt/sources.list.d/sublime-text.sources
```

Update apt sources and install Sublime Text:
```
sudo apt-get update
sudo apt-get install sublime-text
```

In terminal :
```
subl
```

