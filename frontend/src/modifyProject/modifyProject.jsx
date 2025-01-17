import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
const ModifyProject = () => {
  const [formData, setFormData] = useState({
    projectName: "Project Alpha",
    projectDescription: "Description of Project Alpha",
    projectPeers: "John Doe, Jane Smith",
    scheduleDate: "2023-12-01",
    technologies: "HTML, CSS, JavaScript",
    markCompleted: false,
  });

  const handleChange = (e) => {
    const { id, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [id]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send data to the backend
      const response = await fetch("/api/modify-project", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        console.log("Project successfully updated");
        alert("Project successfully updated");
      } else {
        console.error("Failed to update project");
        alert("Failed to update project");
      }
    } catch (error) {
      console.error("Error updating project:", error);
      alert("Error updating project");
    }
  };

  return (
    <div className="container mt-5">
      <div className="row mb-4">
        <div className="col-md-12">
          <h1 className="text-center">Modify Project</h1>
        </div>
      </div>
      <div className="row">
        <div className="col-md-8 offset-md-2">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="projectName">Project Name</label>
              <input
                type="text"
                className="form-control"
                id="projectName"
                placeholder="Enter project name"
                value={formData.projectName}
                onChange={handleChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="projectDescription">Description</label>
              <textarea
                className="form-control"
                id="projectDescription"
                rows="3"
                placeholder="Enter project description"
                value={formData.projectDescription}
                onChange={handleChange}
              ></textarea>
            </div>

            <div className="form-group">
              <label htmlFor="projectPeers">Add Peers</label>
              <input
                type="text"
                className="form-control"
                id="projectPeers"
                placeholder="Enter peer names"
                value={formData.projectPeers}
                onChange={handleChange}
              />
              <small className="form-text text-muted">
                Separate names with commas.
              </small>
            </div>

            <div className="form-group">
              <label htmlFor="scheduleDate">Schedule Date</label>
              <input
                type="date"
                className="form-control"
                id="scheduleDate"
                value={formData.scheduleDate}
                onChange={handleChange}
              />
            </div>

            <div className="form-group">
              <label htmlFor="technologies">Technologies</label>
              <input
                type="text"
                className="form-control"
                id="technologies"
                placeholder="Enter technologies"
                value={formData.technologies}
                onChange={handleChange}
              />
              <small className="form-text text-muted">
                Suggested: HTML, CSS, JavaScript, Python, Django, Java, Spring
                Boot
              </small>
            </div>

            <div className="form-group form-check">
              <input
                type="checkbox"
                className="form-check-input"
                id="markCompleted"
                checked={formData.markCompleted}
                onChange={handleChange}
              />
              <label className="form-check-label" htmlFor="markCompleted">
                Mark as Completed
              </label>
            </div>

            <div className="form-group d-flex justify-content-between">
              <button type="submit" className="btn btn-success">
                Save Changes
              </button>
              <button type="button" className="btn btn-danger">
                Delete
              </button>
              <button type="button" className="btn btn-secondary">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ModifyProject;
