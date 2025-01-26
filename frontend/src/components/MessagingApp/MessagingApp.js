import React, { useState, useEffect } from "react";
import "./MessagingApp.css";
import io from "socket.io-client"; // Install with `npm install socket.io-client`

const socket = io("http://your-backend-url"); // Replace with your backend's URL

const MessagingApp = ({ userId }) => {
  const [messages, setMessages] = useState([]); // List of messages
  const [inputMessage, setInputMessage] = useState(""); // Current input message
  const [chatUser, setChatUser] = useState({ name: "", profilePicture: "" }); // Chat user details
  const [isVisible, setIsVisible] = useState(true); // Visibility state

  // Fetch user and chat data on load
  useEffect(() => {
    // Fetch chat user details
    fetch(`http://your-backend-url/api/chat-user/${userId}`)
      .then((response) => response.json())
      .then((data) => setChatUser(data))
      .catch((err) => console.error("Error fetching user details:", err));

    // Fetch chat history
    fetch(`http://your-backend-url/api/chats/${userId}`)
      .then((response) => response.json())
      .then((data) => setMessages(data))
      .catch((err) => console.error("Error fetching chat history:", err));

    // Listen for real-time messages
    socket.on("receiveMessage", (newMessage) => {
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    });

    // Cleanup listener on unmount
    return () => {
      socket.off("receiveMessage");
    };
  }, [userId]);

  // Handle sending a message
  const handleSendMessage = () => {
    if (inputMessage.trim() === "") return;

    const newMessage = {
      sender: "You",
      text: inputMessage,
      timestamp: new Date().toISOString(),
    };

    // Emit the message to the backend
    socket.emit("sendMessage", { userId, message: newMessage });

    // Update local messages
    setMessages([...messages, newMessage]);
    setInputMessage(""); // Clear the input field
  };

  // If not visible, don't render the component
  if (!isVisible) return null;

  return (
    <div className="messaging-app">
      {/* Header */}
      <div className="messaging-header bg-dark">
        <img
          src={chatUser.profilePicture}
          alt={`${chatUser.name}'s profile`}
          className="profile-picture"
        />
        <h5>{chatUser.name}</h5>
        <button
          className="close-btn btn btn-sm btn-danger"
          onClick={() => setIsVisible(false)} // Close button
        >
          ✖
        </button>
      </div>

      {/* Chat Body */}
      <div className="messaging-body">
        <div className="messages-list">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${
                msg.sender === "You" ? "my-message" : "other-message"
              }`}
            >
              <strong>{msg.sender}: </strong>
              <span>{msg.text}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Chat Footer */}
      <div className="messaging-footer">
        <input
          type="text"
          className="form-control"
          placeholder="Type your message..."
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSendMessage();
          }}
        />
        <button
          className="btn btn-primary send-btn"
          onClick={handleSendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default MessagingApp;
