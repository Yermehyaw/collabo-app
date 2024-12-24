import React from "react";
import { FaSearch, FaUsers, FaRegSmileBeam, FaCogs } from "react-icons/fa";
import { Link } from "react-router-dom";
import "./Home.css"; // Custom styles for the landing page

const Home = () => {
  return (
    <div className="home-container">
      <div className="text-center">
        <h1>Welcome to Collabo</h1>
        <p>
          Your platform to connect and collaborate with professionals and
          enthusiasts
        </p>
      </div>

      <div className="features-section">
        <div className="feature-card">
          <FaSearch size={50} />
          <h3>Search Projects</h3>
          <p>
            Find the best projects to collaborate on with like-minded
            individuals.
          </p>
          <Link to="/projectdetails" className="btn btn-primary">
            Explore Projects
          </Link>
        </div>

        <div className="feature-card">
          <FaUsers size={50} />
          <h3>Meet New People</h3>
          <p>
            Connect with professionals, non-professionals, and people who share
            your interests.
          </p>
          <Link to="/profile" className="btn btn-primary">
            Meet People
          </Link>
        </div>

        <div className="feature-card">
          <FaRegSmileBeam size={50} />
          <h3>Positive Environment</h3>
          <p>
            Be a part of a vibrant community that fosters positivity and growth.
          </p>
          <Link to="/about" className="btn btn-primary">
            Learn More
          </Link>
        </div>

        <div className="feature-card">
          <FaCogs size={50} />
          <h3>Tools & Resources</h3>
          <p>
            Access a variety of tools and resources for personal and
            professional growth.
          </p>
          <Link to="/services" className="btn btn-primary">
            Check Tools
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
