import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
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
      profession: "ux/ui Designer",
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
        <div className="text-center mb-5">
          <h2 className="fw-bold">Why Choose Collabo?</h2>
          <p className="text-muted">
            Collabo connects people, fosters collaboration, and empowers
            creativity.
          </p>
        </div>

        {/* Features Grid */}
        <div className="row mb-5">
          <div className="col-md-4">
            <div className="card shadow-sm border-0 p-4">
              <h5 className="fw-bold">Connect with Peers</h5>
              <p className="text-muted">
                Find like-minded individuals to collaborate with and grow
                together.
              </p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card shadow-sm border-0 p-4">
              <h5 className="fw-bold">Collaborative Tools</h5>
              <p className="text-muted">
                Use our modern tools to manage projects, communicate, and
                succeed.
              </p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card shadow-sm border-0 p-4">
              <h5 className="fw-bold">Professional Growth</h5>
              <p className="text-muted">
                Take your skills to the next level by learning and sharing with
                others.
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
