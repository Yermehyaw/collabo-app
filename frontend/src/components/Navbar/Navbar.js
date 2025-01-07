import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css"; // Bootstrap styles
import {
  FaSearch,
  FaBars,
  FaHome,
  FaSignInAlt,
  FaUser,
  FaProjectDiagram,
} from "react-icons/fa"; // Icons
import logo from "./logo.png";
import "./Navbar.css"; // Navbar styles
import "./Sidebar.css"; // Sidebar styles
import MessagingApp from "../MessagingApp/MessagingApp";

const Navbar = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isSearchVisible, setIsSearchVisible] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const navigate = useNavigate();

  // Searchable sections and keywords
  const searchableSections = [
    { name: "Home", path: "/home", keywords: ["welcome", "start", "home"] },
    { name: "About", path: "/#about", keywords: ["team", "about", "mission"] },
    { name: "Services", path: "/#services", keywords: ["offer", "services"] },
    { name: "Contact Us", path: "/#contact", keywords: ["contact", "help"] },
    {
      name: "Login/Signup",
      path: "/login",
      keywords: ["login", "signup", "auth"],
    },
    { name: "Profile", path: "/profile", keywords: ["profile", "user"] },
    {
      name: "Project Details",
      path: "/projectdetails",
      keywords: ["project", "details", "dog"],
    },
  ];

  // Toggle Sidebar
  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  // Toggle Search Bar
  const toggleSearch = () => {
    setIsSearchVisible(!isSearchVisible);
    setSearchQuery("");
    setSearchResults([]);
  };

  // Handle Search Query
  const handleSearch = (e) => {
    const query = e.target.value.toLowerCase();
    setSearchQuery(query);

    // Filter matches based on query
    if (query) {
      const results = searchableSections.filter((section) =>
        section.keywords.some((keyword) => keyword.includes(query))
      );
      setSearchResults(results);
    } else {
      setSearchResults([]);
    }
  };

  const performSearch = () => {
    if (!searchQuery) {
      return; // If there's no search query, do nothing
    }

    const results = searchableSections.filter((section) =>
      section.name.toLowerCase().includes(searchQuery.toLowerCase())
    );

    setSearchResults(results);
  };

  // Navigate to the selected section
  const handleResultClick = (path) => {
    navigate(path);
    setSearchQuery("");
    setSearchResults([]);
  };

  const [isChatVisible, setIsChatVisible] = useState(false);
  const [hasNewMessages, setHasNewMessages] = useState(true); // Indicates new messages

  // Toggle chat visibility
  const toggleChat = () => {
    setIsChatVisible(!isChatVisible);
    setHasNewMessages(false); // Mark messages as read when chat is opened
  };

  return (
    <>
      {/* Navbar */}
      <nav className="navbar navbar-expand-lg navbar-light  fixed-top">
        <div id="nav-bar" className="container-fluid d-flex align-items-center">
          {/* Hamburger Icon */}
          <button
            id="sidebar-toggle"
            className="navbar-toggler"
            type="button"
            onClick={toggleSidebar}
            aria-label="Toggle navigation"
          >
            <FaBars size={20} />
          </button>

          {/* Logo */}
          <Link id="logo" className="navbar-brand ms-2" to="/">
            <img src={logo} alt="Collabo Logo" width="80" height="80" />
          </Link>

          <div className="collapse navbar-collapse justify-content-center d-none d-lg-flex">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link to="/" className="nav-link">
                  Home
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/#About" className="nav-link">
                  About
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/#services" className="nav-link">
                  Services
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/contact" className="nav-link">
                  Contact Us
                </Link>
              </li>
            </ul>
          </div>

          {/* Right Side Search & Login */}
          <div className="d-flex align-items-center">
            {/* Search Icon */}
            <FaSearch
              className="search-icon"
              size={24}
              onClick={toggleSearch}
              style={{ cursor: "pointer" }}
            />

            {/* Search Bar */}
            {isSearchVisible && (
              <div className="search-bar ms-3 d-flex align-items-center">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Search"
                  autoFocus
                  value={searchQuery}
                  onChange={handleSearch}
                />
                <button
                  className="btn btn-primary ms-2"
                  onClick={performSearch} // This is the search trigger
                >
                  Go
                </button>
                {/* Search Results */}
                {searchResults.length > 0 && (
                  <div className="search-results">
                    <h6>Results (matches: {searchResults.length})</h6>
                    <ul>
                      {searchResults.map((result, index) => (
                        <li
                          key={index}
                          onClick={() => handleResultClick(result.path)}
                          className="search-result-item"
                        >
                          {result.name}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            )}

            <div className="chat-icon-container" onClick={toggleChat}>
              <i className="fa fa-comments chat-icon"></i>
              {hasNewMessages && <span className="red-dot"></span>}
            </div>

            <Link
              to="/login"
              className="btn btn-outline-primary ms-3"
              id="signup"
            >
              Sign Up
            </Link>
          </div>
        </div>
      </nav>

      {/* Sidebar */}
      <div
        className={`sidebar ${isSidebarOpen ? "open" : ""}`}
        onClick={(e) => e.stopPropagation()} // Prevent closing sidebar when clicked inside
      >
        {/* Sidebar Header */}
        <div
          id="sidebar_header"
          className="sidebar-header d-flex justify-content-between align-items-center"
        >
          <button id="close-btn" onClick={toggleSidebar}>
            X
          </button>
          <img src={logo} alt="Collabo Logo" width="80" height="80" />
        </div>

        {/* Sidebar Content */}
        <ul className="list-unstyled">
          <li>
            <Link to="/" onClick={toggleSidebar}>
              <FaHome className="me-2" />
              Home
            </Link>
          </li>
          <li>
            <Link to="/login" onClick={toggleSidebar}>
              <FaSignInAlt className="me-2" />
              Login/Signup
            </Link>
          </li>
          <li>
            <Link to="/profile" onClick={toggleSidebar}>
              <FaUser className="me-2" />
              Profile
            </Link>
          </li>
          <li>
            <Link to="/projectdetails" onClick={toggleSidebar}>
              <FaProjectDiagram className="me-2" />
              Project Details
            </Link>
          </li>
          <li>
            <a href="#about" onClick={toggleSidebar}>
              About
            </a>
          </li>
          <li>
            <a href="#services" onClick={toggleSidebar}>
              Services
            </a>
          </li>
          <li>
            <a href="#contact" onClick={toggleSidebar}>
              Contact Us
            </a>
          </li>
        </ul>
      </div>

      {/* Overlay for Sidebar */}
      {isSidebarOpen && (
        <div className="sidebar-overlay" onClick={toggleSidebar}></div>
      )}
      {isChatVisible && <MessagingApp />}
    </>
  );
};

export default Navbar;
