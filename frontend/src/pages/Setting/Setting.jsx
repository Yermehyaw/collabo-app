import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./Settings.css";

const Settings = () => {
  const [user, setUser] = useState({
    name: "John Doe",
    email: "johndoe@example.com",
    profilePicture: "https://randomuser.me/api/portraits/men/1.jpg",
    theme: "light",
    notifications: {
      email: true,
      push: false,
      inApp: true,
    },
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUser((prevUser) => ({ ...prevUser, [name]: value }));
  };

  const handleNotificationChange = (e) => {
    const { name, checked } = e.target;
    setUser((prevUser) => ({
      ...prevUser,
      notifications: { ...prevUser.notifications, [name]: checked },
    }));
  };

  const toggleTheme = () => {
    setUser((prevUser) => ({
      ...prevUser,
      theme: prevUser.theme === "light" ? "dark" : "light",
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Updated User Settings:", user);
    alert("Settings saved successfully!");
  };

  return (
    <div className={`container mt-5 ${user.theme}`}>
      <h2 className="mb-4">User Settings</h2>
      <form onSubmit={handleSubmit}>
        {/* Profile Information */}
        <div className="mb-3">
          <label htmlFor="profilePicture" className="form-label">
            Profile Picture
          </label>
          <div className="d-flex align-items-center">
            <img
              src={user.profilePicture}
              alt="Profile"
              className="rounded-circle me-3"
              style={{ width: "50px", height: "50px" }}
            />
            <input
              type="text"
              id="profilePicture"
              name="profilePicture"
              value={user.profilePicture}
              onChange={handleInputChange}
              className="form-control"
              placeholder="Profile Picture URL"
            />
          </div>
        </div>
        <div className="mb-3">
          <label htmlFor="name" className="form-label">
            Name
          </label>
          <input
            type="text"
            id="name"
            name="name"
            value={user.name}
            onChange={handleInputChange}
            className="form-control"
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={user.email}
            onChange={handleInputChange}
            className="form-control"
          />
        </div>

        {/* Notification Preferences */}
        <fieldset className="mb-3">
          <legend>Notification Preferences</legend>
          <div className="form-check">
            <input
              type="checkbox"
              id="emailNotification"
              name="email"
              checked={user.notifications.email}
              onChange={handleNotificationChange}
              className="form-check-input"
            />
            <label htmlFor="emailNotification" className="form-check-label">
              Email Notifications
            </label>
          </div>
          <div className="form-check">
            <input
              type="checkbox"
              id="pushNotification"
              name="push"
              checked={user.notifications.push}
              onChange={handleNotificationChange}
              className="form-check-input"
            />
            <label htmlFor="pushNotification" className="form-check-label">
              Push Notifications
            </label>
          </div>
          <div className="form-check">
            <input
              type="checkbox"
              id="inAppNotification"
              name="inApp"
              checked={user.notifications.inApp}
              onChange={handleNotificationChange}
              className="form-check-input"
            />
            <label htmlFor="inAppNotification" className="form-check-label">
              In-App Notifications
            </label>
          </div>
        </fieldset>

        {/* Theme Settings */}
        <div className="mb-3">
          <label className="form-label">Theme</label>
          <div>
            <button
              type="button"
              className={`btn btn-${
                user.theme === "light" ? "secondary" : "light"
              }`}
              onClick={toggleTheme}
            >
              Switch to {user.theme === "light" ? "Dark" : "Light"} Mode
            </button>
          </div>
        </div>

        <button type="submit" className="btn btn-primary">
          Save Settings
        </button>
      </form>
    </div>
  );
};

export default Settings;
