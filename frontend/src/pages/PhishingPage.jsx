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

      <br />

      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze URL"}
      </button>

      {result && (
  <div className="result-card">
    <h2>Analysis Result</h2>

    <p><strong>Attack Type:</strong> {result.attack_type}</p>
    <p>
  <strong>Risk:</strong>{" "}
  <span className={result.risk.toLowerCase()}>
    {result.risk}
  </span>
</p>
    <p><strong>Confidence:</strong> {result.confidence}%</p>
    <p><strong>Recommendation:</strong> {result.recommendation}</p>

    <strong>Reasons:</strong>

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