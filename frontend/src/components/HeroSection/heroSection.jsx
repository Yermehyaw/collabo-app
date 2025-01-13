import React from "react";
import { ArrowRight } from "lucide-react";
import "./heroSection.css";
import { Link } from "react-router-dom";

const heroSection = ({
  headline = "Transform Your Team Collaboration",
  subheading = "Empower your team with our intuitive collaboration platform. Get more done together, faster and smarter.",
  ctaText = "Get Started",
  onCtaClick = () => console.log("CTA clicked"),
}) => {
  return (
    <section
      id="HeroSection"
      className="min-vh-100 d-flex justify-content-center align-items-center  px-4"
    >
      <div className="text-center space-y-3 animate__animated animate__fadeIn">
        <h1 className="display-2 font-weight-bolder text-white">{headline}</h1>
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
  );
};

export default heroSection;
