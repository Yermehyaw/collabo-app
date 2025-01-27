import React from 'react';
import './ProjectCard.css';

const ProjectCard = ({ project, onPeersClick }) => {
  return (
    <div className="project-card">
      <h5 className="project-title">{project.name}</h5>
      <p className="project-description">{project.description}</p>
      <p className="project-info">
        <strong>Technologies:</strong> {project.technologies}
      </p>
      <p className="project-info">
        <strong>Schedule Date:</strong> {project.scheduleDate}
      </p>
      <div className="peers-section">
        <strong>Peers:</strong>
        <div className="peers-list">
          {project.peers.slice(0, 3).map(peer => (
            <img 
              key={peer.id}
              src={peer.avatar}
              alt="Peer avatar"
              className="peer-avatar"
            />
          ))}
          {project.peers.length > 3 && (
            <button 
              className="more-peers"
              onClick={onPeersClick}
            >
              ...
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProjectCard;