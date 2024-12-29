import React from "react";
import { FaSearch, FaUsers, FaRegSmileBeam, FaCogs } from "react-icons/fa";

import "bootstrap/dist/css/bootstrap.min.css";
import "./Home.css";

const Home = () => {
  return (
    <main>
      {/* Hero Section */}
      <section id="hero">
        <div>
          <h1>Collaborate & Grow</h1>
          <p>
            Connect with like-minded individuals and work on projects that
            matter. Join a vibrant community and start building your future
            today.
          </p>
          <button className="btn">Get Started</button>
        </div>
      </section>

      {/* Features Section */}
      <section className="features-section">
        <div className="feature-card">
          <FaSearch size={50} />
          <h3>Search Projects</h3>
          <p>
            Find the best projects to collaborate on with like-minded
            individuals.
          </p>
        </div>

        <div className="feature-card">
          <FaUsers size={50} />
          <h3>Meet New People</h3>
          <p>
            Connect with professionals, non-professionals, and people who share
            your interests.
          </p>
        </div>

        <div className="feature-card">
          <FaRegSmileBeam size={50} />
          <h3>Positive Environment</h3>
          <p>
            Be a part of a vibrant community that fosters positivity and growth.
          </p>
        </div>

        <div className="feature-card">
          <FaCogs size={50} />
          <h3>Tools & Resources</h3>
          <p>
            Access a variety of tools and resources for personal and
            professional growth.
          </p>
        </div>
      </section>

      {/* About Section */}
      <section className="about-section">
        <div>
          <h2>About Us</h2>
          <p>
            At Collabo, we believe in the power of collaboration. Our mission is
            to create a platform that connects people from diverse backgrounds,
            enabling them to share ideas, skills, and resources to achieve their
            goals.
          </p>
        </div>
        <img src="https://via.placeholder.com/400x300" alt="About Collabo" />
      </section>

      {/* Services Section */}
      <section className="services-section">
        <h2>Our Services</h2>
        <div className="service-card">
          <h3>Project Management</h3>
          <p>Streamline your projects with our easy-to-use management tools.</p>
        </div>
        <div className="service-card">
          <h3>Networking</h3>
          <p>Meet and connect with like-minded individuals in your field.</p>
        </div>
        <div className="service-card">
          <h3>Resource Sharing</h3>
          <p>Access a wide range of resources to enhance your productivity.</p>
        </div>
      </section>

      {/* Call-to-Action Section */}
      <section className="cta-section">
        <h2>Ready to Start Collaborating?</h2>
        <button className="btn">Join Now</button>
      </section>
    </main>
  );
};

export default Home;
