import { useState } from 'react';
import ApiForm from './components/ApiForm';
import ResultsPanel from './components/ResultsPanel';
import { scanApi } from './api/scan';
import './App.css';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleScan = async (data) => {
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const res = await scanApi(data);
      setResults(res.results);
    } catch (e) {
      setError('Scan failed. Please check the API URL and try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>API Sentinel</h1>
      <ApiForm onScan={handleScan} loading={loading} />
      {error && <div className="error-msg">{error}</div>}
      <ResultsPanel results={results} />
    </div>
  );
}

export default App;
