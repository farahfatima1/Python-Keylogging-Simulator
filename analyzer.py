from pathlib import Path 
from collections import Counter 
from datetime import datetime 
 
LOG_FILE = Path("logs/keystrokes.txt") 
REPORT_FILE = Path("logs/keylogging_report.txt") 
 
 
def analyze_log(): 
    if not LOG_FILE.exists(): 
        print("Log file not found.") 
        print("Run keylogger.py first.") 
        return 
 
    lines = LOG_FILE.read_text(encoding="utf-8").splitlines() 
 
    keys = [] 
 
    for line in lines: 
        if " - " in line: 
            key = line.split(" - ", 1)[1] 
            keys.append(key) 
 
    total = len(keys) 
 
    letters = sum( 
        1 for key in keys 
        if len(key) == 1 and key.isalpha() 
    ) 
 
    numbers = sum( 
        1 for key in keys 
        if len(key) == 1 and key.isdigit() 
    ) 
 
    special = total - letters - numbers 
 
    counter = Counter(keys) 
 
    # Security risk level 
    if total == 0: 
        risk_level = "NO DATA" 
    elif total < 20: 
        risk_level = "LOW" 
    elif total < 50: 
        risk_level = "MEDIUM" 
    else: 
        risk_level = "HIGH" 
 
    # Generate report 
    report = [] 
 
    report.append("=" * 55) 
    report.append("        KEY LOGGING SIMULATOR REPORT") 
    report.append("=" * 55) 
 
    report.append("") 
    report.append(f"Report Generated : {datetime.now():%Y-%m-%d %H:%M:%S}") 
    report.append(f"Log File         : {LOG_FILE}") 
    report.append("Environment      : Controlled Local Test") 
    report.append("") 
 
    report.append("-" * 55) 
    report.append("KEYSTROKE STATISTICS") 
    report.append("-" * 55) 
 
    report.append(f"Total Keystrokes : {total}") 
    report.append(f"Letters          : {letters}") 
    report.append(f"Numbers          : {numbers}") 
    report.append(f"Special/System   : {special}") 
    report.append(f"Risk Level       : {risk_level}") 
 
    report.append("") 
    report.append("-" * 55) 
    report.append("MOST FREQUENTLY PRESSED KEYS") 
    report.append("-" * 55) 
 
    for key, count in counter.most_common(10): 
        report.append(f"{key:<20} {count}") 
 
    report.append("") 
    report.append("-" * 55) 
    report.append("SECURITY RISK ASSESSMENT") 
    report.append("-" * 55) 
 
    risks = [ 
        "Keystrokes can expose sensitive information.", 
        "Passwords and credentials may be captured.", 
        "Private messages may be recorded.", 
        "Captured data can be misused by attackers.", 
        "Unauthorized keylogging is a privacy and security risk." 
    ] 
 
    for i, risk in enumerate(risks, 1): 
        report.append(f"{i}. {risk}") 
 
    report.append("") 
    report.append("-" * 55) 
    report.append("SECURITY RECOMMENDATIONS") 
    report.append("-" * 55) 
 
    recommendations = [ 
        "Use Multi-Factor Authentication (MFA).", 
        "Keep operating systems and security software updated.", 
        "Avoid installing software from untrusted sources.", 
        "Monitor systems for suspicious processes.", 
        "Use endpoint security and anti-malware protection.", 
        "Only perform keylogging in authorized environments." 
    ] 
 
    for i, recommendation in enumerate(recommendations, 1): 
        report.append(f"{i}. {recommendation}") 
 
    report.append("") 
    report.append("=" * 55) 
    report.append("END OF REPORT") 
    report.append("=" * 55) 
 
    report_text = "\n".join(report) 
 
    REPORT_FILE.write_text(report_text, encoding="utf-8") 
 
    print(report_text) 
 
    print(f"\nReport saved to: {REPORT_FILE}") 
 
 
if __name__ == "__main__": 
    analyze_log()