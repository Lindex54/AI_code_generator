import "react";
import { useState, useEffect } from "react";
import MCQChallenge from "../challenge/MCQChallenge";

const HistoryPanel = () => {
  const [history, setHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    setIsLoading(false);
  };

  if (isLoading) {
    return <div className="loading">Loading history...</div>;
  }

  if (error) {
    return (
      <div className="erro-message">
        <p>{error}</p>
      </div>
    );
  }

  return <div></div>;
};

export default HistoryPanel;
