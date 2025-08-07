import requests

def scan_misconfig(url, headers=None):
    issues = []
    if url.startswith('http://'):
        issues.append('API is served over HTTP, not HTTPS.')
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        # Check for missing security headers
        missing_headers = []
        required_headers = [
            'X-Content-Type-Options',
            'Strict-Transport-Security',
            'X-Frame-Options',
            'X-XSS-Protection',
        ]
        for h in required_headers:
            if h not in resp.headers:
                missing_headers.append(h)
        if missing_headers:
            issues.append(f"Missing security headers: {', '.join(missing_headers)}")
        # Check for open CORS
        if resp.headers.get('Access-Control-Allow-Origin') == '*':
            issues.append('CORS is open to all origins.')
        if issues:
            return {
                "vulnerability": "Security Misconfigurations",
                "risk": "high",
                "details": "; ".join(issues)
            }
        return {
            "vulnerability": "Security Misconfigurations",
            "risk": "low",
            "details": "No obvious misconfigurations detected."
        }
    except Exception as e:
        return {
            "vulnerability": "Security Misconfigurations",
            "risk": "medium",
            "details": f"Error during scan: {str(e)}"
        } 