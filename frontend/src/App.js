import React from "react";
import Navbar from "./components/Navbar/Navbar";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import "./pages/home/Home.css";
import "./assets/styles/global.css";
import "./components/Navbar/Navbar.css";
import "./components/Navbar/Sidebar.css";
import Footer from "./components/Footer/Footer";

import Profile from "./pages/profile/Profile";
import Features from "./components/Features/features";

const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </div>
      <Features />
      <Footer />
    </Router>
  );
};

export default App;
