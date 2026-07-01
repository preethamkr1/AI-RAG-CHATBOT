import { useNavigate } from "react-router-dom";

export default function Dashboard() {

    const navigate = useNavigate();

    const logout = () => {
        localStorage.removeItem("token");
        navigate("/");
    };

    return (
        <div className="dashboard-container">

            <div className="sidebar">

                <h2 className="sidebar-title">
                    🤖 AI RAG
                </h2>

                <div
                    className="sidebar-item"
                    onClick={() =>
                        navigate("/chat/default")
                    }
                >
                    💬 Chat
                </div>

                <div
                    className="sidebar-item"
                >
                    📄 Documents
                </div>

                <div
                    className="sidebar-item"
                >
                    ⚙ Settings
                </div>

                <div
                    className="sidebar-item"
                    onClick={logout}
                >
                    🚪 Logout
                </div>

            </div>

            <div
                style={{
                    flex: 1,
                    padding: "40px"
                }}
            >

                <h1>
                    Welcome Back 👋
                </h1>

                <p>
                    Your AI Multi-Tenant RAG Assistant
                </p>

                <div
                    style={{
                        display: "grid",
                        gridTemplateColumns:
                            "repeat(auto-fit,minmax(250px,1fr))",
                        gap: "20px",
                        marginTop: "40px"
                    }}
                >

                    <div className="auth-card">
                        <h2>📄 Documents</h2>
                        <h1>1</h1>
                        <p>Uploaded PDFs</p>
                    </div>

                    <div className="auth-card">
                        <h2>💬 Chats</h2>
                        <h1>12</h1>
                        <p>Total Questions Asked</p>
                    </div>

                    <div className="auth-card">
                        <h2>🧠 Vector Store</h2>
                        <h1>Ready</h1>
                        <p>FAISS Database Active</p>
                    </div>

                </div>

                <div
                    style={{
                        marginTop: "40px"
                    }}
                >

                    <button
                        className="auth-button"
                        style={{
                            width: "250px",
                            marginRight: "20px"
                        }}
                        onClick={() =>
                            navigate(
                                "/chat/default"
                            )
                        }
                    >
                        Open Chat
                    </button>

                </div>

            </div>

        </div>
    );
}