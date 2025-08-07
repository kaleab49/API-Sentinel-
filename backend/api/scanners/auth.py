import requests

def scan_broken_auth(url, headers=None):
    try:
        # Try with headers (if any)
        resp_auth = requests.get(url, headers=headers, timeout=5)
        # Try without headers
        resp_noauth = requests.get(url, timeout=5)
        # If both succeed and return similar data, possible broken auth
        if resp_auth.status_code == 200 and resp_noauth.status_code == 200:
            if resp_auth.text == resp_noauth.text:
                return {
                    "vulnerability": "Broken Authentication",
                    "risk": "high",
                    "details": "Endpoint accessible with and without authentication."
                }
        if resp_noauth.status_code == 200:
            return {
                "vulnerability": "Broken Authentication",
                "risk": "high",
                "details": "Endpoint accessible without authentication."
            }
        if resp_noauth.status_code in [401, 403]:
            return {
                "vulnerability": "Broken Authentication",
                "risk": "low",
                "details": "Authentication appears to be required."
            }
        return {
            "vulnerability": "Broken Authentication",
            "risk": "medium",
            "details": f"Unexpected status code: {resp_noauth.status_code}"
        }
    except Exception as e:
        return {
            "vulnerability": "Broken Authentication",
            "risk": "medium",
            "details": f"Error during scan: {str(e)}"
        } 