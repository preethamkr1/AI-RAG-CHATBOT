export default function Sidebar() {
    return (
        <div className="sidebar">

            <h2 className="sidebar-title">
                🤖 AI RAG
            </h2>

            <button className="new-chat-btn">
                + New Chat
            </button>

            <div className="sidebar-section">
                <h4>Documents</h4>

                <div className="sidebar-item">
                    📄 Resume.pdf
                </div>

                <div className="sidebar-item">
                    📄 Result.pdf
                </div>
            </div>

            <div className="sidebar-section">
                <h4>Recent Chats</h4>

                <div className="sidebar-item">
                    CGPA Discussion
                </div>

                <div className="sidebar-item">
                    Resume Analysis
                </div>
            </div>

        </div>
    );
}