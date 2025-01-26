import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Notifications.css";
import { Link } from "react-router-dom";

function NotificationsPage() {
  const notifications = [
    {
      id: 1,
      sender: "John Doe",
      message: "liked your project.",
      link: "/projects/123",
      avatar: "https://randomuser.me/api/portraits/men/45.jpg",
    },
    {
      id: 2,
      sender: "Jane Smith",
      message: "commented on your post.",
      link: "/posts/456",
      avatar: "https://randomuser.me/api/portraits/women/34.jpg",
    },
    {
      id: 3,
      sender: "Bob Brown",
      message: "sent you a friend request.",
      link: "/friends",
      avatar: "https://randomuser.me/api/portraits/men/12.jpg",
    },
    {
      id: 4,
      sender: "Alice Johnson",
      message: "invited you to collaborate on a project.",
      link: "/projects/collaborate",
      avatar: "https://randomuser.me/api/portraits/women/22.jpg",
    },
    {
      id: 5,
      sender: "Tom White",
      message: "joined your group.",
      link: "/groups/789",
      avatar: "https://randomuser.me/api/portraits/men/67.jpg",
    },
  ];

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Notifications</h1>
      <div className="list-group">
        {notifications.map((notification) => (
          <Link
            key={notification.id}
            to={notification.link}
            className="list-group-item list-group-item-action d-flex align-items-center"
          >
            <img
              src={notification.avatar}
              alt={notification.sender}
              className="rounded-circle me-3"
              width="50"
              height="50"
            />
            <div>
              <strong>{notification.sender}</strong> {notification.message}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default NotificationsPage;
