import "react";
import { useState } from "react";

const MCQChallenge = ({ challnge, showExplanation = false }) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [shouldShowExplanation, setShouldExplanation] =
    useState(showExplanation);

  const options =
    typeof challnge.options === "string"
      ? JSON.parse(challnge.options)
      : challnge.options;

  return <div></div>;
};

export default MCQChallenge;
