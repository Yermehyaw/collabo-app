import React from 'react';
import './ProjectCard.css';

const ProjectCard = ({ project, onPeersClick }) => (
  <div className="project-card">
    <h5>{project.name}</h5>
    <p className="project-description">{project.description}</p>
    <p><strong>Technologies:</strong> {project.technologies}</p>
    <p><strong>Schedule Date:</strong> {project.scheduleDate}</p>
    <p className="peers-list">
      <strong>Peers:</strong>
      <div className="peers-avatars">
        {project.peers.map(peer => (
          <img 
            key={peer.id}
            src={peer.avatar}
            alt="Avatar"
            className="peer-avatar"
          />
        ))}
        <button 
          onClick={onPeersClick}
          className="more-peers-button"
        >
          ...
        </button>
      </div>
    </p>
  </div>
);

export default ProjectCard;