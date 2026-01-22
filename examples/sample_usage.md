
# 📘 Sample Usage Guide – Automated Attack Surface Discovery Tool

This guide explains how to install, run, test, and verify the **Automated Attack Surface Discovery Tool**.

## 🔧 Installation

### 1️⃣ Install Nmap

#### Ubuntu / Debian
```bash
sudo apt-get update
sudo apt-get install nmap
````

#### CentOS / RHEL / Fedora

```bash
sudo yum install nmap
```

#### macOS

```bash
brew install nmap
```

#### Windows

Download and install from:
[https://nmap.org/download.html](https://nmap.org/download.html)

Verify installation:

```bash
nmap --version
```

---

### 2️⃣ Clone the Project

```bash
git clone <repository-url>
cd attack-surface-discovery
```

---

### 3️⃣ Make Script Executable (Linux / macOS)

```bash
chmod +x attack_surface_discovery.py
```

---

## 🚀 Basic Usage Examples

### 1. Scan a Single IP Address

```bash
python attack_surface_discovery.py 192.168.1.1
```

### 2. Scan a Domain

```bash
python attack_surface_discovery.py example.com
```

### 3. Scan an IP Range

```bash
python attack_surface_discovery.py 192.168.1.0/24
```

### 4. Quick Scan (Faster, Less Detailed)

```bash
python attack_surface_discovery.py -s quick 192.168.1.1
```

### 5. Aggressive Scan (More Detailed)

```bash
python attack_surface_discovery.py -s aggressive scanme.nmap.org
```

### 6. Top 1000 Ports Scan

```bash
python attack_surface_discovery.py -s top-ports 192.168.1.0/24
```

### 7. Verbose Output

```bash
python attack_surface_discovery.py -v 192.168.1.1
```

---

## 📂 Output Files

All scan results are saved in the `reports/` directory:

* **Text Report**
  `attack_surface_<target>_<timestamp>.txt`

* **HTML Report**
  `attack_surface_<target>_<timestamp>.html`

* **JSON Data**
  `attack_surface_<target>_<timestamp>.json`

* **Raw Nmap Output**
  `nmap_raw_<target>_<timestamp>.txt`

---

## 📁 .gitkeep Files

Create empty `.gitkeep` files to preserve directory structure:

```
reports/.gitkeep
templates/.gitkeep
```

---

## 🚀 HOW TO RUN THE PROJECT (From Scratch)

### Step 1: Setup Project Directory

```bash
mkdir attack-surface-discovery
cd attack-surface-discovery

mkdir reports
mkdir examples
mkdir templates

touch reports/.gitkeep
touch templates/.gitkeep
```

---

### Step 2: Create All Files

* `attack_surface_discovery.py` → Main script
* `report_generator.py` → Report generation logic
* `requirements.txt` → Dependencies
* `examples/sample_usage.md` → This file
* `README.md` → Project documentation

---

### Step 3: Install Prerequisites

```bash
nmap --version
python --version
```

---

### Step 4: Make Script Executable

```bash
chmod +x attack_surface_discovery.py
```

---

### Step 5: Run the Tool

#### Basic Usage

```bash
python attack_surface_discovery.py 192.168.1.1
python attack_surface_discovery.py scanme.nmap.org
python attack_surface_discovery.py 192.168.1.0/24
```

#### Advanced Usage

```bash
python attack_surface_discovery.py -s quick scanme.nmap.org
python attack_surface_discovery.py -s aggressive 192.168.1.1
python attack_surface_discovery.py -s top-ports example.com
python attack_surface_discovery.py -v scanme.nmap.org
python attack_surface_discovery.py -s quick -v 192.168.1.0/24
```

---

### Step 6: Check Results

```bash
ls -la reports/
cat reports/attack_surface_*.txt
```

Open HTML report:

#### Linux

```bash
xdg-open reports/attack_surface_*.html
```

#### macOS

```bash
open reports/attack_surface_*.html
```

#### Windows

```bash
start reports/attack_surface_*.html
```

---

## 🧪 Testing the Project (Safe Targets)

```bash
# Nmap official test server
python attack_surface_discovery.py scanme.nmap.org

# Localhost
python attack_surface_discovery.py 127.0.0.1

# Quick scan of local network
python attack_surface_discovery.py -s quick 192.168.1.0/24

# Verbose mode
python attack_surface_discovery.py -v scanme.nmap.org
```

---

## ⚠️ Important Notes

### Permissions

Some scans require elevated privileges:

```bash
sudo python attack_surface_discovery.py 192.168.1.1
```

### Legal Warning

⚠️ Only scan systems you **own** or have **explicit permission** to test.

### Scan Duration

* Quick scans: **1–2 minutes**
* Default scans: **5–10 minutes**
* Aggressive scans: **15–30 minutes**
* Large IP ranges: **May take hours**

---

## 🎯 Expected Output Example

```text
╔═══════════════════════════════════════════════════════╗
║     AUTOMATED ATTACK SURFACE DISCOVERY TOOL           ║
║           Powered by Nmap & Python                    ║
╚═══════════════════════════════════════════════════════╝

[+] Valid target detected: scanme.nmap.org (Type: domain)
[*] Starting Nmap scan on scanme.nmap.org
[*] Scan type: default
[*] Timestamp: 2024-01-15 14:30:00

[+] Raw Nmap output saved to:
    reports/nmap_raw_scanme_nmap_org_20240115_143000.txt

============================================================
ATTACK SURFACE DISCOVERY SUMMARY
============================================================
Target: scanme.nmap.org
Scan Type: default
Timestamp: 2024-01-15T14:30:00
------------------------------------------------------------
Total Hosts Scanned: 1
Live Hosts Found: 1
Total Open Ports: 5
------------------------------------------------------------

[+] Text report saved to:
    reports/attack_surface_scanme_nmap_org_20240115_143000.txt
[+] HTML report saved to:
    reports/attack_surface_scanme_nmap_org_20240115_143000.html
[+] JSON data saved to:
    reports/attack_surface_scanme_nmap_org_20240115_143000.json

[+] Attack surface discovery completed successfully!
```

---

<p align="center"><strong>⚡ Happy Ethical Hacking ⚡</strong></p>
