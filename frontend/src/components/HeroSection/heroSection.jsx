import React from "react";
import { ArrowRight } from "lucide-react";
import "./heroSection.css";
import { Link } from "react-router-dom";

const HeroSection = ({
  headline = "Transform Your Team Collaboration",
  subheading = "Empower your team with our intuitive collaboration platform. Get more done together, faster and smarter.",
  ctaText = "Get Started",
  onCtaClick = () => console.log("CTA clicked"),
}) => {
  return (
    <>
      {/* Hero Section */}
      <section
        id="HeroSection"
        className="min-vh-100 d-flex justify-content-center align-items-center px-4"
      >
        <div className="text-center space-y-3 animate__animated animate__fadeIn">
          <h1 className="display-2 font-weight-bolder text-white">
            {headline}
          </h1>
          <p className="lead text-light">{subheading}</p>
          <div className="pt-4">
            <Link to="/login">
              <button
                onClick={onCtaClick}
                className="btn btn-primary btn-lg d-flex align-items-center justify-content-center"
              >
                {ctaText}
                <ArrowRight className="ml-2 h-4 w-4" />
              </button>
            </Link>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="about-section">
        <div className="container">
          <h2 className="section-title">
            About <span>Collabo</span>
          </h2>
          <p className="section-subtitle">
            Meet. Collaborate. Achieve. <br />
            Bringing like-minded individuals together to build something
            amazing.
          </p>
          <div className="features">
            <div className="feature">
              <i
                className="bi bi-people-fill feature-icon"
                style={{ color: "blue" }}
              ></i>
              <h3>Find Your Tribe</h3>
              <p>
                Connect with professionals and peers who share your passion and
                interests.
              </p>
            </div>
            <div className="feature">
              <i
                className="bi bi-lightbulb-fill feature-icon "
                style={{ color: "Yellow" }}
              ></i>
              <h3>Innovate Together</h3>
              <p>
                Collaborate on groundbreaking projects with others who share
                your vision.
              </p>
            </div>
            <div className="feature">
              <i
                className="bi bi-chat-dots-fill feature-icon"
                style={{ color: "green" }}
              ></i>
              <h3>Seamless Communication</h3>
              <p>
                Stay connected with an intuitive messaging system for smooth
                teamwork.
              </p>
            </div>
            <div className="feature">
              <i
                className="bi bi-award-fill feature-icon"
                style={{ color: "red" }}
              ></i>
              <h3>Achieve Goals</h3>
              <p>
                Turn your ideas into reality with the power of collaboration and
                shared knowledge.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Our Services Section */}
      <section className="services-section py-5 bg-light">
        <div className="container">
          <h2 className="section-title text-center mb-4">
            Our <span>Services</span>
          </h2>
          <p className="section-subtitle text-center mb-5">
            Explore our range of services designed to enhance your collaborative
            experience and help you succeed.
          </p>
          <div className="row">
            <div className="col-md-4 text-center">
              <i
                className="bi bi-gear-fill service-icon mb-3"
                style={{ color: "#007bff", fontSize: "2rem" }}
              ></i>
              <h3>Project Management</h3>
              <p>
                Simplify project tracking and ensure your team stays on target
                with clear goals and milestones.
              </p>
            </div>
            <div className="col-md-4 text-center">
              <i
                className="bi bi-graph-up-arrow service-icon mb-3"
                style={{ color: "#28a745", fontSize: "2rem" }}
              ></i>
              <h3>Performance Insights</h3>
              <p>
                Gain valuable insights into team performance and identify
                opportunities for growth.
              </p>
            </div>
            <div className="col-md-4 text-center">
              <i
                className="bi bi-cloud-upload-fill service-icon mb-3"
                style={{ color: "#ffc107", fontSize: "2rem" }}
              ></i>
              <h3>Cloud Integration</h3>
              <p>
                Access your data securely from anywhere, anytime, with our
                cloud-based solutions.
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default HeroSection;
