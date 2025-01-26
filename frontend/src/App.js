import React, { useEffect, useState } from "react";
import Axios from "axios";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Navbar from "./components/Navbar/Navbar.jsx";
import HeroSection from "./components/HeroSection/heroSection.jsx";
import Login from "./pages/login/Login";
import "./assets/styles/global.css";
import "./components/Navbar/Navbar.css";
import Profile from "./pages/profile/Profile";
import SignUp from "./pages/signUp/SignUp.jsx";
import Peers from "./pages/Peers/peers.jsx";
import Projects from "./pages/Project/Project.jsx";
import CreateProject from "./pages/createProject/createProject.jsx";
import Footer from "./components/Footer/Footer.jsx";
import MessagingApp from "./components/MessagingApp/MessagingApp.jsx";
import Notifications from "./components/Notifications/Notification.jsx";
import Settings from "./pages/Setting/Setting.jsx";

// Axios Configuration
Axios.defaults.baseURL = "http://localhost:5000/api"; // Backend Base URL
Axios.defaults.headers.common["Authorization"] = `Bearer ${localStorage.getItem(
  "token"
)}`; // Attach token to every request if available

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(
    !!localStorage.getItem("token")
  ); // Track authentication state
  const [data, setData] = useState(""); // Backend data
  const [error, setError] = useState(null); // Handle errors

  // Fetch Data from Backend
  const getData = async () => {
    try {
      const response = await Axios.get("/"); // Replace '/' with your backend endpoint if needed
      setData(response.data);
    } catch (err) {
      console.error("Error fetching data:", err);
      setError("Failed to fetch data from the server.");
    }
  };

  // Refresh authentication state
  const handleAuthenticationChange = () => {
    const token = localStorage.getItem("token");
    setIsAuthenticated(!!token);
  };

  useEffect(() => {
    getData();
    handleAuthenticationChange(); // Ensure auth state is updated on component mount
  }, []);

  return (
    <Router>
      <Navbar
        isAuthenticated={isAuthenticated}
        onAuthChange={handleAuthenticationChange}
      />
      <Routes>
        <Route path="/" element={<HeroSection data={data} />} />{" "}
        {/* Home page */}
        <Route
          path="/profile"
          element={
            isAuthenticated ? <Profile /> : <Navigate to="/login" replace />
          }
        />
        <Route
          path="/login"
          element={<Login onAuthChange={handleAuthenticationChange} />}
        />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/peers" element={<Peers />} />
        <Route path="/createProject" element={<CreateProject />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="Notifications" element={<Notifications />} />
        <Route path="Settings" element={<Settings />} />
        <Route path="/MessagingApp" element={<MessagingApp />} />
      </Routes>
      {error && <p className="error-message">{error}</p>}{" "}
      {/* Display error if it exists */}
      <Footer />
    </Router>
  );
};

export default App;
