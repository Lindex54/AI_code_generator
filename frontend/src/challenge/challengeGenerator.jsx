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

  return <div></div>;
};

export default ChallengeGenerator;
