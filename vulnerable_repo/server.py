"""
Server Endpoint and Command Handler
CRITICAL SECURITY AND LOGIC VULNERABILITIES:
- Arbitrary code execution via eval() and exec()
- System command injection via os.system()
- Path traversal vulnerability via open() string concatenation
- Unreachable code logic defect
"""

import os


def execute_admin_expression(user_expression):
    # CRITICAL: Remote Code Execution via eval()
    result = eval(user_expression)
    return result
    print("This log line is completely unreachable code")  # Logic defect: Unreachable code


def run_system_diagnostic(target_host):
    # CRITICAL: Remote Command Injection via os.system()
    command = "ping -c 1 " + target_host
    os.system(command)


def read_system_report(filename):
    # CRITICAL: Path Traversal vulnerability
    report_path = "/var/log/reports/" + filename
    with open(report_path, "r") as f:
        return f.read()
