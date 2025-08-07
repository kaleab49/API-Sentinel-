import { useState, useEffect } from 'react';
import ApiForm from './components/ApiForm';
import ResultsPanel from './components/ResultsPanel';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import { scanApi, login, register } from './api/scan';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [authMode, setAuthMode] = useState('login'); // 'login' or 'register'
  const [token, setToken] = useState(() => localStorage.getItem('token'));
  const [authLoading, setAuthLoading] = useState(false);
  const [authError, setAuthError] = useState(null);

  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token);
    } else {
      localStorage.removeItem('token');
    }
  }, [token]);

  const handleScan = async (data) => {
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const res = await scanApi({ ...data, token });
      setResults(res.results);
    } catch (e) {
      setError('Scan failed. Please check the API URL and try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleLogin = async (creds) => {
    setAuthLoading(true);
    setAuthError(null);
    try {
      const res = await login(creds);
      setToken(res.token);
    } catch (e) {
      setAuthError('Invalid username or password.');
    } finally {
      setAuthLoading(false);
    }
  };

  const handleRegister = async (creds) => {
    setAuthLoading(true);
    setAuthError(null);
    try {
      const res = await register(creds);
      setToken(res.token);
    } catch (e) {
      setAuthError('Registration failed. Username may already exist.');
    } finally {
      setAuthLoading(false);
    }
  };

  const handleLogout = () => {
    setToken(null);
    setResults(null);
  };

  if (!token) {
    return (
      <div className="container">
        <h1>API Sentinel</h1>
        {authMode === 'login' ? (
          <>
            <LoginForm onLogin={handleLogin} loading={authLoading} error={authError} />
            <div style={{ marginTop: '1em', textAlign: 'center' }}>
              <span>Don't have an account? </span>
              <button className="scan-btn" onClick={() => setAuthMode('register')}>Register</button>
            </div>
          </>
        ) : (
          <>
            <RegisterForm onRegister={handleRegister} loading={authLoading} error={authError} />
            <div style={{ marginTop: '1em', textAlign: 'center' }}>
              <span>Already have an account? </span>
              <button className="scan-btn" onClick={() => setAuthMode('login')}>Login</button>
            </div>
          </>
        )}
      </div>
    );
  }

  return (
    <div className="container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>API Sentinel</h1>
        <button className="scan-btn" id='logoutbtn' onClick={handleLogout}>Logout</button>
      </div>
      <ApiForm onScan={handleScan} loading={loading} />
      {error && <div className="error-msg">{error}</div>}
      <ResultsPanel results={results} />
    </div>
  );
}

export default App;
