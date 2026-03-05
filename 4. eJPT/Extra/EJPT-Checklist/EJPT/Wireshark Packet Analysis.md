### 🧪 Wireshark – Analysis & Filters Checklist

#### ✅ Common Display Filters
- [ ] `http.response.code == 200`  
  → Shows all successful HTTP responses.

- [ ] `ip.dst == <ip>`  
  → Filters packets with a specific destination IP.

- [ ] `nbns`  
  → Displays NetBIOS Name Service packets (to extract hostnames).

#### 🔍 MAC Address Identification

- [ ] Click any packet.
- [ ] Expand **Ethernet II** section.
- [ ] Note the **Source** and **Destination** MAC addresses.
#### 🎯 Search Specific Payloads or Scripts

- [ ] Press `Ctrl + F`
- [ ] Set **Find By** to `String`
- [ ] Set **Search In** to `Packet Bytes`
- [ ] Enter the string (e.g., `mystery_file.ps1`)
- [ ] Then Right Click -> Copy -> As printable text, then paste in a file and look into ps1 script
#### 🧠 Detect PowerShell Usage
- [ ] Look in HTTP headers for `User-Agent`
- [ ] If `WindowsPowerShell` is present  
  → A PowerShell script made the HTTP request.
#### 🧰 General Tip
- [ ] Use `Ctrl + F` to search for keywords in packet payloads.
  - Set search to **Packet Bytes** for raw content matching.

---

