import React, { useState } from "react";
import "./ProjectDetails.css";

const sampleProjects = [
  { id: 1, name: "Weather App", description: "A simple weather forecast app." },
  {
    id: 2,
    name: "Task Manager",
    description: "Manage your daily tasks efficiently.",
  },
  {
    id: 3,
    name: "Collabo App",
    description: "A social collaboration platform.",
  },
  {
    id: 4,
    name: "E-Commerce Site",
    description: "A fully functional online store.",
  },
  {
    id: 5,
    name: "Portfolio Website",
    description: "Showcase your projects and skills.",
  },
];

const ProjectPage = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [projects, setProjects] = useState(sampleProjects);

  const handleSearch = (e) => {
    e.preventDefault();
    const filteredProjects = sampleProjects.filter((project) =>
      project.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setProjects(filteredProjects);
  };

  return (
    <div className="container project-page mt-5 mb-5">
      <div className="project-header d-flex justify-content-between align-items-center">
        <h1>Projects</h1>
        <div>
          <form onSubmit={handleSearch} className=" search-bar d-flex">
            <input
              type="text"
              placeholder="Search for projects..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <button type="submit">Search</button>
          </form>
        </div>
      </div>

      <div className="project-list">
        {projects.length > 0 ? (
          projects.map((project) => (
            <div key={project.id} className="project-card">
              <h3>{project.name}</h3>
              <p>{project.description}</p>
            </div>
          ))
        ) : (
          <p className="no-projects">No projects found.</p>
        )}
      </div>
    </div>
  );
};

export default ProjectPage;
