import { useState } from "react";
import "./App.css";

const URL = "https://5g47lc6193.execute-api.us-east-1.amazonaws.com/test";

function App() {
  const [inputText, setInputText] = useState("");
  const [apiResponse, setApiResponse] = useState("");

  const handleProcess = async () => {
    try {
      const response = await fetch(URL, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          text: inputText,
        }),
      });
      const data = await response.json();
      setApiResponse(data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="container">
      <h1>Text Parsing</h1>
      <form>
        <label>Enter String(Text):</label>
        <textarea
          placeholder="Example: This is my text."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <button type="button" onClick={handleProcess}>Process</button>
      </form>
      {apiResponse && (
        <div>
          <h2>API Response:</h2>
          <pre>{JSON.stringify(apiResponse, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
