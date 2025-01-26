import React, { useState } from "react";
import "./Login.css"; // Make sure your styles handle responsiveness
import { Link, useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Dummy user credentials (for simulation purposes)
  const dummyUser = {
    email: "wilzilla@gnail.com",
    password: "password123",
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(""); // Clear previous errors

    // Local dummy login logic
    if (email === dummyUser.email && password === dummyUser.password) {
      localStorage.setItem("token", "dummy-auth-token"); // Simulate login token
      navigate("/profile"); // Redirect to the profile page
      setLoading(false);
      return;
    }

    // Simulate a backend API call for login
    try {
      const response = await fetch("https://collabo-app.onrender.com/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        // Save user info to localStorage
        localStorage.setItem("token", data.token);
        localStorage.setItem("user", JSON.stringify(data.user));
        navigate("/profile"); // Redirect to profile
      } else {
        setError(
          data.message || "Login failed. Please check your credentials."
        );
      }
    } catch (err) {
      setError("An error occurred. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      {/* Logo */}
      <div className="logo-container">
        <img src="/Collabo.png" alt="Collabo Logo" className="logo" />
      </div>

      {/* Login Form */}
      <div className="login-card">
        <h2 className="login-title">Log In</h2>
        <p className="login-subtitle">
          Don’t have an account? <Link to="/signup">Sign up here</Link>
        </p>

        {/* Display errors if any */}
        {error && <p className="error-message">{error}</p>}

        <form onSubmit={handleLogin} className="login-form">
          {/* Email Field */}
          <div className="form-group">
            <label htmlFor="email">Email Address</label>
            <input
              type="email"
              id="email"
              className="form-control"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          {/* Password Field */}
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <div className="password-wrapper">
              <input
                type={showPassword ? "text" : "password"}
                id="password"
                className="form-control"
                placeholder="Enter your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
              <button
                type="button"
                className="toggle-password"
                onClick={() => setShowPassword(!showPassword)}
              >
                <i
                  className={`bi ${showPassword ? "bi-eye" : "bi-eye-slash"}`}
                ></i>
              </button>
            </div>
          </div>

          {/* Remember Me */}
          <div className="form-group">
            <input type="checkbox" id="remember-me" />
            <label htmlFor="remember-me" className="remember-me-label">
              Remember me
            </label>
          </div>

          {/* Submit Button */}
          <button type="submit" className="login-button" disabled={loading}>
            {loading ? "Logging in..." : "Log In"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
