import React, { useState } from 'react';
import './SearchResults.css';
import ProjectCard from './components/ProjectCard';
import PeerCard from './components/PeerCard';
import PeersModal from './components/PeersModal';

const SearchResults = () => {
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
        { id: 3, avatar: "/api/placeholder/30/30" }
      ]
    },
    {
      id: 2,
      name: "Project Beta",
      description: "Description of Project Beta",
      technologies: "Python, Django",
      scheduleDate: "2023-12-15",
      peers: [
        { id: 4, avatar: "/api/placeholder/30/30" },
        { id: 5, avatar: "/api/placeholder/30/30" },
        { id: 6, avatar: "/api/placeholder/30/30" }
      ]
    },
    {
      id: 3,
      name: "Project Gamma",
      description: "Description of Project Gamma",
      technologies: "Java, Spring Boot",
      scheduleDate: "2023-12-20",
      peers: [
        { id: 7, avatar: "/api/placeholder/30/30" },
        { id: 8, avatar: "/api/placeholder/30/30" },
        { id: 9, avatar: "/api/placeholder/30/30" }
      ]
    }
  ];

  const peers = [
    {
      id: 1,
      name: "John Doe",
      role: "Web Developer",
      skills: "HTML, CSS, JavaScript",
      avatar: "/api/placeholder/30/30"
    },
    {
      id: 2,
      name: "Jane Smith",
      role: "Graphic Designer",
      skills: "Photoshop, Illustrator, InDesign",
      avatar: "/api/placeholder/30/30"
    },
    {
      id: 3,
      name: "Alice Johnson",
      role: "Project Manager",
      skills: "Agile, Scrum, Leadership",
      avatar: "/api/placeholder/30/30"
    }
  ];

  return (
    <div className="search-results-container">
      <div className="search-results-wrapper">
        <div className="search-header">
          <h1>Search Results</h1>
          <div className="search-input-wrapper">
            <input
              type="text"
              className="search-input"
              placeholder="Search projects and peers"
            />
            <button className="search-button">
              🔍
            </button>
          </div>
        </div>

        <section className="projects-section">
          <h2>Results for Projects</h2>
          <div className="projects-grid">
            {projects.map(project => (
              <ProjectCard 
                key={project.id} 
                project={project} 
                onPeersClick={() => setSelectedProject(project)} 
              />
            ))}
          </div>
        </section>

        <section className="peers-section">
          <h2>Results for Peers</h2>
          <div className="peers-grid">
            {peers.map(peer => (
              <PeerCard key={peer.id} peer={peer} />
            ))}
          </div>
        </section>

        <div className="pagination">
          <nav>
            <button>Previous</button>
            <button>1</button>
            <button>2</button>
            <button>3</button>
            <button>Next</button>
          </nav>
        </div>

        {selectedProject && (
          <PeersModal 
            project={selectedProject} 
            onClose={() => setSelectedProject(null)} 
          />
        )}
      </div>
    </div>
  );
};

export default SearchResults;