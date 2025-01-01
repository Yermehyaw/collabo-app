import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import TypingEffect from "react-typing-effect"; // Import the typing effect component

import "./Home.css";

const Home = () => {
  return (
    <main>
      {/* Hero Section */}
      <section id="hero">
        <div className="hero-content">
          <h1 id="logo-name">COLLABO</h1>
          <p id="welcome">
            Welcome to Collabo — where connections spark creativity! Meet
            like-minded individuals, collaborate on projects, and grow together.
            Join today and turn ideas into reality!
          </p>
          <h2>
            <TypingEffect
              text={[
                "CREATE PROJECTS",
                "MEET NEW FRIENDS",
                "CONNECT",
                "COLLABORATE",
                "GROW",
              ]}
              speed={100}
              eraseDelay={1500}
              typingDelay={500}
            />
          </h2>{" "}
          <div className="hero-buttons">
            <button className="btn primary">Try Now</button>
            <button className="btn secondary">Contact Us</button>
          </div>
        </div>
      </section>
    </main>
  );
};
export default Home;
