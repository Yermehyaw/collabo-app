import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import {
  FaUsers,
  FaTools,
  FaGraduationCap,
  FaHandshake,
  FaChartLine,
} from "react-icons/fa"; // Icons
import "./features.css";

const Features = () => {
  const people = [
    {
      name: "Akor Jerimiah",
      profession: "Project Manager",
      image: "https://via.placeholder.com/150", // Placeholder for user image
    },
    {
      name: "Eyakeno Umana",
      profession: "Backend Developer",
      image: "https://via.placeholder.com/150", // Placeholder for user image
    },
    {
      name: "Asmiyen",
      profession: "UX/UI Designer",
      image: "https://via.placeholder.com/150", // Placeholder for user image
    },
    {
      name: "Whilz Abel",
      profession: "Frontend Developer",
      image: "https://via.placeholder.com/150", // Placeholder for user image
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
            individuals. Whether you're a professional seeking to expand your
            network, a creative mind looking for inspiration, or simply someone
            eager to meet new friends, Collabo makes it happen. Collaborate
            seamlessly on projects, share innovative ideas, and grow your skills
            with others who share your passions. Empower your creativity, build
            lasting connections, and discover endless possibilities with
            Collabo. Join today and experience a world where collaboration meets
            innovation!
          </p>
        </div>

        {/* Features Grid */}
        <div className="row mb-5">
          <div className="col-md-4">
            <div className="feature-card card shadow-sm border-0 p-4 text-center">
              <div className="icon mb-3 text-primary">
                <FaUsers />
              </div>
              <h5 className="fw-bold">Connect with Peers</h5>
              <p className="text-muted">
                Find like-minded individuals to collaborate with and grow
                together.
              </p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="feature-card card shadow-sm border-0 p-4 text-center">
              <div className="icon mb-3 text-success">
                <FaTools />
              </div>
              <h5 className="fw-bold">Collaborative Tools</h5>
              <p className="text-muted">
                Use our modern tools to manage projects, communicate, and
                succeed.
              </p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="feature-card card shadow-sm border-0 p-4 text-center">
              <div className="icon mb-3 text-warning">
                <FaGraduationCap />
              </div>
              <h5 className="fw-bold">Professional Growth</h5>
              <p className="text-muted">
                Take your skills to the next level by learning and sharing with
                others.
              </p>
            </div>
          </div>
        </div>

        {/* Services Section */}
        <div className="row mb-5">
          <div className="col-md-6">
            <div className="service-card card shadow-sm border-0 p-4 text-center">
              <div className="icon mb-3 text-info">
                <FaHandshake />
              </div>
              <h5 className="fw-bold">Trusted Partnerships</h5>
              <p className="text-muted">
                Build strong, lasting relationships through trust and
                collaboration.
              </p>
            </div>
          </div>
          <div className="col-md-6">
            <div className="service-card card shadow-sm border-0 p-4 text-center">
              <div className="icon mb-3 text-danger">
                <FaChartLine />
              </div>
              <h5 className="fw-bold">Result-Oriented Solutions</h5>
              <p className="text-muted">
                Achieve measurable success through efficient teamwork and tools.
              </p>
            </div>
          </div>
        </div>

        {/* People Cards */}
        <div className="text-center mb-4">
          <h3 className="fw-bold">Meet Our Community</h3>
          <p className="text-muted">
            Join a growing network of amazing people.
          </p>
        </div>
        <div className="row justify-content-center">
          {people.map((person, index) => (
            <div className="col-md-4 col-sm-6 mb-4" key={index}>
              <div className="card shadow-sm border-0 text-center p-4">
                <img
                  src={person.image}
                  alt={person.name}
                  className="rounded-circle mx-auto mb-3"
                  width="100"
                  height="100"
                />
                <h5 className="fw-bold">{person.name}</h5>
                <p className="text-muted">{person.profession}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
