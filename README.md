```markdown
# 🔍 Automated Attack Surface Discovery Tool

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Nmap](https://img.shields.io/badge/Nmap-Required-red)](https://nmap.org/)
[![License](https://img.shields.io/badge/License-Educational-green)]()

A powerful **Python-based security automation tool** that leverages **Nmap** to perform attack surface discovery.  
It transforms raw Nmap output into **structured, actionable intelligence** through **modern HTML reports**, detailed text summaries, and machine-readable JSON data.

This project is designed for **cybersecurity students, cloud security engineers, and entry-level security professionals**.

---

## 🎯 Key Features

- 🚀 **Fully Automated Reconnaissance** – One command to complete scanning and reporting  
- 🎨 **Beautiful HTML Reports** – Modern UI, clean tables, and summaries  
- 📊 **Multiple Output Formats** – HTML, Text, JSON, and Raw Nmap logs  
- 🔧 **Flexible Scan Types** – Quick, Default, Aggressive, Top-Ports  
- 🌐 **Versatile Targets** – Single IPs, domains, and CIDR ranges  
- 📝 **Service & Version Detection** – Ports, services, OS hints  
- ⚡ **Production-Ready Design** – Validation, error handling, verbose mode  

---

## 📸 Screenshots

### Console Output

```

╔═══════════════════════════════════════════════════════╗
║   AUTOMATED ATTACK SURFACE DISCOVERY TOOL              ║
║   Powered by Nmap & Python                             ║
╚═══════════════════════════════════════════════════════╝

````

### HTML Report Preview

- Clean, modern gradient-based design  
- Interactive summary cards  
- Detailed host & service tables  
- Mobile-responsive layout  

---

## 🏗️ Architecture

```mermaid
graph LR
    A[User Input] --> B[Target Validation]
    B --> C[Nmap Execution]
    C --> D[Output Parsing]
    D --> E[Report Generation]
    E --> F[HTML Report]
    E --> G[Text Report]
    E --> H[JSON Data]
````

---

## 📁 Project Structure

```
attack-surface-discovery/
│
├── attack_surface_discovery.py     # Main scanning engine
├── report_generator.py             # Report generation logic
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
│
├── reports/                        # Generated outputs
│   ├── attack_surface_*.html
│   ├── attack_surface_*.txt
│   ├── attack_surface_*.json
│   └── nmap_raw_*.txt
│
└── examples/
    └── sample_usage.md
```

---

## 🚀 Quick Start

### Prerequisites

* Python **3.7+**
* Nmap (Network Mapper)
* Linux / macOS / Windows (WSL recommended)
* Root/Admin privileges for advanced scans

---

### Installation

#### Clone the Repository

```bash
git clone https://github.com/yourusername/attack-surface-discovery.git
cd attack-surface-discovery
```

#### Install Nmap

<details>
<summary>🐧 Linux</summary>

```bash
sudo apt-get update && sudo apt-get install -y nmap
# or
sudo yum install -y nmap
# or
sudo pacman -S nmap
```

</details>

<details>
<summary>🍎 macOS</summary>

```bash
brew install nmap
```

</details>

<details>
<summary>🪟 Windows</summary>

Download from: [https://nmap.org/download.html](https://nmap.org/download.html)

</details>

#### Verify Installation

```bash
python --version
nmap --version
```

---

## 💻 Usage

### Basic Commands

```bash
python attack_surface_discovery.py 192.168.1.1
python attack_surface_discovery.py example.com
python attack_surface_discovery.py 192.168.1.0/24
```

### Advanced Options

```bash
# Quick scan
python attack_surface_discovery.py -s quick target.com

# Aggressive scan
python attack_surface_discovery.py -s aggressive target.com

# Top ports only
python attack_surface_discovery.py -s top-ports target.com

# Verbose mode
python attack_surface_discovery.py -v target.com
```

---

## 📊 Scan Types Explained

| Scan Type  | Speed     | Detail Level | Use Case            |
| ---------- | --------- | ------------ | ------------------- |
| quick      | ⚡ Fast    | Basic        | Initial recon       |
| default    | ⚖️ Medium | Full         | Standard assessment |
| aggressive | 🐢 Slow   | Maximum      | Deep analysis       |
| top-ports  | ⚡ Fast    | Focused      | Common services     |

---

## 📈 Output Formats

### 1️⃣ HTML Report

* Modern web interface
* Shareable and presentation-ready

### 2️⃣ Text Report

* Clean CLI-friendly summary
* Easy to archive

### 3️⃣ JSON Output

* Structured data
* Automation & integration friendly

### 4️⃣ Raw Nmap Logs

* Full original scan output
* Manual verification

---

## 🎯 Real-World Use Cases

* 🔒 Security assessments & reconnaissance
* ☁️ Cloud infrastructure exposure mapping
* 🏢 Internal network audits
* 📚 Cybersecurity learning projects
* 🐛 Bug bounty attack surface enumeration
* 📊 Compliance & reporting

---

## 🔒 Security & Ethics

⚠️ **IMPORTANT:**
Use this tool **only** on:

* Systems you own
* Systems you have written authorization for
* Legal testing environments (e.g., `scanme.nmap.org`)

Always follow ethical hacking principles.

---

## 🐛 Troubleshooting

<details>
<summary>Nmap not found</summary>

Install Nmap and ensure it is in PATH.

</details>

<details>
<summary>Permission denied</summary>

Run with elevated privileges:

```bash
sudo python attack_surface_discovery.py target
```

</details>

---

## 📚 Technical Details

### Core Technologies

* Python 3.7+
* Nmap
* subprocess
* argparse
* ipaddress
* regex
* JSON
* HTML/CSS

---

## 🔮 Future Enhancements

* CVE correlation
* Shodan API integration
* PDF reports
* Email alerts
* Web dashboard
* Docker support
* Cloud provider integrations
* Risk scoring

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

## 📝 License

Educational and authorized security testing only.

---

## 🙏 Acknowledgments

* Nmap Project
* Security community
* Open-source contributors

---

<p align="center"><strong>⚡ Built for Security Professionals by Security Professionals ⚡</strong></p>
<p align="center">Made with ❤️ for the security community</p>
<p align="center"><i>Always hack ethically.</i></p>