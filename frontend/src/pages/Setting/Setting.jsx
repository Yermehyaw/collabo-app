import React, { useState, useEffect } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./Settings.css";

const Settings = () => {
  const [user, setUser] = useState({
    name: "",
    email: "",
    profilePicture: "",
    theme: "light",
    notifications: {
      email: false,
      push: false,
      inApp: false,
    },
  });

  const [isEditing, setIsEditing] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  // Fetch user data from the backend
  useEffect(() => {
    axios
      .get("/api/user") // Replace with your backend endpoint
      .then((response) => {
        setUser(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching user data:", error);
        setIsLoading(false);
      });
  }, []);

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

  const handleProfilePictureChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setUser((prevUser) => ({
          ...prevUser,
          profilePicture: e.target.result,
        }));
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .put("/api/user", user) // Replace with your backend endpoint
      .then((response) => {
        alert("Settings saved successfully!");
        setIsEditing(false);
      })
      .catch((error) => {
        console.error("Error saving settings:", error);
        alert("Failed to save settings. Please try again.");
      });
  };

  if (isLoading) {
    return <div className="container mt-5">Loading user settings...</div>;
  }

  return (
    <div className={`container mt-5 ${user.theme}`}>
      <h2 className="mb-4">User Settings</h2>
      <div className="card shadow-sm">
        <div className="card-body">
          {/* Profile Picture */}
          <div className="d-flex align-items-center mb-4">
            <img
              src={user.profilePicture || "https://via.placeholder.com/100"}
              alt="Profile"
              className="rounded-circle me-3"
              style={{ width: "100px", height: "100px", objectFit: "cover" }}
            />
            <button
              className="btn btn-outline-primary"
              onClick={() => setIsEditing(!isEditing)}
            >
              {isEditing ? "Cancel" : "Edit"}
            </button>
          </div>

          {isEditing ? (
            <form onSubmit={handleSubmit}>
              {/* Name */}
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

              {/* Email */}
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

              {/* Change Password */}
              <div className="mb-3">
                <label htmlFor="password" className="form-label">
                  Change Password
                </label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  placeholder="New Password"
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
                  <label
                    htmlFor="emailNotification"
                    className="form-check-label"
                  >
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
                  <label
                    htmlFor="pushNotification"
                    className="form-check-label"
                  >
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
                  <label
                    htmlFor="inAppNotification"
                    className="form-check-label"
                  >
                    In-App Notifications
                  </label>
                </div>
              </fieldset>

              {/* Profile Picture Upload */}
              <div className="mb-3">
                <label htmlFor="profilePicture" className="form-label">
                  Update Profile Picture
                </label>
                <input
                  type="file"
                  id="profilePicture"
                  onChange={handleProfilePictureChange}
                  className="form-control"
                  accept="image/*"
                />
              </div>

              <button type="submit" className="btn btn-primary">
                Save Changes
              </button>
            </form>
          ) : (
            <div>
              <p>
                <strong>Name:</strong> {user.name}
              </p>
              <p>
                <strong>Email:</strong> {user.email}
              </p>
              <p>
                <strong>Theme:</strong>{" "}
                {user.theme === "light" ? "Light Mode" : "Dark Mode"}
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Settings;
