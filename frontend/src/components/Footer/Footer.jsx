import React from "react";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="bg-light text-center py-4 mt-5">
      <div className="container">
        <p className="mb-0 text-muted">
          Connect, Collaborate, and Create with Collabo!
        </p>
        <div className="social-icons mt-3">
          <Link to="#" className="text-muted mx-2">
            <i className="bi bi-facebook"></i>
          </Link>
          <Link to="#" className="text-muted mx-2">
            <i className="bi bi-twitter"></i>
          </Link>
          <Link to="#" className="text-muted mx-2">
            <i className="bi bi-linkedin"></i>
          </Link>
          <Link to="#" className="text-muted mx-2">
            <i className="bi bi-instagram"></i>
          </Link>
        </div>
        <p className="mt-4 text-muted">© 2025 Collabo. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
