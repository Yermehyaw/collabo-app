import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./SignUp.css"; // Additional custom styling if needed

const SignUp = () => {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    gender: "",
    username: "",
    dob: "",
    password: "",
    confirmPassword: "",
  });

  const [usernameAvailable, setUsernameAvailable] = useState(null);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [passwordCriteriaMet, setPasswordCriteriaMet] = useState(false);
  const [passwordsMatch, setPasswordsMatch] = useState(null); // null initially

  const handleChange = async (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    if (name === "username") {
      try {
        const response = await fetch(
          `https://your-backend-api.com/check-username?username=${value}`
        );
        const data = await response.json();
        setUsernameAvailable(data.available);
      } catch (err) {
        console.error("Error checking username availability:", err);
        setUsernameAvailable(null);
      }
    }

    if (name === "password") {
      const passwordRegex =
        /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;
      setPasswordCriteriaMet(passwordRegex.test(value));
    }
    if (name === "confirmPassword") {
      // Check if the passwords match
      setPasswordsMatch(value === formData.password);
    }

    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handlePasswordBlur = () => {
    // Trigger match validation on blur for confirmPassword field
    setPasswordsMatch(formData.password === formData.confirmPassword);
  };

  const handleSignUp = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    if (!passwordCriteriaMet) {
      setError(
        "Password must contain at least one uppercase letter, one number, and one special character."
      );
      setLoading(false);
      return;
    }

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match!");
      setLoading(false);
      return;
    }

    try {
      const response = await fetch("https://your-backend-api.com/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Sign up successful! Please log in.");
        window.location.href = "/login";
      } else {
        setError(data.message || "Sign up failed. Please try again.");
      }
    } catch (err) {
      setError("An error occurred. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="container d-flex justify-content-center align-items-center"
      id="sign-up"
    >
      <div className="card shadow-lg p-4 w-100" style={{ maxWidth: "500px" }}>
        <div className="text-center mb-4">
          <img
            src="/Collabo.png"
            alt="Collabo Logo"
            className="img-fluid"
            style={{ width: "100px" }}
          />
          <h2 className="mt-3">Sign Up</h2>
          <p>
            Already have an account?{" "}
            <a href="/login" className="text-primary">
              Log in here
            </a>
          </p>
        </div>
        {error && <div className="alert alert-danger">{error}</div>}
        <form onSubmit={handleSignUp}>
          <div className="mb-3">
            <label htmlFor="firstName" className="form-label">
              First Name
            </label>
            <input
              type="text"
              id="firstName"
              name="firstName"
              className="form-control"
              placeholder="Enter your first name"
              value={formData.firstName}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label htmlFor="lastName" className="form-label">
              Last Name
            </label>
            <input
              type="text"
              id="lastName"
              name="lastName"
              className="form-control"
              placeholder="Enter your last name"
              value={formData.lastName}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label htmlFor="email" className="form-label">
              Email Address
            </label>
            <input
              type="email"
              id="email"
              name="email"
              className="form-control"
              placeholder="Enter your email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label htmlFor="gender" className="form-label">
              Gender
            </label>
            <select
              id="gender"
              name="gender"
              className="form-select"
              value={formData.gender}
              onChange={handleChange}
              required
            >
              <option value="">Select Gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div className="mb-3">
            <label htmlFor="username" className="form-label">
              Username
            </label>
            <input
              type="text"
              id="username"
              name="username"
              className="form-control"
              placeholder="Enter a username"
              value={formData.username}
              onChange={handleChange}
              required
            />
            {usernameAvailable !== null && (
              <small
                className={`text-${usernameAvailable ? "success" : "danger"}`}
              >
                {usernameAvailable
                  ? "Username is available!"
                  : "Username is taken. Please choose another."}
              </small>
            )}
          </div>
          <div className="mb-3">
            <label htmlFor="dob" className="form-label">
              Date of Birth
            </label>
            <input
              type="date"
              id="dob"
              name="dob"
              className="form-control"
              value={formData.dob}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3 position-relative">
            <label htmlFor="password" className="form-label">
              Password
            </label>
            <input
              type={showPassword ? "text" : "password"}
              id="password"
              name="password"
              className={`form-control ${
                passwordCriteriaMet === null
                  ? "" // Default styling
                  : passwordCriteriaMet
                  ? "is-valid" // Green outline
                  : "is-invalid" // Red outline
              }`}
              placeholder="Enter your password"
              value={formData.password}
              onChange={handleChange}
              required
            />
            <button
              type="button"
              className="btn btn-light btn-sm position-absolute top-50 end-0 translate-middle-y"
              onClick={() => setShowPassword(!showPassword)}
            >
              <i
                className={`bi ${showPassword ? "bi-eye" : "bi-eye-slash"}`}
                style={{ filter: "none", background: "transparent" }}
              ></i>
            </button>
            <small className="text-muted">
              Password must contain at least one uppercase letter, one number,
              and one special character (e.g., !@#$%^&*).
            </small>
          </div>
          <div className="mb-3 position-relative">
            <label htmlFor="confirmPassword" className="form-label">
              Confirm Password
            </label>
            <input
              type={showConfirmPassword ? "text" : "password"}
              id="confirmPassword"
              name="confirmPassword"
              className={`form-control ${
                passwordsMatch === null
                  ? "" // Default styling
                  : passwordsMatch
                  ? "is-valid" // Green border
                  : "is-invalid" // Red border
              }`}
              placeholder="Confirm your password"
              value={formData.confirmPassword}
              onChange={handleChange}
              onBlur={handlePasswordBlur}
              required
            />
            <button
              type="button"
              className="btn btn-light btn-sm position-absolute top-50 end-0 translate-middle-y"
              onClick={() => setShowConfirmPassword(!showConfirmPassword)}
              style={{
                background: "transparent",
                border: "none",
                boxShadow: "none",
                outline: "none",
              }}
            >
              <i
                className={`bi ${
                  showConfirmPassword ? "bi-eye" : "bi-eye-slash"
                }`}
                style={{ filter: "none" }}
              ></i>
            </button>
          </div>
          <button
            type="submit"
            className="btn btn-primary w-100"
            disabled={loading}
          >
            {loading ? "Signing up..." : "Sign Up"}
          </button>
        </form>
        <div className="text-center mt-3">
          <p>Or sign up with:</p>
          <div className="d-flex justify-content-center gap-2">
            <button className="btn btn-outline-primary">Facebook</button>
            <button className="btn btn-outline-danger">Google</button>
            <button className="btn btn-outline-info">LinkedIn</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
