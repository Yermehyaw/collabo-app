import React from "react";
import { useLocation, Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const Profile = () => {
  const location = useLocation();
  const { userData } = location.state || {};
  const navigate = useNavigate();
  const isAuthenticated = !!localStorage.getItem("token");

  if (!userData) {
    return (
      <div className="text-center">
        <h2>No user data found. Please log in first.</h2>
        <Link to="/">Go back to Login</Link>
      </div>
    );
  }
  if (!isAuthenticated) {
    navigate("/login"); // Redirect to login if not authenticated
    return null;
  }

  return (
    <div className="container mt-5">
      <h1>Welcome, {userData.fullName}!</h1>
      <p>Title: {userData.title}</p>
      <p>Location: {userData.location}</p>
      <img
        src={userData.avatar}
        alt="Profile Avatar"
        style={{ width: "150px", borderRadius: "50%" }}
      />
      <p>Birthday: {userData.birthday}</p>
      <p>Joined: {userData.joinedDate}</p>
      <p>Mobile: {userData.mobile}</p>
      <p>Email: {userData.email}</p>
      <p>About: {userData.about}</p>
    </div>
  );
};

export default Profile;
