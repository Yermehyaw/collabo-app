import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "./MessagingApp.css";
import "bootstrap-icons/font/bootstrap-icons.css"; // Bootstrap Icons

const socket = io("http://localhost:3000"); // Connect to WebSocket server

const MessagingApp = () => {
  const [message, setMessage] = useState("[]");
  const [messageInput, setMessageInput] = useState("");
  const [username, setUsername] = useState(
    "User" + Math.floor(Math.random() * 1000)
  );

  useEffect(() => {
    socket.on("message", (message) => {
      setMessage((prevMessages) => [...prevMessages, message]);
    });
  });

  const [activeContact, setActiveContact] = useState("John Doe");
  const [messages, setMessages] = useState([
    {
      sender: "John Doe",
      content: "Hello, how are you?",
      timestamp: new Date().toLocaleTimeString([], {
        minute: "2-digit",
        second: "2-digit",
      }),
      status: "read",
    },
    {
      sender: "You",
      content: "I'm good, thank you! How about you?",
      timestamp: new Date().toLocaleTimeString([], {
        minute: "2-digit",
        second: "2-digit",
      }),
      status: "read",
    },
  ]);

  const contacts = [
    { name: "John Doe", img: "https://randomuser.me/api/portraits/men/1.jpg" },
    {
      name: "Jane Smith",
      img: "https://randomuser.me/api/portraits/women/2.jpg",
    },
    { name: "Bob Brown", img: "https://randomuser.me/api/portraits/men/3.jpg" },
    {
      name: "Alice Johnson",
      img: "https://randomuser.me/api/portraits/women/4.jpg",
    },
    {
      name: "Charlie Davis",
      img: "https://randomuser.me/api/portraits/men/5.jpg",
    },
  ];

  const handleSendMessage = (e) => {
    e.preventDefault();
    const messageInput = e.target.message.value;
    if (messageInput.trim()) {
      setMessages([...messages, { sender: "You", content: messageInput }]);
      e.target.reset();
    }
  };

  return (
    <div className="container-fluid bg-light">
      <div className="row">
        {/* Contact Bubbles for Mobile View */}
        <div className="col-12 contact-bubbles d-md-none">
          {contacts.map((contact) => (
            <img
              key={contact.name}
              src={contact.img}
              alt={contact.name}
              data-name={contact.name}
              onClick={() => setActiveContact(contact.name)}
            />
          ))}
        </div>
        {/* Sidebar for Desktop View */}
        <div className="col-md-3 bg-white border-right sidebar d-none d-md-block">
          <div className="p-4 border-bottom">
            <h1 className="text-2xl font-bold text-primary">Messages</h1>
          </div>
          <div className="p-4">
            <div className="input-group mb-3">
              <input
                type="text"
                className="form-control"
                placeholder="Search contacts"
                aria-label="Search contacts"
              />
              <div className="input-group-append">
                <button className="btn btn-outline-secondary" type="button">
                  <i className="bi bi-search"></i>
                </button>
              </div>
            </div>
            <ul className="list-unstyled">
              {contacts.map((contact) => (
                <li
                  key={contact.name}
                  className="media p-2 hover:bg-light cursor-pointer"
                  onClick={() => setActiveContact(contact.name)}
                >
                  <img
                    src={contact.img}
                    alt="Avatar"
                    className="mr-3 rounded-circle"
                    width="40"
                    height="40"
                  />
                  <div className="media-body">
                    <h5 className="mt-0 mb-1">{contact.name}</h5>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
        {/* Conversation Area */}
        <div className="col-md-9 bg-white">
          <div className="p-4 border-bottom d-flex align-items-center">
            <img
              src={
                contacts.find((contact) => contact.name === activeContact)?.img
              }
              alt="Avatar"
              className="rounded-circle mr-3"
              width="40"
              height="40"
            />
            <h2 className="text-xl font-bold text-dark mb-0">
              {activeContact}
            </h2>
          </div>
          <div className="p-4 conversation-area">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`media mb-4 ${
                  message.sender === "You" ? "flex-row-reverse" : ""
                }`}
              >
                <img
                  src={
                    message.sender === "You"
                      ? "https://via.placeholder.com/30"
                      : contacts.find(
                          (contact) => contact.name === message.sender
                        )?.img
                  }
                  alt="Avatar"
                  className="mr-3 rounded-circle"
                  width="30"
                  height="30"
                />
                <div
                  className={`media-body p-3 rounded ${
                    message.sender === "You"
                      ? "user-message" // Add this class for user messages
                      : "incoming-message"
                  }`}
                >
                  <p className="mb-0">{message.content}</p>
                </div>
              </div>
            ))}
          </div>
          <div className="message-input">
            <form onSubmit={handleSendMessage}>
              <div className="input-group">
                <div className="input-group-prepend d-flex">
                  <button className="btn btn-outline-secondary" type="button">
                    <i className="bi bi-paperclip"></i>
                  </button>
                  <button
                    className="btn btn-outline-secondary ms-2 bg-warning"
                    type="button"
                  >
                    <i className="bi bi-emoji-smile"></i>
                  </button>
                </div>
                <input
                  type="text"
                  className="form-control ms-2"
                  name="message"
                  placeholder="Type a message"
                  required
                />
                <div className="input-group-append">
                  <button className="btn btn-primary" type="submit">
                    &#10148;
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MessagingApp;
