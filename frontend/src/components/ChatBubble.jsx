export default function ChatBubble({
    role,
    text
}) {

    return (
        <div
            className={
                role === "user"
                ? "message-user"
                : "message-bot"
            }
        >
            {text}
        </div>
    );
}