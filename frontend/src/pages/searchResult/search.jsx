import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import { Link } from "react-router-dom";

const App = () => {
  const projects = [
    {
      id: 1,
      name: "Project Alpha",
      description: "Description of Project Alpha",
      technologies: "HTML, CSS, JavaScript",
      scheduleDate: "2023-12-01",
      peers: [
        "https://randomuser.me/api/portraits/men/1.jpg",
        "https://randomuser.me/api/portraits/women/2.jpg",
        "https://randomuser.me/api/portraits/men/3.jpg",
      ],
    },
    {
      id: 2,
      name: "Project Beta",
      description: "Description of Project Beta",
      technologies: "Python, Django",
      scheduleDate: "2023-12-15",
      peers: [
        "https://randomuser.me/api/portraits/men/4.jpg",
        "https://randomuser.me/api/portraits/women/5.jpg",
        "https://randomuser.me/api/portraits/men/6.jpg",
      ],
    },
    {
      id: 3,
      name: "Project Gamma",
      description: "Description of Project Gamma",
      technologies: "Java, Spring Boot",
      scheduleDate: "2023-12-20",
      peers: [
        "https://randomuser.me/api/portraits/men/7.jpg",
        "https://randomuser.me/api/portraits/women/8.jpg",
        "https://randomuser.me/api/portraits/men/9.jpg",
      ],
    },
  ];

  const peers = [
    {
      id: 1,
      name: "John Doe",
      title: "Web Developer",
      skills: "HTML, CSS, JavaScript",
      avatar: "https://randomuser.me/api/portraits/men/1.jpg",
    },
    {
      id: 2,
      name: "Jane Smith",
      title: "Graphic Designer",
      skills: "Photoshop, Illustrator, InDesign",
      avatar: "https://randomuser.me/api/portraits/women/2.jpg",
    },
    {
      id: 3,
      name: "Alice Johnson",
      title: "Project Manager",
      skills: "Agile, Scrum, Leadership",
      avatar: "https://randomuser.me/api/portraits/women/3.jpg",
    },
    // Add additional peers as needed...
  ];

  return (
    <div className="bg-light">
      <div className="container mt-5">
        {/* Header Section */}
        <div className="row mb-4">
          <div className="col-md-12 d-flex justify-content-between align-items-center">
            <h1 className="text-center">Search Results</h1>
            <div className="input-group w-50">
              <input
                type="text"
                className="form-control"
                placeholder="Search projects and peers"
                aria-label="Search projects and peers"
              />
              <div className="input-group-append">
                <button className="btn btn-outline-secondary" type="button">
                  <i className="fa fa-search"></i>
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Projects Section */}
        <div className="row">
          <div className="col-12">
            <h2 className="text-primary">Results for Projects</h2>
          </div>
          {projects.map((project) => (
            <div className="col-md-4" key={project.id}>
              <div className="project-card">
                <h5 className="font-weight-bold">{project.name}</h5>
                <p className="text-muted">{project.description}</p>
                <p>
                  <strong>Technologies:</strong> {project.technologies}
                </p>
                <p>
                  <strong>Schedule Date:</strong> {project.scheduleDate}
                </p>
                <p>
                  <strong>Peers:</strong>
                  {project.peers.map((peer, index) => (
                    <img
                      key={index}
                      src={peer}
                      alt="Avatar"
                      className="project-avatar"
                    />
                  ))}
                  <span className="more-peers">...</span>
                </p>
              </div>
            </div>
          ))}
        </div>

        {/* Peers Section */}
        <div className="row">
          <div className="col-12">
            <h2 className="text-primary">Results for Peers</h2>
          </div>
          {peers.map((peer) => (
            <div className="col-md-4 mb-4" key={peer.id}>
              <div className="card peer-card text-center">
                <div className="card-body">
                  <img src={peer.avatar} className="peer-avatar" alt="Avatar" />
                  <h5 className="card-title">{peer.name}</h5>
                  <p className="card-text">{peer.title}</p>
                  <p className="card-text">
                    <strong>Skills:</strong> {peer.skills}
                  </p>
                  <button className="btn btn-primary">Connect</button>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Pagination */}
        <div className="row mt-4">
          <div className="col-md-12">
            <nav aria-label="Page navigation">
              <ul className="pagination justify-content-center">
                <li className="page-item">
                  <Link className="page-link" to="#">
                    Previous
                  </Link>
                </li>
                <li className="page-item">
                  <Link className="page-link" to="#">
                    1
                  </Link>
                </li>
                <li className="page-item">
                  <Link className="page-link" to="#">
                    2
                  </Link>
                </li>
                <li className="page-item">
                  <Link className="page-link" to="#">
                    3
                  </Link>
                </li>
                <li className="page-item">
                  <Link className="page-link" to="#">
                    Next
                  </Link>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
