import requests

def scan_data_exposure(url, headers=None):
    sensitive_fields = ["password", "ssn", "credit_card", "secret", "token"]
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.headers.get('Content-Type', '').startswith('application/json'):
            data = resp.json()
            found = []
            if isinstance(data, dict):
                for field in sensitive_fields:
                    if field in data:
                        found.append(field)
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        for field in sensitive_fields:
                            if field in item:
                                found.append(field)
            if found:
                return {
                    "vulnerability": "Excessive Data Exposure",
                    "risk": "high",
                    "details": f"Sensitive fields exposed: {', '.join(set(found))}"
                }
            return {
                "vulnerability": "Excessive Data Exposure",
                "risk": "low",
                "details": "No sensitive fields found in response."
            }
        return {
            "vulnerability": "Excessive Data Exposure",
            "risk": "medium",
            "details": "Response is not JSON."
        }
    except Exception as e:
        return {
            "vulnerability": "Excessive Data Exposure",
            "risk": "medium",
            "details": f"Error during scan: {str(e)}"
        } 