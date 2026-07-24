import { useState } from "react";
import { analyzeURL } from "../services/api";

function PhishingPage() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);

  async function handleAnalyze() {
  try {
    console.log("Button clicked");
    const data = await analyzeURL(url);
    console.log(data);
    setResult(data);
  } catch (error) {
    console.error("Error:", error);
    alert(error.message);
  }
}

  return (
    <div>
      <h1>Phishing URL Detector</h1>

      <input
        type="text"
        placeholder="Enter website URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <br /><br />

      <button onClick={handleAnalyze}>
        Analyze URL
      </button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}

export default PhishingPage;