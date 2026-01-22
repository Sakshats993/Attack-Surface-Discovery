# Sample Usage Guide

## Installation

1.**Install Nmap**
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install nmap

   # CentOS/RHEL/Fedora
   sudo yum install nmap

   # macOS
   brew install nmap

   # Windows
   # Download from https://nmap.org/download.html

2.**Clone the Project**
   git clone <repository-url>
   cd attack-surface-discovery

 3.**Make Script Executable (Linux/macOS)**
   chmod +x attack_surface_discovery.py

4.**Basic Usage Examples**
1. Scan a Single IP Address
Bash
python attack_surface_discovery.py 192.168.1.1
2. Scan a Domain
Bash
python attack_surface_discovery.py example.com
3. Scan an IP Range
Bash
python attack_surface_discovery.py 192.168.1.0/24
4. Quick Scan (Faster, Less Detailed)
Bash
python attack_surface_discovery.py -s quick 192.168.1.1
5. Aggressive Scan (More Detailed)
Bash
python attack_surface_discovery.py -s aggressive scanme.nmap.org
6. Top 1000 Ports Scan
Bash
python attack_surface_discovery.py -s top-ports 192.168.1.0/24
7. Verbose Output
Bash
python attack_surface_discovery.py -v 192.168.1.1

Output Files
All scan results are saved in the reports/ directory:
Text Report: attack_surface_<target>_<timestamp>.txt
HTML Report: attack_surface_<target>_<timestamp>.html
JSON Data: attack_surface_<target>_<timestamp>.json
Raw Nmap Output: nmap_raw_<target>_<timestamp>.txt

**5. File: `.gitkeep` files**
Create empty `.gitkeep` files in:
- `reports/.gitkeep`
- `templates/.gitkeep`
These keep empty directories in version control.

## 🚀 HOW TO RUN THE PROJECT
### **Step 1: Setup Project Directory**
```bash
# Create main project directory
mkdir attack-surface-discovery
cd attack-surface-discovery

# Create subdirectories
mkdir reports
mkdir examples
mkdir templates

# Create .gitkeep files to maintain directory structure
touch reports/.gitkeep
touch templates/.gitkeep
```
**Step 2: Create All Files**
Create attack_surface_discovery.py and paste the main script code
Create report_generator.py and paste the report module code
Create requirements.txt and paste the requirements
Create examples/sample_usage.md and paste the usage guide
Copy the original README.md to the root directory

**Step 3: Install Prerequisites**
```bash
# Install Nmap (choose based on your OS)

# For Ubuntu/Debian:
sudo apt-get update
sudo apt-get install nmap

# For CentOS/RHEL:
sudo yum install nmap

# For macOS:
brew install nmap

# For Windows:
# Download installer from https://nmap.org/download.html

# Verify Nmap installation
nmap --version
```
**Step 4: Make Script Executable (Linux/macOS)**
```bash
chmod +x attack_surface_discovery.py
```
**Step 5: Run the Tool**
Basic Usage:
```bash
# Scan a single IP
python attack_surface_discovery.py 192.168.1.1
# Scan a domain
python attack_surface_discovery.py scanme.nmap.org
# Scan an IP range
python attack_surface_discovery.py 192.168.1.0/24
```
Advanced Usage:
```bash
# Quick scan (faster)
python attack_surface_discovery.py -s quick scanme.nmap.org
# Aggressive scan (detailed)
python attack_surface_discovery.py -s aggressive 192.168.1.1
# Top 1000 ports only
python attack_surface_discovery.py -s top-ports example.com
# Verbose output
python attack_surface_discovery.py -v scanme.nmap.org
# Combine option
python attack_surface_discovery.py -s quick -v 192.168.1.0/24
```
**Step 6: Check Results**
After running a scan, check the reports/ directory for:

Text Report - Quick summary in terminal-friendly format
HTML Report - Beautiful web report (open in browser)
JSON Data - Structured data for further processing
Raw Nmap Output - Original Nmap scan results

```bash
# List generated reports
ls -la reports/
# View text report
cat reports/attack_surface_*.txt
# Open HTML report in browser (Linux)
xdg-open reports/attack_surface_*.html
# Open HTML report in browser (macOS)
open reports/attack_surface_*.html
# Open HTML report in browser (Windows)
start reports/attack_surface_*.html
```
**📝 TESTING THE PROJECT**
Test Commands (Safe Targets)
```bash
# Test 1: Scan Nmap's official test server
python attack_surface_discovery.py scanme.nmap.org
# Test 2: Scan localhost
python attack_surface_discovery.py 127.0.0.1
# Test 3: Quick scan of local network (adjust IP range)
python attack_surface_discovery.py -s quick 192.168.1.0/24
# Test 4: Verbose mode
python attack_surface_discovery.py -v scanme.nmap.org
```
**⚠️IMPORTANT NOTES**
Permissions: Some scan types require root/admin privileges:
```Bash
sudo python attack_surface_discovery.py 192.168.1.1
```
Legal Warning: Only scan systems you own or have permission to test
Firewall Issues: Some networks block Nmap scans

Scan Duration:
Quick scans: 1-2 minutes
Default scans: 5-10 minutes
Aggressive scans: 15-30 minutes
Large IP ranges: Can take hours

**🎯 Expected Output Example**
When you run the tool, you'll see:
text
╔═══════════════════════════════════════════════════════╗
║     AUTOMATED ATTACK SURFACE DISCOVERY TOOL           ║
║           Powered by Nmap & Python                    ║
╚═══════════════════════════════════════════════════════╝
[+] Valid target detected: scanme.nmap.org (Type: domain)
[*] Starting Nmap scan on scanme.nmap.org
[*] Scan type: default
[*] Timestamp: 2024-01-15 14:30:00
[+] Raw Nmap output saved to: reports/nmap_raw_scanme_nmap_org_20240115_143000.txt
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
[+] Text report saved to: reports/attack_surface_scanme_nmap_org_20240115_143000.txt
[+] HTML report saved to: reports/attack_surface_scanme_nmap_org_20240115_143000.html
[+] JSON data saved to: reports/attack_surface_scanme_nmap_org_20240115_143000.json
[+] Attack surface discovery completed successfully!