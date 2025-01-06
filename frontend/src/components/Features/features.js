import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import {
  FaUsers,
  FaTools,
  FaGraduationCap,
  FaHandshake,
  FaChartLine,
  FaLightbulb,
} from "react-icons/fa"; // Icons for feature cards
import "./features.css";

const Features = () => {
  const featureCards = [
    {
      icon: <FaUsers className="icon text-primary" />,
      title: "Connect with Peers",
      description:
        "Find like-minded individuals to collaborate with and grow together.",
    },
    {
      icon: <FaTools className="icon text-success" />,
      title: "Collaborative Tools",
      description:
        "Use our modern tools to manage projects, communicate, and succeed.",
    },
    {
      icon: <FaGraduationCap className="icon text-warning" />,
      title: "Professional Growth",
      description:
        "Take your skills to the next level by learning and sharing with others.",
    },
    {
      icon: <FaHandshake className="icon text-info" />,
      title: "Trusted Partnerships",
      description:
        "Build strong, lasting relationships through trust and collaboration.",
    },
    {
      icon: <FaChartLine className="icon text-danger" />,
      title: "Result-Oriented Solutions",
      description:
        "Achieve measurable success through efficient teamwork and tools.",
    },
    {
      icon: <FaLightbulb className="icon text-secondary" />,
      title: "Innovative Ideas",
      description:
        "Bring your creativity to life by sharing ideas and collaborating with others.",
    },
  ];

  const peopleCards = [
    {
      name: "John Doe",
      title: "Team Leader",
      image: "https://via.placeholder.com/150",
      quote:
        "Collabo transformed the way I work. It's the best platform for collaboration and teamwork!",
    },
    {
      name: "Jane Smith",
      title: "Product Manager",
      image: "https://via.placeholder.com/150",
      quote:
        "With Collabo, I was able to find amazing collaborators and build something truly special.",
    },
    {
      name: "Samuel Green",
      title: "Creative Designer",
      image: "https://via.placeholder.com/150",
      quote:
        "The tools and connections I've made on Collabo have been nothing short of amazing!",
    },

    {
      name: "Emily White",
      title: "Marketing Specialist",
      image: "https://via.placeholder.com/150",
      quote:
        "Collabo has helped me grow my skills, connect with others, and achieve great results!",
    },
  ];

  return (
    <section className="features py-5">
      <div className="container">
        {/* Features Intro */}
        <div className="text-center mb-5" id="choose">
          <h2 className="fw-bold">Why Choose Collabo?</h2>
          <p className="text">
            Collabo is your ultimate platform for connecting with like-minded
            individuals. Collaborate seamlessly on projects, share innovative
            ideas, and grow your skills with others who share your passions.
            Empower your creativity, build lasting connections, and discover
            endless possibilities with Collabo!
          </p>
        </div>

        {/* Features Grid */}
        <div className="row g-4">
          {featureCards.map((card, index) => (
            <div className="col-lg-4 col-md-6" key={index}>
              <div className="feature-card card shadow-sm border-0 p-4 text-center">
                <div className="mb-3">{card.icon}</div>
                <h5 className="fw-bold">{card.title}</h5>
                <p className="text-muted">{card.description}</p>
              </div>
            </div>
          ))}
        </div>

        {/* People Section */}
        <div className="people-section text-center">
          <h3 className="fw-bold mb-4">What People Are Saying</h3>
          <div className="row g-1">
            {peopleCards.map((person, index) => (
              <div className="col-lg-4 col-md-4" key={index}>
                <div className="people-card card shadow-sm border-0 p-4">
                  <img
                    src={person.image}
                    alt={person.name}
                    className="rounded-circle mb-3"
                    style={{
                      width: "80px",
                      height: "80px",
                      objectFit: "cover",
                    }}
                  />
                  <h5 className="fw-bold">{person.name}</h5>
                  <p className="text-muted">{person.title}</p>
                  <p className="quote">"{person.quote}"</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Features;
