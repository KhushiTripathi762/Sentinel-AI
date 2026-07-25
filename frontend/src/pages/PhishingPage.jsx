import { useState } from "react";
import { analyzeURL } from "../services/api";

function PhishingPage() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleAnalyze() {
    try {
      setLoading(true);

      const data = await analyzeURL(url);
      setResult(data);

    } catch (error) {
      console.error(error);
      alert("Backend is not running or API connection failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="prompt-page">

      <h1>Phishing URL Detector</h1>

      <input
        type="text"
        placeholder="Enter website URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze URL"}
      </button>

      {result && (
        <div className="result-card">

          <h2>🛡 Sentinel AI Report</h2>

          <p>
            <strong>Attack Type:</strong> {result.attack_type}
          </p>

          <p>
            <strong>Risk:</strong>{" "}
            <span
              className={
                result.risk === "High"
                  ? "risk-high"
                  : result.risk === "Medium"
                  ? "risk-medium"
                  : "risk-low"
              }
            >
              {result.risk}
            </span>
          </p>

          <div className="confidence-section">
            <strong>Confidence:</strong>

            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{ width: `${result.confidence}%` }}
              ></div>
            </div>

            <span>{result.confidence}%</span>
          </div>

          <p>
            <strong>Recommendation:</strong>{" "}
            <span
              className={
                result.recommendation === "Block"
                  ? "rec-block"
                  : result.recommendation === "Review"
                  ? "rec-review"
                  : "rec-allow"
              }
            >
              {result.recommendation}
            </span>
          </p>

          <h3>Reasons</h3>

          <ul>
            {result.reasons.map((reason, index) => (
              <li key={index}>{reason}</li>
            ))}
          </ul>

        </div>
      )}

    </div>
  );
}

export default PhishingPage;