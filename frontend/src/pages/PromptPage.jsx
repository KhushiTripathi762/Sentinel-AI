import { useState } from "react";
import { analyzePrompt } from "../services/api";

function PromptPage() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleAnalyze() {
    try {
      setLoading(true);

      const data = await analyzePrompt(prompt);

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
      <h1>Prompt Injection Detector</h1>

      <textarea
        rows="8"
        placeholder="Paste your prompt here..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      ></textarea>

      <br />

      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Prompt"}
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

          <h3>Matched Patterns</h3>

          <ul>
            {result.matched_patterns.length > 0 ? (
              result.matched_patterns.map((item, index) => (
                <li key={index}>{item}</li>
              ))
            ) : (
              <li>No suspicious patterns detected.</li>
            )}
          </ul>

          <h3>AI Analysis</h3>

          <p>
            <strong>AI Prediction:</strong> {result.ai_analysis.label}
          </p>

          <p>
            <strong>AI Confidence:</strong> {result.ai_analysis.score}%
          </p>
        </div>
      )}
    </div>
  );
}

export default PromptPage;