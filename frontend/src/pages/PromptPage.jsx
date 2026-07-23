import { useState } from "react";
import { analyzePrompt } from "../services/api";

function PromptPage() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);

  async function handleAnalyze() {
  try {
    const data = await analyzePrompt(prompt);
    setResult(data);
  } catch (error) {
    console.error(error);
    alert("Backend is not running or API connection failed.");
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

      <button onClick={handleAnalyze}>
        Analyze Prompt
      </button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}

export default PromptPage;