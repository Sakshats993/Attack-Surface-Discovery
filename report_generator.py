"""
Report Generator Module
Handles the generation of HTML and other formatted reports
"""

import json
from datetime import datetime
from typing import Dict, List

class ReportGenerator:
    """Class for generating various report formats"""
    
    def __init__(self):
        """Initialize the Report Generator"""
        self.html_template = self.get_html_template()
    
    def get_html_template(self) -> str:
        """
        Get the HTML report template
        
        Returns:
            HTML template string
        """
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attack Surface Discovery Report</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .summary-section {
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }
        
        .summary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .summary-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            text-align: center;
            transition: transform 0.3s;
        }
        
        .summary-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        }
        
        .summary-card h3 {
            color: #667eea;
            font-size: 2em;
            margin-bottom: 5px;
        }
        
        .summary-card p {
            color: #6c757d;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .content-section {
            padding: 30px;
        }
        
        .section-title {
            font-size: 1.8em;
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }
        
        .host-card {
            background: white;
            border: 1px solid #dee2e6;
            border-radius: 10px;
            margin-bottom: 20px;
            overflow: hidden;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        }
        
        .host-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            font-size: 1.2em;
            font-weight: bold;
        }
        
        .host-body {
            padding: 20px;
        }
        
        .service-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        
        .service-table th {
            background: #f8f9fa;
            color: #495057;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #dee2e6;
        }
        
        .service-table td {
            padding: 10px 12px;
            border-bottom: 1px solid #dee2e6;
        }
        
        .service-table tr:hover {
            background: #f8f9fa;
        }
        
        .port-badge {
            background: #667eea;
            color: white;
            padding: 3px 8px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.9em;
        }
        
        .state-open {
            color: #28a745;
            font-weight: bold;
        }
        
        .services-summary {
            margin-top: 30px;
        }
        
        .service-tag {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            margin: 5px;
            font-size: 0.9em;
        }
        
        .footer {
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #6c757d;
            font-size: 0.9em;
        }
        
        .timestamp {
            color: #667eea;
            font-weight: bold;
        }
        
        .no-data {
            text-align: center;
            padding: 40px;
            color: #6c757d;
            font-style: italic;
        }
        
        @media (max-width: 768px) {
            .summary-grid {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Attack Surface Discovery Report</h1>
            <p>Automated Network Reconnaissance Results</p>
        </div>
        
        <div class="summary-section">
            <h2 class="section-title">📊 Scan Summary</h2>
            <div class="summary-grid">
                <div class="summary-card">
                    <h3>{total_hosts}</h3>
                    <p>Total Hosts</p>
                </div>
                <div class="summary-card">
                    <h3>{hosts_up}</h3>
                    <p>Live Hosts</p>
                </div>
                <div class="summary-card">
                    <h3>{open_ports}</h3>
                    <p>Open Ports</p>
                </div>
                <div class="summary-card">
                    <h3>{unique_services}</h3>
                    <p>Unique Services</p>
                </div>
            </div>
            
            <div style="margin-top: 20px;">
                <p><strong>Target:</strong> {target}</p>
                <p><strong>Scan Type:</strong> {scan_type}</p>
                <p><strong>Timestamp:</strong> <span class="timestamp">{timestamp}</span></p>
            </div>
        </div>
        
        <div class="content-section">
            <h2 class="section-title">🖥️ Discovered Hosts</h2>
            {hosts_content}
        </div>
        
        <div class="content-section">
            <div class="services-summary">
                <h2 class="section-title">🔧 Services Overview</h2>
                {services_content}
            </div>
        </div>
        
        <div class="footer">
            <p>Generated by Automated Attack Surface Discovery Tool</p>
            <p>Report created on {report_timestamp}</p>
        </div>
    </div>
</body>
</html>
        """
    
    def generate_html_report(self, results: Dict, output_file: str):
        """
        Generate an HTML report from scan results
        
        Args:
            results: Scan results dictionary
            output_file: Path to save the HTML report
        """
        # Prepare data for the template
        total_hosts = results.get('total_hosts', 0)
        hosts_up = results.get('hosts_up', 0)
        open_ports = results.get('total_open_ports', 0)
        unique_services = len(results.get('services', {}))
        
        # Generate hosts content
        hosts_content = self.generate_hosts_html(results.get('hosts', []))
        
        # Generate services content
        services_content = self.generate_services_html(results.get('services', {}))
        
        # Format timestamp
        timestamp = results.get('timestamp', datetime.now().isoformat())
        if isinstance(timestamp, str):
            try:
                dt = datetime.fromisoformat(timestamp)
                formatted_timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                formatted_timestamp = timestamp
        else:
            formatted_timestamp = timestamp
        
        # Fill the template
        html_content = self.html_template.format(
            total_hosts=total_hosts,
            hosts_up=hosts_up,
            open_ports=open_ports,
            unique_services=unique_services,
            target=results.get('target', 'N/A'),
            scan_type=results.get('scan_type', 'N/A'),
            timestamp=formatted_timestamp,
            hosts_content=hosts_content,
            services_content=services_content,
            report_timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        
        # Save the report
        with open(output_file, 'w') as f:
            f.write(html_content)
    
    def generate_hosts_html(self, hosts: List[Dict]) -> str:
        """
        Generate HTML content for hosts section
        
        Args:
            hosts: List of host dictionaries
            
        Returns:
            HTML string for hosts section
        """
        if not hosts:
            return '<p class="no-data">No hosts discovered</p>'
        
        html_parts = []
        for host in hosts:
            host_html = f"""
            <div class="host-card">
                <div class="host-header">
                    {host['ip']} {f"({host['hostname']})" if host['hostname'] != host['ip'] else ""}
                </div>
                <div class="host-body">
            """
            
            if host.get('os_detection'):
                host_html += f"<p><strong>OS Detection:</strong> {host['os_detection']}</p>"
            
            if host.get('ports'):
                host_html += """
                    <table class="service-table">
                        <thead>
                            <tr>
                                <th>Port</th>
                                <th>Protocol</th>
                                <th>State</th>
                                <th>Service</th>
                            </tr>
                        </thead>
                        <tbody>
                """
                
                for port in host['ports']:
                    host_html += f"""
                        <tr>
                            <td><span class="port-badge">{port['port']}</span></td>
                            <td>{port['protocol']}</td>
                            <td class="state-open">{port['state']}</td>
                            <td>{port['service']}</td>
                        </tr>
                    """
                
                host_html += """
                        </tbody>
                    </table>
                """
            else:
                host_html += '<p class="no-data">No open ports detected</p>'
            
            host_html += """
                </div>
            </div>
            """
            
            html_parts.append(host_html)
        
        return ''.join(html_parts)
    
    def generate_services_html(self, services: Dict) -> str:
        """
        Generate HTML content for services section
        
        Args:
            services: Dictionary of services and their locations
            
        Returns:
            HTML string for services section
        """
        if not services:
            return '<p class="no-data">No services discovered</p>'
        
        html_parts = ['<div>']
        for service, locations in services.items():
            html_parts.append(f'<span class="service-tag">{service} ({len(locations)})</span>')
        html_parts.append('</div>')
        
        # Add detailed service listing
        html_parts.append('<div style="margin-top: 20px;">')
        for service, locations in sorted(services.items()):
            html_parts.append(f'<h4 style="margin-top: 15px; color: #495057;">{service}</h4>')
            html_parts.append('<ul style="list-style-type: none; padding-left: 20px;">')
            for location in locations[:5]:  # Show first 5 locations
                html_parts.append(f'<li>📍 {location}</li>')
            if len(locations) > 5:
                html_parts.append(f'<li style="color: #6c757d; font-style: italic;">... and {len(locations) - 5} more</li>')
            html_parts.append('</ul>')
        html_parts.append('</div>')
        
        return ''.join(html_parts)