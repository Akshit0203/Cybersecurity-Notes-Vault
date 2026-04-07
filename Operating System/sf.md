# 🖥️ Operating Systems – Introduction

## 📌 What is an Operating System (OS)?
An **Operating System (OS)** is the **core software** of a computer that acts as a bridge between:
- User
- Applications
- Hardware

It works as an **“invisible manager”** coordinating everything.

> [!info] Why OS is Important
> Without an OS, applications would directly interact with hardware, causing conflicts, crashes, and instability.

---

## ✈️ Analogy: Airport System
- **Hardware** → Runways, planes, infrastructure  
- **Applications** → Airlines  
- **Operating System** → Air Traffic Control  

> [!tip] Key Idea
> The OS manages all operations just like air traffic control manages flights safely.

---

## 🧠 System Privilege Layers

### 🔐 Kernel Space
- Core part of OS
- Has **full/unrestricted access**
- Directly interacts with:
  - CPU
  - Memory
  - Hardware

---

### 👤 User Space
- Where normal applications run
- **Restricted access**
- Cannot directly access hardware
- Uses **system calls** to communicate with kernel

> [!important] Why Separation Matters
> - Improves security  
> - Prevents system crashes  
> - Ensures stability  

---

## ⚙️ Core Responsibilities of OS

### 🧩 Process Management
- Creates, schedules, and terminates processes
- Allocates CPU time

**Example:** Running browser + music + apps simultaneously  

---

### 🧠 Memory Management
- Allocates RAM to processes
- Protects memory between applications
- Uses **virtual memory** when RAM is low  

---

### 📂 File System Management
- Organizes files into directories
- Manages:
  - File names
  - Paths
  - Permissions
  - Metadata (size, type, timestamps)

**Example:** Creating folders, saving files  

---

### 👥 User Management
- Manages user accounts
- Handles authentication
- Controls permissions  

**Example:** Login system, access control  

---

### 🔌 Device Management
- Uses device drivers
- Provides hardware abstraction layer  

**Example:** Plugging USB/mouse and it works instantly  

---

## 🔐 Operating System Security

> [!warning] OS = First Line of Defense

### Key Security Functions:
- **Authentication** → Verifies user identity  
- **Permissions** → Controls access (read/write/execute)  
- **Isolation** → Separates processes (kernel vs user space)  
- **System Protection** → Protects critical files  

---

## 🧪 Important Questions

- **Which OS space has unrestricted hardware access?**  
  → `Kernel Space`

- **Which OS function manages users and permissions?**  
  → `User Management`

---

## ⚡ Quick Revision

- OS = **System Manager**
- Kernel = **Full access core**
- User Space = **Restricted apps**
- OS handles:
  - Processes  
  - Memory  
  - Files  
  - Users  
  - Devices  
- Provides built-in **security layer**

---

## 🔗 Tags
#operating-systems #tryhackme #cybersecurity #basics