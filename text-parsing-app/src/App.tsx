import "./App.css";

function App() {
  return (
    <div className="container">
      <h1>Text Parsing</h1>
      <form>
        <label>Enter String(Text):</label>
        <textarea placeholder="Example: This is my text." />
        <button>Process</button>
      </form>
    </div>
  );
}

export default App;
