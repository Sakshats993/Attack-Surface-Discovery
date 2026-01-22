#!/usr/bin/env python3
"""
Automated Attack Surface Discovery Tool
A security tool for automated network reconnaissance using Nmap
Author: Security Engineer
Version: 1.0.0
"""

import subprocess
import argparse
import json
import re
import sys
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import ipaddress
from report_generator import ReportGenerator

class AttackSurfaceDiscovery:
    """Main class for automated attack surface discovery using Nmap"""
    
    def __init__(self, verbose: bool = False):
        """
        Initialize the Attack Surface Discovery tool
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.scan_results = {}
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.report_gen = ReportGenerator()
        
        # Create reports directory if it doesn't exist
        os.makedirs('reports', exist_ok=True)
        
    def validate_target(self, target: str) -> Tuple[bool, str]:
        """
        Validate the target (IP, domain, or IP range)
        
        Args:
            target: Target to validate
            
        Returns:
            Tuple of (is_valid, target_type)
        """
        # Check if it's an IP address
        try:
            ipaddress.ip_address(target)
            return True, "ip"
        except ValueError:
            pass
            
        # Check if it's an IP network/range
        try:
            ipaddress.ip_network(target, strict=False)
            return True, "network"
        except ValueError:
            pass
            
        # Check if it's a domain name
        domain_pattern = re.compile(
            r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?$'
        )
        if domain_pattern.match(target):
            return True, "domain"
            
        return False, "unknown"
    
    def run_nmap_scan(self, target: str, scan_type: str = "default") -> Dict:
        """
        Execute Nmap scan on the target
        
        Args:
            target: Target to scan
            scan_type: Type of scan (default, aggressive, quick)
            
        Returns:
            Dictionary containing scan results
        """
        print(f"\n[*] Starting Nmap scan on {target}")
        print(f"[*] Scan type: {scan_type}")
        print(f"[*] Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Build Nmap command based on scan type
        nmap_commands = {
            "default": ["nmap", "-sV", "-sC", "-p-", "--open"],
            "aggressive": ["nmap", "-A", "-T4", "-p-"],
            "quick": ["nmap", "-F", "-T4"],
            "top-ports": ["nmap", "-sV", "--top-ports", "1000"]
        }
        
        command = nmap_commands.get(scan_type, nmap_commands["default"])
        command.append(target)
        
        if self.verbose:
            print(f"[*] Running command: {' '.join(command)}")
        
        try:
            # Execute Nmap scan
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=600  # 10 minute timeout
            )
            
            if result.returncode != 0:
                print(f"[!] Nmap scan failed: {result.stderr}")
                return {}
                
            # Save raw output
            raw_output_file = f"reports/nmap_raw_{target.replace('/', '_')}_{self.timestamp}.txt"
            with open(raw_output_file, 'w') as f:
                f.write(result.stdout)
            print(f"[+] Raw Nmap output saved to: {raw_output_file}")
            
            # Parse the output
            parsed_results = self.parse_nmap_output(result.stdout)
            parsed_results['target'] = target
            parsed_results['scan_type'] = scan_type
            parsed_results['timestamp'] = datetime.now().isoformat()
            
            return parsed_results
            
        except subprocess.TimeoutExpired:
            print("[!] Nmap scan timed out")
            return {}
        except Exception as e:
            print(f"[!] Error during Nmap scan: {str(e)}")
            return {}
    
    def parse_nmap_output(self, output: str) -> Dict:
        """
        Parse Nmap output to extract structured information
        
        Args:
            output: Raw Nmap output
            
        Returns:
            Dictionary containing parsed results
        """
        results = {
            'hosts': [],
            'total_hosts': 0,
            'hosts_up': 0,
            'total_open_ports': 0,
            'services': {}
        }
        
        current_host = None
        
        for line in output.split('\n'):
            # Detect host information
            if 'Nmap scan report for' in line:
                if current_host:
                    results['hosts'].append(current_host)
                    
                host_match = re.search(r'Nmap scan report for (.+?)(?:\s+\((.+?)\))?$', line)
                if host_match:
                    current_host = {
                        'hostname': host_match.group(1),
                        'ip': host_match.group(2) if host_match.group(2) else host_match.group(1),
                        'status': 'up',
                        'ports': [],
                        'os_detection': '',
                        'services': []
                    }
                    results['hosts_up'] += 1
            
            # Parse port information
            elif current_host and re.match(r'^\d+\/', line):
                port_match = re.match(r'^(\d+)\/(\w+)\s+(\w+)\s+(.*)$', line)
                if port_match:
                    port_info = {
                        'port': int(port_match.group(1)),
                        'protocol': port_match.group(2),
                        'state': port_match.group(3),
                        'service': port_match.group(4)
                    }
                    
                    if port_info['state'] == 'open':
                        current_host['ports'].append(port_info)
                        results['total_open_ports'] += 1
                        
                        # Track services
                        service_name = port_info['service'].split()[0] if port_info['service'] else 'unknown'
                        if service_name not in results['services']:
                            results['services'][service_name] = []
                        results['services'][service_name].append(f"{current_host['ip']}:{port_info['port']}")
            
            # Parse OS detection
            elif current_host and 'OS details:' in line:
                os_match = re.search(r'OS details:\s+(.+)$', line)
                if os_match:
                    current_host['os_detection'] = os_match.group(1)
        
        # Add the last host
        if current_host:
            results['hosts'].append(current_host)
        
        results['total_hosts'] = len(results['hosts'])
        
        return results
    
    def generate_summary(self, results: Dict) -> str:
        """
        Generate a summary of the scan results
        
        Args:
            results: Parsed scan results
            
        Returns:
            Summary string
        """
        summary = []
        summary.append("\n" + "="*60)
        summary.append("ATTACK SURFACE DISCOVERY SUMMARY")
        summary.append("="*60)
        summary.append(f"Target: {results.get('target', 'N/A')}")
        summary.append(f"Scan Type: {results.get('scan_type', 'N/A')}")
        summary.append(f"Timestamp: {results.get('timestamp', 'N/A')}")
        summary.append("-"*60)
        summary.append(f"Total Hosts Scanned: {results.get('total_hosts', 0)}")
        summary.append(f"Live Hosts Found: {results.get('hosts_up', 0)}")
        summary.append(f"Total Open Ports: {results.get('total_open_ports', 0)}")
        summary.append("-"*60)
        
        # Service summary
        if results.get('services'):
            summary.append("\nDISCOVERED SERVICES:")
            for service, locations in results['services'].items():
                summary.append(f"  • {service}: {len(locations)} instance(s)")
                if self.verbose:
                    for loc in locations[:3]:  # Show first 3 locations
                        summary.append(f"    - {loc}")
                    if len(locations) > 3:
                        summary.append(f"    ... and {len(locations) - 3} more")
        
        # Host details
        summary.append("\n" + "-"*60)
        summary.append("HOST DETAILS:")
        for host in results.get('hosts', []):
            summary.append(f"\n  Host: {host['ip']}")
            if host['hostname'] != host['ip']:
                summary.append(f"    Hostname: {host['hostname']}")
            if host.get('os_detection'):
                summary.append(f"    OS: {host['os_detection']}")
            summary.append(f"    Open Ports: {len(host['ports'])}")
            
            if host['ports']:
                summary.append("    Services:")
                for port in host['ports'][:10]:  # Show first 10 ports
                    summary.append(f"      - {port['port']}/{port['protocol']}: {port['service']}")
                if len(host['ports']) > 10:
                    summary.append(f"      ... and {len(host['ports']) - 10} more ports")
        
        summary.append("\n" + "="*60)
        
        return '\n'.join(summary)
    
    def save_results(self, results: Dict, target: str):
        """
        Save scan results to files
        
        Args:
            results: Scan results to save
            target: Target that was scanned
        """
        # Clean target for filename
        clean_target = target.replace('/', '_').replace('.', '_')
        
        # Generate text report
        text_report = self.generate_summary(results)
        text_file = f"reports/attack_surface_{clean_target}_{self.timestamp}.txt"
        with open(text_file, 'w') as f:
            f.write(text_report)
        print(f"[+] Text report saved to: {text_file}")
        
        # Generate HTML report
        html_file = f"reports/attack_surface_{clean_target}_{self.timestamp}.html"
        self.report_gen.generate_html_report(results, html_file)
        print(f"[+] HTML report saved to: {html_file}")
        
        # Save JSON data for further processing
        json_file = f"reports/attack_surface_{clean_target}_{self.timestamp}.json"
        with open(json_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"[+] JSON data saved to: {json_file}")
    
    def scan(self, target: str, scan_type: str = "default"):
        """
        Main scanning method
        
        Args:
            target: Target to scan
            scan_type: Type of scan to perform
        """
        # Validate target
        is_valid, target_type = self.validate_target(target)
        if not is_valid:
            print(f"[!] Invalid target: {target}")
            print("    Please provide a valid IP address, domain name, or IP range")
            return
        
        print(f"[+] Valid target detected: {target} (Type: {target_type})")
        
        # Run the scan
        results = self.run_nmap_scan(target, scan_type)
        
        if results:
            # Display summary
            print(self.generate_summary(results))
            
            # Save results
            self.save_results(results, target)
            
            print("\n[+] Attack surface discovery completed successfully!")
        else:
            print("[!] No results obtained from scan")

def main():
    """Main entry point for the script"""
    
    # ASCII Banner
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║     AUTOMATED ATTACK SURFACE DISCOVERY TOOL          ║
    ║           Powered by Nmap & Python                    ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(banner)
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Automated Attack Surface Discovery Tool using Nmap'
    )
    parser.add_argument(
        'target',
        help='Target to scan (IP, domain, or IP range)'
    )
    parser.add_argument(
        '-s', '--scan-type',
        choices=['default', 'aggressive', 'quick', 'top-ports'],
        default='default',
        help='Type of scan to perform (default: default)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Check if Nmap is installed
    try:
        subprocess.run(['nmap', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[!] Error: Nmap is not installed or not in PATH")
        print("    Please install Nmap: https://nmap.org/download.html")
        sys.exit(1)
    
    # Initialize and run the scanner
    scanner = AttackSurfaceDiscovery(verbose=args.verbose)
    scanner.scan(args.target, args.scan_type)

if __name__ == "__main__":
    main()