import React, { useState } from "react";
import API from "../services/api";

function Chatbot() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const askQuestion = async () => {
        try {
            const response = await API.post("/chat", {
                question: question
            });

            setAnswer(response.data.answer);
        } catch (error) {
            console.error(error);
            alert("Unable to get response from chatbot.");
        }
    };

    return (
        <div className="card p-4 mt-4">
            <h3>🏦 Banking Assistant</h3>

            <input
                className="form-control mt-3"
                type="text"
                placeholder="Ask a banking question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />

            <button
                className="btn btn-success mt-3"
                onClick={askQuestion}
            >
                Ask
            </button>

            <div className="mt-4">
                <h5>Answer</h5>
                <p>{answer}</p>
            </div>
        </div>
    );
}

export default Chatbot;