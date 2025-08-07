import React from 'react';

const riskColor = {
  low: '#4caf50',
  medium: '#ff9800',
  high: '#f44336',
};

const ResultsPanel = ({ results }) => {
  if (!results) return null;
  return (
    <div className="results-panel">
      <h2>Scan Results</h2>
      <ul>
        {results.map((r, idx) => (
          <li key={idx} className="result-item">
            <div className="vuln-title">
              <span className="vuln-name">{r.vulnerability}</span>
              <span
                className="risk-badge"
                style={{ background: riskColor[r.risk] || '#ccc' }}
              >
                {r.risk.toUpperCase()}
              </span>
            </div>
            <div className="vuln-details">{r.details}</div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ResultsPanel; 