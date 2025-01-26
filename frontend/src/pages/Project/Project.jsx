import React, { useState } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./Project.css";

const ProjectCard = ({ project }) => (
  <div className="col-md-3 mb-4">
    <div className="card project-card shadow-sm h-100">
      <div className="card-body d-flex flex-column">
        <h5 className="font-weight-bold">{project.title}</h5>
        <p className="text-muted">{project.description}</p>
        <p>
          <strong>Technologies:</strong> {project.technologies.join(", ")}
        </p>
        <p>
          <strong>Schedule Date:</strong> {project.scheduleDate}
        </p>
        <p>
          <strong>Creator:</strong> {project.creator}
        </p>
        <p>
          <strong>Date Created:</strong> {project.dateCreated}
        </p>
        <button className="btn btn-primary mt-auto">Join</button>
      </div>
    </div>
  </div>
);

const Projects = () => {
  const projectsData = [
    {
      id: 1,
      title: "Project Alpha",
      description: "Description of Project Alpha",
      technologies: ["HTML", "CSS", "JavaScript"],
      scheduleDate: "2023-12-01",
      creator: "John Doe",
      dateCreated: "2023-01-15",
    },
    {
      id: 2,
      title: "Project Beta",
      description: "Description of Project Beta",
      technologies: ["Python", "Django"],
      scheduleDate: "2023-12-15",
      creator: "Jane Smith",
      dateCreated: "2023-02-01",
    },
    {
      id: 3,
      title: "Project Gamma",
      description: "Description of Project Gamma",
      technologies: ["React", "Node.js"],
      scheduleDate: "2023-12-20",
      creator: "Alice Johnson",
      dateCreated: "2023-03-10",
    },
    {
      id: 4,
      title: "Project Delta",
      description: "Description of Project Delta",
      technologies: ["Vue", "Firebase"],
      scheduleDate: "2024-01-05",
      creator: "Michael Brown",
      dateCreated: "2023-04-12",
    },
    {
      id: 5,
      title: "Project Epsilon",
      description: "Description of Project Epsilon",
      technologies: ["Angular", "TypeScript"],
      scheduleDate: "2024-01-10",
      creator: "Sarah Wilson",
      dateCreated: "2023-05-20",
    },
    {
      id: 6,
      title: "Project Zeta",
      description: "Description of Project Zeta",
      technologies: ["Ruby", "Rails"],
      scheduleDate: "2024-01-15",
      creator: "Chris Evans",
      dateCreated: "2023-06-25",
    },
    {
      id: 7,
      title: "Project Eta",
      description: "Description of Project Eta",
      technologies: ["Java", "Spring"],
      scheduleDate: "2024-01-20",
      creator: "Emma Watson",
      dateCreated: "2023-07-10",
    },
    {
      id: 8,
      title: "Project Theta",
      description: "Description of Project Theta",
      technologies: ["PHP", "Laravel"],
      scheduleDate: "2024-01-25",
      creator: "Daniel Craig",
      dateCreated: "2023-08-01",
    },
    {
      id: 9,
      title: "Project Iota",
      description: "Description of Project Iota",
      technologies: ["C#", ".NET"],
      scheduleDate: "2024-01-30",
      creator: "Olivia Benson",
      dateCreated: "2023-09-05",
    },
  ];

  const [searchQuery, setSearchQuery] = useState("");
  const [currentPage, setCurrentPage] = useState(1);

  const projectsPerPage = 4;

  const filteredProjects = projectsData.filter(
    (project) =>
      project.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      project.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
      project.technologies.some((tech) =>
        tech.toLowerCase().includes(searchQuery.toLowerCase())
      ) ||
      project.creator.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const totalPages = Math.ceil(filteredProjects.length / projectsPerPage);

  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const indexOfLastProject = currentPage * projectsPerPage;
  const indexOfFirstProject = indexOfLastProject - projectsPerPage;
  const currentProjects = filteredProjects.slice(
    indexOfFirstProject,
    indexOfLastProject
  );

  return (
    <div className="container mt-5">
      <div className="row mb-4">
        <div className="col-md-12 d-flex justify-content-between align-items-center">
          <Link to="/createProject">
            <button className="btn btn-primary">Create Project</button>
          </Link>
          <div className="input-group w-50">
            <input
              type="text"
              className="form-control"
              placeholder="Search projects"
              aria-label="Search projects"
              value={searchQuery}
              onChange={(e) => {
                setSearchQuery(e.target.value);
                setCurrentPage(1);
              }}
            />
            <div className="input-group-append">
              <span className="input-group-text">
                <i className="bi bi-search"></i>
              </span>
            </div>
          </div>
        </div>
      </div>
      <div className="row">
        {currentProjects.map((project) => (
          <ProjectCard key={project.id} project={project} />
        ))}
        {currentProjects.length === 0 && (
          <div className="col-md-12 text-center">
            <p className="text-muted">No projects found matching your query.</p>
          </div>
        )}
      </div>
      {filteredProjects.length > projectsPerPage && (
        <div className="row mt-4">
          <div className="col-md-12">
            <nav aria-label="Page navigation">
              <ul className="pagination justify-content-center">
                <li
                  className={`page-item ${currentPage === 1 ? "disabled" : ""}`}
                >
                  <button
                    className="page-link"
                    onClick={() => paginate(currentPage - 1)}
                  >
                    Previous
                  </button>
                </li>
                {[...Array(totalPages)].map((_, index) => (
                  <li
                    key={index + 1}
                    className={`page-item ${
                      currentPage === index + 1 ? "active" : ""
                    }`}
                  >
                    <button
                      className="page-link"
                      onClick={() => paginate(index + 1)}
                    >
                      {index + 1}
                    </button>
                  </li>
                ))}
                <li
                  className={`page-item ${
                    currentPage === totalPages ? "disabled" : ""
                  }`}
                >
                  <button
                    className="page-link"
                    onClick={() => paginate(currentPage + 1)}
                  >
                    Next
                  </button>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      )}
    </div>
  );
};

export default Projects;
