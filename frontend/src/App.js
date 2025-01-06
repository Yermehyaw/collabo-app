import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Home from "./pages/home/Home";
import Login from "./pages/Login/Login";
import "./pages/home/Home.css";
import "./assets/styles/global.css";
import "./components/Navbar/Navbar.css";
import "./components/Navbar/Sidebar.css";
import Layout from "./components/Layout/Layout";
import Profile from "./pages/profile/Profile";

const App = () => {
  const isAuthenticated = !!localStorage.getItem("token"); // Check if user is authenticated

  return (
    <Router>
      <Routes>
        {/* All routes inside Layout will have the Navbar and Footer */}
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} /> {/* Home page */}
          <Route
            path="/Profile"
            element={isAuthenticated ? <Profile /> : <Navigate to="/Login" />}
          />{" "}
          {/* Add more routes here for other pages */}
        </Route>
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
};

export default App;
