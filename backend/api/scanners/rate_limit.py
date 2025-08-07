import requests
import time

def scan_rate_limiting(url, headers=None):
    try:
        hit_429 = False
        for _ in range(5):
            resp = requests.get(url, headers=headers, timeout=5)
            if resp.status_code == 429:
                hit_429 = True
                break
            time.sleep(0.2)
        if hit_429:
            return {
                "vulnerability": "Missing Rate Limiting",
                "risk": "low",
                "details": "Rate limiting detected (429 received)."
            }
        return {
            "vulnerability": "Missing Rate Limiting",
            "risk": "high",
            "details": "No rate limiting detected after multiple rapid requests."
        }
    except Exception as e:
        return {
            "vulnerability": "Missing Rate Limiting",
            "risk": "medium",
            "details": f"Error during scan: {str(e)}"
        } 