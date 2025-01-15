import React from "react";
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
import Footer from "./components/Footer/Footer.jsx";

const App = () => {
  const isAuthenticated = !!localStorage.getItem("token"); // Check if user is authenticated

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<HeroSection />} /> {/* Home page */}
        <Route
          path="/profile"
          element={isAuthenticated ? <Profile /> : <Navigate to="/Login" />}
        />{" "}
        <Route path="/login" element={<Login />} /> {/* Login page */}
        <Route path="/signup" element={<SignUp />} /> {/* Sign up page */}
        <Route path="/peers" element={<Peers />} /> {/* Peers page */}
        <Route path="/projects" element={<Projects />} /> {/* Projects page */}
        {/* Add more routes here for other pages */}
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;
