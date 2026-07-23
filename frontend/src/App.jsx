import "./App.css";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import PromptPage from "./pages/PromptPage";
import PhishingPage from "./pages/PhishingPage";


function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/prompt" element={<PromptPage />} />
        <Route path="/phishing" element={<PhishingPage />} />
      </Routes>
    </>
  );
}

export default App;