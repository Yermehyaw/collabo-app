import React from "react";
import { useLocation, Link } from "react-router-dom";

const Profile = () => {
  const location = useLocation();
  const { userData } = location.state || {};

  if (!userData) {
    return (
      <div className="text-center">
        <h2>No user data found. Please log in first.</h2>
        <Link to="/">Go back to Login</Link>
      </div>
    );
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
