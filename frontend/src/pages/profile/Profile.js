import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "./profile.css";

const Profile = () => {
  return (
    <div className="container mt-5">
      <h1 className="text-center text-primary mb-4">John Doe's Profile</h1>
      <div className="row">
        <div className="col-md-4">
          <div className="card text-center">
            <img
              src="https://randomuser.me/api/portraits/men/9.jpg"
              alt="John Doe"
              className="card-img-top rounded-circle mx-auto mt-3"
              style={{ width: "150px", height: "150px", objectFit: "cover" }}
            />
            <div className="card-body">
              <h5 className="card-title">John Doe</h5>
              <p className="card-text">Web Developer</p>
              <p className="card-text">
                <strong>Skills:</strong> HTML, CSS, JavaScript
              </p>
              <div className="d-grid gap-2">
                <button className="btn btn-primary ">Connect</button>
                <button className="btn btn-secondary">Message</button>
              </div>
            </div>
          </div>
        </div>
        <div className="col-md-8">
          <ul className="nav nav-tabs">
            <li className="nav-item">
              <a
                className="nav-link active"
                data-bs-toggle="tab"
                href="#profile"
              >
                Profile
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" data-bs-toggle="tab" href="#projects">
                Projects
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" data-bs-toggle="tab" href="#peers">
                Peers
              </a>
            </li>
          </ul>
          <div className="tab-content mt-3">
            <div className="tab-pane fade show active" id="profile">
              <h5>About John Doe</h5>
              <p>
                John is a skilled web developer with over 5 years of experience
                in HTML, CSS, and JavaScript. He has worked on numerous projects
                and is always eager to learn new technologies.
              </p>
            </div>
            <div className="tab-pane fade" id="projects">
              <p>Projects will be displayed here.</p>
            </div>
            <div className="tab-pane fade" id="peers">
              <p>Peers will be displayed here.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
