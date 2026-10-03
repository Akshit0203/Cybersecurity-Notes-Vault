# Starting and Stopping Services

## Managing Services with `service`

| Command | What it does |
|---|---|
| `sudo service apache2 start` | Starts the Apache web server (begins serving web pages) |
| `sudo service apache2 stop` | Stops the Apache web server (halts active web page serving) |

## Quick HTTP Server with Python

| Command | What it does |
|---|---|
| `python3 -m http.server 80` | Starts a simple HTTP server on port 80, serving files from the current directory |

## Enabling/Disabling Services at Boot with `systemctl`

| Command | What it does |
|---|---|
| `sudo systemctl enable ssh` | Enables SSH to start **automatically on boot** |
| `sudo systemctl disable ssh` | Prevents SSH from starting automatically on boot |

## Key Concepts

- **`sudo`** — execute commands with superuser privileges
- **`service`** — manage services (start/stop) in the current session
- **`systemctl`** — manage services at the system level (enable/disable at boot, start/stop)
