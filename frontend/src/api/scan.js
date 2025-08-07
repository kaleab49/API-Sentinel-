export async function login({ username, password }) {
  const res = await fetch('http://localhost:8000/api/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) throw new Error('Login failed');
  return res.json();
}

export async function register({ username, password }) {
  const res = await fetch('http://localhost:8000/api/register/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) throw new Error('Register failed');
  return res.json();
}

export async function scanApi({ url, headers, token }) {
  const res = await fetch('http://localhost:8000/api/scan/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`,
    },
    body: JSON.stringify({ url, headers }),
  });
  if (!res.ok) throw new Error('Scan failed');
  return res.json();
} 