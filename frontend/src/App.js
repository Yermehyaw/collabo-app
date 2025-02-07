import React, { useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import jwtDecode from "jwt-decode";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import "./pages/home/Home.css";
import "./assets/styles/global.css";
import "./components/Navbar/Navbar.css";
import "./components/Navbar/Sidebar.css";
import Layout from "./components/Layout/Layout";
import Profile from "./pages/profile/Profile";
import ProjectPage from "./pages/projectdetails/projectDetails";

// Check for expired token before server returns a 401
const getToken = () => {
  const token = localStorage.getItem("token");
  if (!token) {
    return null
  }

  try {
    const decoded = jwtDecode(token);
    if (decoded.expires_in * 1000 < Date.now()) {
      localStorage.removeItem("token");
      return null;
    }
    return token;
  } catch (error) {
    return null;
  }
};

const App = () => {
  // Manage authetication in state
  const [token, setToken] = useState(getToken());

  // Handles saving the token in state and to local storage
  const handleSetToken = (userToken) => {
    localStorage.setItem("token", userToken);
    setToken(userToken);
  };

  const isAuthenticated = !!token; // Check if user is authenticated

  return (
    <Router>
      <Routes>
        {/* All routes inside Layout will have the Navbar and Footer */}
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} /> {/* Home page */}
          <Route
            path="/profile"
            element={isAuthenticated ? <Profile /> : <Navigate to="/Login" />}
          />{" "}
          <Route path="/ProjectDetails" element={<ProjectPage />} />{" "}
          {/* Add more routes here for other pages */}
        </Route>
        <Route path="/login" element={<Login setToken={handleSetToken}/>} />
      </Routes>
    </Router>
  );
};

export default App;
