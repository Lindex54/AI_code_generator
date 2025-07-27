import "react";
import { useState, useEffect } from "react";
import MCQChallenge from "../challenge/MCQChallenge";

const HistoryPanel = () => {
  const [history, setHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  return <div></div>;
};

export default HistoryPanel;
