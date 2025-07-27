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
        <button onClick={fetchHistory}>Retry</button>
      </div>
    );
  }

  return (
    <div className="history-panel">
      <h2>History</h2>
      {history.length === 0 ? (
        <p>No challenge hisotry</p>
      ) : (
        <div className="history-list">
          {history.map((challenge) => {
            return (
              <MCQChallenge
                challenge={challenge}
                key={challenge.id}
                showExplanation
              />
            );
          })}
        </div>
      )}
    </div>
  );
};

export default HistoryPanel;
