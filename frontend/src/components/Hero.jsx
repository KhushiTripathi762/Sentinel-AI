import { useNavigate } from "react-router-dom";

function Hero() {
  const navigate = useNavigate();

  return (
    <section className="hero">
      <h1>AI-Powered Cybersecurity Assistant</h1>

      <p>
        Detect Prompt Injection attacks and Phishing URLs
        using Artificial Intelligence.
      </p>

      <button onClick={() => navigate("/prompt")}>
        Get Started
      </button>
    </section>
  );
}

export default Hero;