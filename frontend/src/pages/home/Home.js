import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import TypingEffect from "react-typing-effect"; // Import the typing effect component
import "./Home.css";
import { Link } from "react-router-dom";
import Features from "../../components/Features/features";

const Home = () => {
  return (
    <main>
      {/* Hero Section */}
      <section id="hero">
        <div className="hero-content">
          <div className="hero-image"></div>
          <h1 id="logo-name">COLLABO</h1>
          <p id="welcome">
            Welcome to Collabo — where connections spark creativity! Meet
            like-minded individuals, collaborate on projects, and grow together.
            Join today and turn ideas into reality!
          </p>
          <h2>
            <TypingEffect
              text={[
                "CONNECT",
                "MEET NEW FRIENDS",
                "CREATE PROJECTS",
                "COLLABORATE",
                "GROW",
              ]}
              speed={200}
              eraseDelay={1500}
              typingDelay={500}
            />
          </h2>{" "}
          <div className="hero-buttons">
            <Link to="/login">
              <button className="btn primary">Get Started</button>
            </Link>
            <button className="btn secondary">Learn More</button>
          </div>
        </div>
      </section>

      <Features />
    </main>
  );
};
export default Home;
