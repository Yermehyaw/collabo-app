import React, { useState } from "react";
import "./peers.css"; // Import your CSS file here

// Expanded peers dataset
const peersData = [
  // Page 1 (9 users)
  {
    id: 1,
    name: "John Doe",
    role: "Web Developer",
    skills: "HTML, CSS, JavaScript",
    image: "https://randomuser.me/api/portraits/men/1.jpg",
  },
  {
    id: 2,
    name: "Jane Smith",
    role: "Graphic Designer",
    skills: "Photoshop, Illustrator, InDesign",
    image: "https://randomuser.me/api/portraits/women/2.jpg",
  },
  {
    id: 3,
    name: "Alice Johnson",
    role: "Project Manager",
    skills: "Agile, Scrum, Leadership",
    image: "https://randomuser.me/api/portraits/women/3.jpg",
  },
  {
    id: 4,
    name: "Bob Brown",
    role: "Software Engineer",
    skills: "Java, Python, C++",
    image: "https://randomuser.me/api/portraits/men/4.jpg",
  },
  {
    id: 5,
    name: "Charlie Davis",
    role: "Data Scientist",
    skills: "R, Python, SQL",
    image: "https://randomuser.me/api/portraits/men/5.jpg",
  },
  {
    id: 6,
    name: "Diana Evans",
    role: "UX Designer",
    skills: "Wireframing, Prototyping, User Research",
    image: "https://randomuser.me/api/portraits/women/6.jpg",
  },
  {
    id: 7,
    name: "Ethan Foster",
    role: "Marketing Specialist",
    skills: "SEO, Content Marketing, Social Media",
    image: "https://randomuser.me/api/portraits/men/7.jpg",
  },
  {
    id: 8,
    name: "Fiona Green",
    role: "Content Writer",
    skills: "Copywriting, Blogging, Editing",
    image: "https://randomuser.me/api/portraits/women/8.jpg",
  },
  {
    id: 9,
    name: "George Harris",
    role: "SEO Specialist",
    skills: "SEO, Google Analytics, SEM",
    image: "https://randomuser.me/api/portraits/men/9.jpg",
  },

  // Page 2 (9 users)
  {
    id: 10,
    name: "Hannah Lee",
    role: "DevOps Engineer",
    skills: "AWS, Kubernetes, Jenkins",
    image: "https://randomuser.me/api/portraits/women/9.jpg",
  },
  {
    id: 11,
    name: "Isaac Moore",
    role: "Game Developer",
    skills: "Unity, C#, Unreal Engine",
    image: "https://randomuser.me/api/portraits/men/10.jpg",
  },
  {
    id: 12,
    name: "Julia Parker",
    role: "AI Researcher",
    skills: "Machine Learning, AI Ethics, NLP",
    image: "https://randomuser.me/api/portraits/women/10.jpg",
  },
  {
    id: 13,
    name: "Kevin Miller",
    role: "Blockchain Engineer",
    skills: "Solidity, Ethereum, Bitcoin",
    image: "https://randomuser.me/api/portraits/men/11.jpg",
  },
  {
    id: 14,
    name: "Laura Phillips",
    role: "Cybersecurity Analyst",
    skills: "Penetration Testing, Cryptography, Forensics",
    image: "https://randomuser.me/api/portraits/women/11.jpg",
  },
  {
    id: 15,
    name: "Mike Rodriguez",
    role: "Cloud Engineer",
    skills: "Azure, AWS, Google Cloud",
    image: "https://randomuser.me/api/portraits/men/12.jpg",
  },
  {
    id: 16,
    name: "Nancy Thompson",
    role: "Mobile App Developer",
    skills: "iOS, Android, Flutter",
    image: "https://randomuser.me/api/portraits/women/12.jpg",
  },
  {
    id: 17,
    name: "Oliver White",
    role: "Database Administrator",
    skills: "MySQL, PostgreSQL, MongoDB",
    image: "https://randomuser.me/api/portraits/men/13.jpg",
  },
  {
    id: 18,
    name: "Paula Brown",
    role: "Business Analyst",
    skills: "Requirement Gathering, Process Improvement, Reporting",
    image: "https://randomuser.me/api/portraits/women/13.jpg",
  },

  // Add more users for pages 3, 4, and 5 following the same structure
];

// Component
const Peers = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const peersPerPage = 9;

  // Filtering the peers based on the search term
  const filteredPeers = peersData.filter(
    (peer) =>
      peer.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      peer.role.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // Pagination logic
  const totalPages = Math.ceil(filteredPeers.length / peersPerPage);
  const startIndex = (currentPage - 1) * peersPerPage;
  const currentPeers = filteredPeers.slice(
    startIndex,
    startIndex + peersPerPage
  );

  const handleNext = () => {
    if (currentPage < totalPages) setCurrentPage(currentPage + 1);
  };

  const handlePrev = () => {
    if (currentPage > 1) setCurrentPage(currentPage - 1);
  };

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-12 text-center mb-4">
          <h1 className="text-primary">Peers You May Want to Connect With</h1>
        </div>
        <div className="col-12 mb-4">
          <input
            type="text"
            className="form-control"
            placeholder="Search peers by name or project..."
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              setCurrentPage(1); // Reset to page 1 on search
            }}
          />
        </div>
      </div>
      <div className="row">
        {currentPeers.map((peer) => (
          <div key={peer.id} className="col-md-4 mb-4">
            <div className="card">
              <div className="card-body text-center">
                <img
                  src={peer.image}
                  className="rounded-circle mb-3"
                  alt="Avatar"
                  width="100"
                  height="100"
                />
                <h5 className="card-title">{peer.name}</h5>
                <p className="card-text">{peer.role}</p>
                <p className="card-text">
                  <strong>Skills:</strong> {peer.skills}
                </p>
                <button className="btn btn-primary">Connect</button>
              </div>
            </div>
          </div>
        ))}
        {currentPeers.length === 0 && (
          <div className="col-12 text-center">
            <p className="text-muted">
              No peers found. Try a different search.
            </p>
          </div>
        )}
      </div>
      <div className="row">
        <div className="col-12 text-center mt-4">
          <button
            className="btn btn-outline-primary me-2"
            onClick={handlePrev}
            disabled={currentPage === 1}
          >
            &laquo; Prev
          </button>
          {Array.from({ length: totalPages }, (_, index) => (
            <button
              key={index + 1}
              className={`btn ${
                currentPage === index + 1
                  ? "btn-primary"
                  : "btn-outline-primary"
              } mx-1`}
              onClick={() => setCurrentPage(index + 1)}
            >
              {index + 1}
            </button>
          ))}
          <button
            className="btn btn-outline-primary ms-2"
            onClick={handleNext}
            disabled={currentPage === totalPages}
          >
            Next &raquo;
          </button>
        </div>
      </div>
    </div>
  );
};

export default Peers;
