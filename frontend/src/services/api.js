import dotenv from 'dotenv';

dotenv.config();
const API_URL = process.env.API_URL || "http://localhost:3000";

export default async function apiRequest() {
  const token = localStorage.getItem("token");

  const headers = {
    "Content-Type": "application/json",
    ...options.headers,
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_URL}${endpoint}`, {...options, headers});

  // Expired token
  if (response.status === 401) {
    alert("Session expired. Kindly log in again.");
    localStorage.removeItem("token");
    window.loacation.href = "/login"; // Redirect to login page
    return null;
  }

  return response.json();
}