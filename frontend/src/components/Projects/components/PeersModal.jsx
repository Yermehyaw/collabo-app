import React from 'react';
import './PeersModal.css';

const PeersModal = ({ project, onClose }) => {
  if (!project) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <div className="modal-header">
          <h5 className="modal-title">
            Peers working on {project.name}
          </h5>
          <button 
            className="close-button"
            onClick={onClose}
          >
            ×
          </button>
        </div>
        <div className="modal-body">
          {project.peers.map(peer => (
            <img 
              key={peer.id}
              src={peer.avatar}
              alt="Peer avatar"
              className="modal-peer-avatar"
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default PeersModal;