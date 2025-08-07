import requests

def scan_sql_injection(url, headers=None):
    payload = "' OR 1=1--"
    try:
        resp = requests.get(url, params={'test': payload}, headers=headers, timeout=5)
        if any(err in resp.text.lower() for err in ['sql', 'syntax', 'mysql', 'psql', 'error']):
            return {
                "vulnerability": "SQL Injection",
                "risk": "high",
                "details": f"Possible SQL error detected with payload {payload}"
            }
    except Exception as e:
        return {
            "vulnerability": "SQL Injection",
            "risk": "medium",
            "details": f"Error during scan: {str(e)}"
        }
    return {
        "vulnerability": "SQL Injection",
        "risk": "low",
        "details": "No SQLi patterns detected"
    } 