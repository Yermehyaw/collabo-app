import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./createProject.css";

const CreateProject = () => {
  const [formData, setFormData] = useState({
    projectName: "",
    projectDescription: "",
    projectPeers: "",
    scheduleDate: "",
    technologies: "",
  });

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData({
      ...formData,
      [id]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Safely send formData to the backend
    console.log("Form Data Submitted:", formData);

    // Example: Post data to backend
    // fetch("/api/create-project", {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json",
    //   },
    //   body: JSON.stringify(formData),
    // })
    //   .then((response) => response.json())
    //   .then((data) => console.log(data));
  };

  return (
    <div className="container mt-5">
      <div className="row mb-4">
        <div className="col-md-12">
          <h1 className="text-center">Create Project</h1>
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

            <div className="form-group d-flex justify-content-between">
              <button type="submit" className="btn btn-success">
                Create
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

export default CreateProject;
