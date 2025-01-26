import React, { useState } from 'react';
import './Projects.css';
import ProjectCard from './components/ProjectCard';
import PeersModal from './components/PeersModal';

const Projects = () => {
  const [selectedProject, setSelectedProject] = useState(null);
  
  const projects = [
    {
      id: 1,
      name: "Project Alpha",
      description: "Description of Project Alpha",
      technologies: "HTML, CSS, JavaScript",
      scheduleDate: "2023-12-01",
      peers: [
        { id: 1, avatar: "/api/placeholder/30/30" },
        { id: 2, avatar: "/api/placeholder/30/30" },
        { id: 3, avatar: "/api/placeholder/30/30" },
        { id: 4, avatar: "/api/placeholder/30/30" }
      ]
    },
    {
      id: 2,
      name: "Project Beta",
      description: "Description of Project Beta",
      technologies: "Python, Django",
      scheduleDate: "2023-12-15",
      peers: [
        { id: 5, avatar: "/api/placeholder/30/30" },
        { id: 6, avatar: "/api/placeholder/30/30" },
        { id: 7, avatar: "/api/placeholder/30/30" },
        { id: 8, avatar: "/api/placeholder/30/30" }
      ]
    }
  ];

  return (
    <div className="projects-container">
      <div className="header">
        <button className="create-button">Create Project</button>
        <div className="search-wrapper">
          <input
            type="text"
            className="search-input"
            placeholder="Search projects"
          />
          <button className="search-button">
            🔍
          </button>
        </div>
      </div>

      <div className="projects-grid">
        {projects.map(project => (
          <ProjectCard 
            key={project.id} 
            project={project}
            onPeersClick={() => setSelectedProject(project)}
          />
        ))}
      </div>

      <div className="pagination">
        <button>Previous</button>
        <button className="active">1</button>
        <button>2</button>
        <button>3</button>
        <button>Next</button>
      </div>

      {selectedProject && (
        <PeersModal 
          project={selectedProject}
          onClose={() => setSelectedProject(null)}
        />
      )}
    </div>
  );
};

export default Projects;