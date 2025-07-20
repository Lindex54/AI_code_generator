import "react";
import { useState, useEffect } from "react";
import { MCQChallenge } from "./MCQChallenge.jsx";

const ChallengeGenerator = () => {
  const [challenge, setChallenge] = useState(null);
  const [isLoading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [difficulty, setDifficulty] = useState("easy");

  const fetchQuota = async () => {};

  const generateChallenge = async () => {};

  const getNextResetTime = () => {};

  return (
    <div className="challenge-container">
      <h2>Coding Challenge Generator</h2>
      <div className="quota-display">
        <p>Challenges remaining today: {quota?.quota_remaining || 0}</p>
        {quota?.quota_remaining === 0 && <p>Next reset: {0}</p>}
      </div>
      <div className="difficulty-selector">
        <label>Select Difficulty</label>
      </div>
    </div>
  );
};

export default ChallengeGenerator;
