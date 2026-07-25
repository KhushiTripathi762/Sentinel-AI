
const BASE_URL = "http://127.0.0.1:8000";

export async function analyzePrompt(prompt) {
  const response = await fetch(`${BASE_URL}/prompt`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: prompt,   // ✅ Backend expects "text"
    }),
  });

  return await response.json();
}

export async function analyzeURL(url) {
  const response = await fetch(`${BASE_URL}/phishing`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url: url,
    }),
  });

  return await response.json();
}