import React from 'react';
import './PeerCard.css';

const PeerCard = ({ peer }) => (
  <div className="peer-card">
    <img 
      src={peer.avatar}
      className="peer-avatar"
      alt={`${peer.name}'s avatar`}
    />
    <h5>{peer.name}</h5>
    <p className="peer-role">{peer.role}</p>
    <p><strong>Skills:</strong> {peer.skills}</p>
    <button className="connect-button">
      Connect
    </button>
  </div>
);

export default PeerCard;