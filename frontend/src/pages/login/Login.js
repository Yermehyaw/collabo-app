import React, { useState } from "react";
import PropTypes from "prop-types";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Login.css";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";
import { FaHome } from "react-icons/fa";


// Use fetch to submit http login request
async function loginUser(credentials) {
  return fetch("https://collabo-app.onrender.com/auth/login", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
}

// Use fetch to submit signup request
async function signupUser(credentials) {
  return fetch("https://collabo-app.onrender.com/auth/signup", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
}

const AuthPage = ( {setToken} ) => {
  const [isLogin, setIsLogin] = useState(true); // Toggle between Login and Sign Up forms
  const [passwordVisibility, setPasswordVisibility] = useState({
    createPassword: false,
    confirmPassword: false,
  });
  const [email, setEmail] = useState("");
  const [name, setUserName] = useState("");
  const [password, setPassword] = useState("");

  // Toggle password visibility
  const togglePasswordVisibility = (field) => {
    setPasswordVisibility((prevState) => ({
      ...prevState,
      [field]: !prevState[field],
    }));
  };

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
    const response = await loginUser({
      email, password
    });
    if (response.access_token) {
      setToken(response.access_token);
      console.log("Login form submitted");
    } else {
      console.log("Login failed". response);
    }
  };

  const handleSignUpSubmit = async (e) => {
    e.preventDefault();
    const response = await signupUser({
      email, password, name
    });
    console.log("Sign Up form submitted");
  };

  return (
    <div className="  align-items-center justify-content-center min-vh-100">
      <div className="Login-header text-align-center">
        <h3 className="text-center m-4 text-white mb-2"> COLLABO</h3>
      </div>
      <div className="auth-card p-4 shadow-sm border-0  mt-4 mb-5">
        <div className="text-center mb-4 d-flex justify-content-between">
          {" "}
          <Link to={"/"}>
            <FaHome size={24} color="green" />
          </Link>{" "}
          <h3 className="text-center mb-4">{isLogin ? "Log In" : "Sign Up"}</h3>
        </div>

        {isLogin ? (
          // Login Form
          <form onSubmit={handleLoginSubmit}>
            <div className="mb-3">
              <label htmlFor="loginEmail" className="form-label">
                Email Address
              </label>
              <input
                type="email"
		onChange={e => setEmail(e.target.value)}
                className="form-control"
                id="loginEmail"
                placeholder="Enter your email"
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="loginPassword" className="form-label">
                Password
              </label>
              <input
                type="password"
		onChange={e => setPassword(e.target.value)}
                className="form-control"
                id="loginPassword"
                placeholder="Enter your password"
                required
              />
            </div>
            <div className="mb-3 form-check">
              <input
                type="checkbox"
                className="form-check-input"
                id="rememberMe"
              />
              <label htmlFor="rememberMe" className="form-check-label">
                Remember me
              </label>
            </div>
            <button type="submit" className="btn btn-primary w-100">
              Log In
            </button>
            <div className="mt-3 text-center">
              <span>Don't have an account? </span>
              <button
                type="button"
                className="btn btn-link p-0"
                onClick={() => setIsLogin(false)}
              >
                Sign Up
              </button>
            </div>
          </form>
        ) : (
          // Sign Up Form
          <form onSubmit={handleSignUpSubmit}>
            <div className="mb-3">
              <label htmlFor="signupEmail" className="form-label">
                First Name
              </label>
              <input
                type="text"
		className="form-control"
                id="signupEmail"
                placeholder="Enter your first name"
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="signupEmail" className="form-label">
                Last Name
              </label>
              <input
                type="text"
                className="form-control"
                id="signupEmail"
                placeholder="Enter your last name"
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="username" className="form-label">
                Username
              </label>
              <input
                type="text"
		onChange={e => setUserName(e.target.value)}
                className="form-control"
                id="username"
                placeholder="Choose a username"
                required
              />
            </div>

            <div className="mb-3">
              <label htmlFor="signupEmail" className="form-label">
                Email Address
              </label>
              <input
                type="email"
	        onChange={e => setEmail(e.target.value)}
                className="form-control"
                id="signupEmail"
                placeholder="Enter your email"
                required
              />
            </div>
            <div className="mb-3 position-relative">
              <label htmlFor="createPassword" className="form-label">
                Create Password
              </label>
              <input
                type={passwordVisibility.createPassword ? "text" : "password"}
	        onChange={e => setPassword(e.target.value)}
                className="form-control"
                id="createPassword"
                placeholder="Create your password"
                required
              />
              <button
                type="button"
                className="btn btn-outline-secondary toggle-password-btn"
                onClick={() => togglePasswordVisibility("createPassword")}
              >
                {passwordVisibility.createPassword ? "🙈" : "👁️"}
              </button>
            </div>
            <div className="mb-3 position-relative">
              <label htmlFor="confirmPassword" className="form-label">
                Confirm Password
              </label>
              <input
                type={passwordVisibility.confirmPassword ? "text" : "password"}
                className="form-control"
                id="confirmPassword"
                placeholder="Confirm your password"
                required
              />
              <button
                type="button"
                className="btn btn-outline-secondary toggle-password-btn"
                onClick={() => togglePasswordVisibility("confirmPassword")}
              >
                {passwordVisibility.confirmPassword ? "🙈" : "👁️"}
              </button>
            </div>
            <button type="submit" className="btn btn-primary w-100">
              Sign Up
            </button>
            <div className="mt-3 text-center">
              <span>Already have an account? </span>
              <button
                type="button"
                className="btn btn-link p-0"
                onClick={() => setIsLogin(true)}
              >
                Log In
              </button>
            </div>
          </form>
        )}
      </div>
      <Footer />
    </div>
  );

  AuthPage.Login.propTypes = (
    setToken: PropTypes.func.isRequired,
  );
};

export default AuthPage;
