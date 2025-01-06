import React from "react";
import Navbar from "../Navbar/Navbar"; // Your Navbar component
import Footer from "../Footer/Footer"; // Your Footer component
import { Outlet, useLocation } from "react-router-dom"; // Import useLocation

const Layout = () => {
  const location = useLocation(); // Get the current location

  // Define paths where the Navbar should not appear
  const hideNavbarPaths = ["/login"];

  return (
    <div>
      {/* Conditionally render the Navbar */}
      {!hideNavbarPaths.includes(location.pathname) && <Navbar />}
      <div className="main-content">
        <Outlet /> {/* This is where page-specific content will be rendered */}
      </div>
      <Footer /> {/* Footer will still be visible on all pages */}
    </div>
  );
};

export default Layout;
