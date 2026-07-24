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

    <strong>Matched Patterns:</strong>

    <ul>
      {result.matched_patterns.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  </div>
)}
    </div>
  );
}

export default PromptPage;