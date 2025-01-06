import React, { useState, useEffect } from "react";
import "./Profile.css";

const Profile = () => {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // Simulating a backend API response
    const mockData = {
      fullName: "Amanda S. Ross",
      title: "Senior Software Engineer at Tailwind CSS",
      location: "New York, USA",
      avatar: "https://example.com/avatar.jpg",
      birthday: "24 Jul, 1991",
      joinedDate: "10 Jan 2022",
      mobile: "(123) 123-1234",
      email: "amandaross@example.com",
      about: "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
      totalRevenue: "$12,345",
      newOrders: "32",
      newConnections: "5",
    };

    setUserData(mockData); // Set mock data as user data
  }, []);

  if (!userData) {
    return <p>Loading profile...</p>;
  }

  fetch("http://localhost:5000/api/user-profile")
    .then((response) => response.json())
    .then((data) => setUserData(data));

  return (
    <div className="profile-container">
      <div className="profile-cover">
        <div className="profile-avatar">
          <img src={userData.avatar} alt={`${userData.fullName}'s avatar`} />
        </div>
      </div>
      <div className="profile-details">
        <h2>{userData.fullName}</h2>
        <p>{userData.title}</p>
        <p>{userData.location}</p>
      </div>
      <div className="profile-sections">
        <div className="personal-info">
          <h3>Personal Info</h3>
          <p>
            <strong>Full name:</strong> {userData.fullName}
          </p>
          <p>
            <strong>Birthday:</strong> {userData.birthday}
          </p>
          <p>
            <strong>Joined:</strong> {userData.joinedDate}
          </p>
          <p>
            <strong>Mobile:</strong> {userData.mobile}
          </p>
          <p>
            <strong>Email:</strong> {userData.email}
          </p>
          <p>
            <strong>Location:</strong> {userData.location}
          </p>
        </div>
        <div className="about-info">
          <h3>About</h3>
          <p>{userData.about}</p>
        </div>
      </div>
      <div className="profile-statistics">
        <div>
          <h3>Total Revenue</h3>
          <p>{userData.totalRevenue}</p>
        </div>
        <div>
          <h3>New Orders</h3>
          <p>{userData.newOrders}</p>
        </div>
        <div>
          <h3>New Connections</h3>
          <p>{userData.newConnections}</p>
        </div>
      </div>
      <div className="profile-actions">
        <button className="btn btn-primary">Connect</button>
        <button className="btn btn-secondary">Message</button>
      </div>
    </div>
  );
};

export default Profile;
