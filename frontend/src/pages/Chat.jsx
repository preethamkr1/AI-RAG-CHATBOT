import { useState } from "react";
import api from "../services/api";

export default function Chat() {

    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [file, setFile] = useState(null);
    const [uploadStatus, setUploadStatus] = useState("");
    const [chatId, setChatId] = useState(
        Date.now().toString()
    );

    const sendMessage = async () => {

        if (!question.trim()) return;

        const userMessage = {
            role: "user",
            text: question
        };

        setMessages(prev => [
            ...prev,
            userMessage
        ]);

        try {

            const response = await api.post(
                "/ask",
                {
                    question,
                    session_id: chatId
                }
            );

            const botMessage = {
                role: "assistant",
                text: response.data.answer
            };

            setMessages(prev => [
                ...prev,
                botMessage
            ]);

            setQuestion("");

        } catch (error) {

            console.log(error);

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    text: "Failed to get response."
                }
            ]);
        }
    };

    const uploadPDF = async () => {

        if (!file) {
            alert("Please select a PDF file");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {

            const response = await api.post(
                "/upload-pdf",
                formData,
                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data"
                    }
                }
            );

            setUploadStatus(
                `✅ ${response.data.filename} uploaded`
            );

            setFile(null);

        } catch (error) {

            console.log(error);

            setUploadStatus(
                "❌ Upload failed"
            );
        }
    };

    const clearChat = () => {
        setMessages([]);
    };

    const newChat = () => {
        setMessages([]);
        setChatId(
            Date.now().toString()
        );
    };

    return (

        <div className="dashboard-container">

            {/* Sidebar */}

            <div className="sidebar">

                <h2 className="sidebar-title">
                    🤖 AI RAG
                </h2>

                <button
                    className="auth-button"
                    onClick={newChat}
                    style={{
                        marginBottom: "15px"
                    }}
                >
                    + New Chat
                </button>

                <button
                    className="auth-button"
                    onClick={clearChat}
                    style={{
                        marginBottom: "25px"
                    }}
                >
                    Clear Chat
                </button>

                <h3>
                    Upload PDF
                </h3>

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) =>
                        setFile(
                            e.target.files[0]
                        )
                    }
                    style={{
                        marginTop: "10px",
                        marginBottom: "15px"
                    }}
                />

                <button
                    className="auth-button"
                    onClick={uploadPDF}
                >
                    Upload
                </button>

                <p
                    style={{
                        marginTop: "15px",
                        fontSize: "14px"
                    }}
                >
                    {uploadStatus}
                </p>

            </div>

            {/* Main Chat */}

            <div className="chat-container">

                <div className="chat-header">

                    <h2>
                        AI RAG Assistant
                    </h2>

                </div>

                {/* Messages */}

                <div className="chat-messages">

                    {
                        messages.length === 0 &&
                        (
                            <div
                                style={{
                                    textAlign:
                                        "center",
                                    marginTop:
                                        "100px",
                                    color:
                                        "#94A3B8"
                                }}
                            >
                                <h2>
                                    Welcome 👋
                                </h2>

                                <p>
                                    Upload a PDF and start asking questions.
                                </p>
                            </div>
                        )
                    }

                    {
                        messages.map(
                            (
                                msg,
                                index
                            ) => (
                                <div
                                    key={index}
                                    style={{
                                        display:
                                            "flex",
                                        justifyContent:
                                            msg.role ===
                                            "user"
                                                ? "flex-end"
                                                : "flex-start",
                                        marginBottom:
                                            "20px"
                                    }}
                                >
                                    <div
                                        className={
                                            msg.role ===
                                            "user"
                                                ? "message-user"
                                                : "message-bot"
                                        }
                                    >
                                        {
                                            msg.text
                                        }
                                    </div>
                                </div>
                            )
                        )
                    }

                </div>

                {/* Input */}

                <div className="chat-input-container">

                    <textarea
                        className="chat-input"
                        value={question}
                        onChange={(e) =>
                            setQuestion(
                                e.target.value
                            )
                        }
                        placeholder="Ask anything about your documents..."
                        rows={3}
                        onKeyDown={(e) => {

                            if (
                                e.key === "Enter" &&
                                !e.shiftKey
                            ) {

                                e.preventDefault();
                                sendMessage();
                            }
                        }}
                    />

                    <button
                        className="send-button"
                        onClick={sendMessage}
                    >
                        Send
                    </button>

                </div>

            </div>

        </div>
    );
}