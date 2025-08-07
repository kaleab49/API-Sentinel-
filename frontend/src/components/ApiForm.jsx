import React, { useState } from 'react';

const ApiForm = ({ onScan, loading }) => {
  const [url, setUrl] = useState('');
  const [headers, setHeaders] = useState([{ key: '', value: '' }]);

  const handleHeaderChange = (idx, field, value) => {
    const newHeaders = [...headers];
    newHeaders[idx][field] = value;
    setHeaders(newHeaders);
  };

  const addHeader = () => setHeaders([...headers, { key: '', value: '' }]);
  const removeHeader = idx => setHeaders(headers.filter((_, i) => i !== idx));

  const handleSubmit = e => {
    e.preventDefault();
    const headerObj = {};
    headers.forEach(h => {
      if (h.key && h.value) headerObj[h.key] = h.value;
    });
    onScan({ url, headers: headerObj });
  };

  return (
    <form className="api-form" onSubmit={handleSubmit}>
      <label>
        API URL:
        <input
          type="url"
          value={url}
          onChange={e => setUrl(e.target.value)}
          required
          placeholder="https://api.example.com/v1/users"
        />
      </label>
      <div className="headers-section">
        <div className="headers-label">Headers (optional):</div>
        {headers.map((h, idx) => (
          <div className="header-row" key={idx}>
            <input
              type="text"
              placeholder="Key"
              value={h.key}
              onChange={e => handleHeaderChange(idx, 'key', e.target.value)}
            />
            <input
              type="text"
              placeholder="Value"
              value={h.value}
              onChange={e => handleHeaderChange(idx, 'value', e.target.value)}
            />
            {headers.length > 1 && (
              <button type="button" onClick={() => removeHeader(idx)} className="remove-header">×</button>
            )}
          </div>
        ))}
        <button type="button" onClick={addHeader} className="add-header">+ Add Header</button>
      </div>
      <button type="submit" disabled={loading} className="scan-btn">
        {loading ? 'Scanning...' : 'Scan API'}
      </button>
    </form>
  );
};

export default ApiForm; 