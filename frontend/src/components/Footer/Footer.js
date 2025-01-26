import React from "react";
import "bootstrap-icons/font/bootstrap-icons.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Link } from "react-router-dom";
import "./Footer.css";

const Footer = () => {
  return (
    <footer className="footer bg-dark text-light pt-5">
      <div className="container">
        <div className="row">
          {/* About Us */}
          <div className="col-md-4 mb-4">
            <h5 className="fw-bold">About Us</h5>
            <p>
              Collabo is a social platform designed to connect professionals and
              enthusiasts from all walks of life. Discover like-minded
              individuals, share ideas, and create meaningful collaborations.
            </p>
          </div>

          {/* Contact Address */}
          <div className="col-md-4 mb-4">
            <h5 className="fw-bold">Contact Us</h5>
            <address>
              <p>123 Rhine Street, Abuja, Nigeria</p>
              <p>Email: support@collabo.com</p>
              <p>Phone: +234 7061251386</p>
            </address>
          </div>

          {/* Feedback Form */}
          <div className="col-md-4 mb-4">
            <h5 className="fw-bold">Feedback</h5>
            <form>
              <div className="mb-3">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Your Name"
                  required
                />
              </div>
              <div className="mb-3">
                <input
                  type="email"
                  className="form-control"
                  placeholder="Your Email"
                  required
                />
              </div>
              <div className="mb-3">
                <textarea
                  className="form-control"
                  rows="3"
                  placeholder="Your Feedback"
                  required
                ></textarea>
              </div>
              <button type="submit" className="btn w-100">
                Submit
              </button>
            </form>
          </div>
        </div>

        <div className="row">
          {/* Join Today Section */}
          <div className="col-md-6 mb-4">
            <h5 className="fw-bold">Are You New to Collabo?</h5>
            <p>
              Join today and start collaborating with amazing people around the
              globe!
            </p>
            <form>
              <div className="mb-3">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Your Name"
                  required
                />
              </div>
              <div className="mb-3">
                <input
                  type="email"
                  className="form-control"
                  placeholder="Your Email"
                  required
                />
              </div>
              <div className="mb-3">
                <input
                  type="password"
                  className="form-control"
                  placeholder="Create Password"
                  required
                />
              </div>
              <button type="submit" className="btn w-100">
                Sign Up
              </button>
            </form>
          </div>

          {/* Social Media Links */}
          <div className="col-md-6 mb-4">
            <h5 className="fw-bold">Follow Us</h5>
            <p>Stay connected and get the latest updates:</p>
            <div className="d-flex gap-3">
              <Link to="#" className="text-light fs-5">
                <i className="bi bi-facebook"></i>
              </Link>
              <Link to="#" className="text-light fs-5">
                <i className="bi bi-twitter"></i>
              </Link>
              <Link to="#" className="text-light fs-5">
                <i className="bi bi-instagram"></i>
              </Link>
              <Link to="#" className="text-light fs-5">
                <i className="bi bi-linkedin"></i>
              </Link>
            </div>
          </div>
        </div>

        <hr className="text-light" />
        <div className="text-center py-3">
          <p className="mb-0">&copy; 2025 Collabo. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
