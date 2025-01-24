import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "bootstrap-icons/font/bootstrap-icons.css"; // Bootstrap Icons
import { Nav, Form, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import "./Navbar.css";

function NavbarComponent() {
  return (
    <Nav className="navbar navbar-expand-lg navbar-light bg-light justify-content-center mx-3">
      <Link to={"/"} className="navbar-brand ">
        <img src="/Collabo.png" alt="Collabo" height={40} />
      </Link>

      {/* SEARCH BAR  */}
      <Form className="d-flex mx-auto search-bar-container">
        <input
          className="form-control mr-sm-2"
          type="search"
          placeholder="Search project and peers"
          aria-label="Search"
        />
        <Button
          variant="outline-primary"
          type="submit"
          className="btn btn-outline-primary my-2 my-sm-0"
        >
          <i className="bi bi-search"></i>
        </Button>
      </Form>
      <Button
        className="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </Button>

      <div className="collapse navbar-collapse " id="navbarNav">
        <ul className="navbar-nav ms-auto">
          <li className="nav-item">
            <Link className="nav-link" to={"/Login"}>
              Dashboard
            </Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to={"/Peers"}>
              Peers
            </Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to={"/Projects"}>
              Projects
            </Link>
          </li>

          {/* Notification dropdown */}
          <li className="nav-item dropdown">
            <Link
              className="nav-link dropdown-toggle notification-icon"
              role="button"
              data-bs-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <i className="bi bi-bell"></i>
              <span className="badge badge-notification">3</span>
            </Link>
            <div
              className="dropdown-menu dropdown-menu-end"
              aria-labelledby="notificationsDropdown"
            >
              <div className="dropdown-header">Notifications</div>
              <Link key={1} className="dropdown-item" to={"#"}>
                <img
                  src="https://randomuser.me/api/portraits/men/1.jpg"
                  alt="Avatar"
                />
                Notification 1
              </Link>
              <Link key={2} className="dropdown-item" to={"#"}>
                <img
                  src="https://randomuser.me/api/portraits/women/2.jpg"
                  alt="Avatar"
                />
                Notification 2
              </Link>
              <Link key={3} className="dropdown-item" to={"#"}>
                <img
                  src="https://randomuser.me/api/portraits/men/3.jpg"
                  alt="Avatar"
                />
                Notification 3
              </Link>
              <div className="dropdown-footer">
                <Link to={"/notifications"}>view all</Link>
              </div>
            </div>
          </li>

          {/* MESSAGE DROP-DOWN */}
          <li className="nav-item dropdown ">
            <Link
              className="nav-link dropdown-toggle notification-icon"
              role="button"
              data-bs-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <i className="bi bi-envelope "></i>
              <span className="badge badge-notification">5</span>
            </Link>
            <div
              className="dropdown-menu dropdown-menu-end"
              aria-labelledby="messagesDropdown"
            >
              <div className="dropdown-header">Messages</div>
              <Link key={1} className="dropdown-item" to="#">
                <img
                  src="https://randomuser.me/api/portraits/men/1.jpg"
                  alt="Avatar"
                />
                John Doe: Message 1
              </Link>
              <Link key={2} className="dropdown-item" to="#">
                <img
                  src="https://randomuser.me/api/portraits/women/1.jpg"
                  alt="Avatar"
                />
                Jane Smith: Message 2
              </Link>
              <Link to={"/MessagingApp"} key={3} className="dropdown-item">
                <img
                  src="https://randomuser.me/api/portraits/men/3.jpg"
                  alt="Avatar"
                />
                Bob Brown: Message 3
              </Link>
              <div className="dropdown-footer">
                <Link to={"/MessagingApp"}> View all </Link>
              </div>
            </div>
          </li>

          {/* PROFILE DROPDOWN */}
          <li className="nav-item dropdown">
            <Link
              to={"#"}
              className="nav-link"
              id="profiledropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <img
                src="https://randomuser.me/api/portraits/men/1.jpg"
                alt="Avatar"
                className="rounded-circle"
                width="30"
                height="30"
              />
            </Link>
            <div
              className="dropdown-menu dropdown-menu-end"
              aria-labelledby="profiledropdown"
            >
              <Link className="dropdown-item" to="/Profile">
                Profile
              </Link>
              <Link className="dropdown-item" to="/settings">
                Settings
              </Link>
              <Link className="dropdown-item" to="/login">
                Logout
              </Link>
            </div>
          </li>
        </ul>
      </div>
    </Nav>
  );
}

export default NavbarComponent;
