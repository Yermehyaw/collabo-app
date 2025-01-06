import React, { useState } from "react";

// Sample data for projects
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

  // Function to handle search
  const handleSearch = (e) => {
    e.preventDefault();
    const filteredProjects = sampleProjects.filter((project) =>
      project.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setProjects(filteredProjects);
  };

  const styles = {
    page: {
      padding: "20px",
      fontFamily: "Arial, sans-serif",
    },
    searchBar: {
      marginBottom: "20px",
      display: "flex",
      gap: "10px",
    },
    input: {
      flex: 1,
      padding: "10px",
      fontSize: "16px",
      border: "1px solid #ccc",
      borderRadius: "4px",
    },
    button: {
      padding: "10px 20px",
      backgroundColor: "#4CAF50",
      color: "white",
      border: "none",
      borderRadius: "4px",
      cursor: "pointer",
    },
    projectList: {
      display: "grid",
      gap: "20px",
      gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
    },
    projectCard: {
      padding: "15px",
      border: "1px solid #ccc",
      borderRadius: "4px",
      backgroundColor: "#f9f9f9",
    },
  };

  return (
    <div style={styles.page}>
      <h1>Projects</h1>

      {/* Search Bar */}
      <form onSubmit={handleSearch} style={styles.searchBar}>
        <input
          type="text"
          placeholder="Search for projects..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={styles.input}
        />
        <button type="submit" style={styles.button}>
          Search
        </button>
      </form>

      {/* Project List */}
      <div style={styles.projectList}>
        {projects.length > 0 ? (
          projects.map((project) => (
            <div key={project.id} style={styles.projectCard}>
              <h3>{project.name}</h3>
              <p>{project.description}</p>
            </div>
          ))
        ) : (
          <p>No projects found.</p>
        )}
      </div>
    </div>
  );
};

export default ProjectPage;
