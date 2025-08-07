export async function scanApi({ url, headers }) {
  const res = await fetch('http://localhost:8000/api/scan/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url, headers }),
  });
  if (!res.ok) throw new Error('Scan failed');
  return res.json();
} 