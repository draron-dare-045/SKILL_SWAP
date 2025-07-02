// frontend/src/components/Header.jsx
import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { useAuth } from '../context/AuthContext.jsx';

// Inline style for the gradient background
const headerStyle = {
  background: 'linear-gradient(90deg, var(--secondary-color), var(--primary-color))',
  boxShadow: '0 2px 10px rgba(0, 0, 0, 0.1)'
};

// Style for the active NavLink
const activeLinkStyle = {
  fontWeight: '600',
  color: '#fff',
  borderBottom: '2px solid #fff'
};

function Header() {
  const { user, logout } = useAuth();

  return (
    <header className="navbar navbar-expand-lg navbar-dark sticky-top" style={headerStyle}>
      <div className="container">
        <Link className="navbar-brand" to="/" style={{fontWeight: 700, fontSize: '1.5rem'}}>
          SkillSwap
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link" to="/" style={({ isActive }) => isActive ? activeLinkStyle : undefined }>
                Home
              </NavLink>
            </li>
            {user && (
              <li className="nav-item">
                <NavLink className="nav-link" to="/add-skill" style={({ isActive }) => isActive ? activeLinkStyle : undefined }>
                  Add Skill
                </NavLink>
              </li>
            )}
            {user?.role === 'admin' && (
              <li className="nav-item">
                <NavLink className="nav-link" to="/admin" style={({ isActive }) => isActive ? activeLinkStyle : undefined }>
                  Admin Dashboard
                </NavLink>
              </li>
            )}
          </ul>
          <div className="d-flex align-items-center">
            {user ? (
              <>
                <span className="navbar-text me-3">
                  Welcome, {user.username}!
                </span>
                <button onClick={logout} className="btn btn-outline-light">Logout</button>
              </>
            ) : (
              <>
                <Link to="/login" className="btn btn-outline-light me-2">Login</Link>
                <Link to="/register" className="btn btn-light">Register</Link>
              </>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}
export default Header;