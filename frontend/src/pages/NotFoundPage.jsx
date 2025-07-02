// frontend/src/pages/NotFoundPage.jsx
import React from 'react';
import { Link } from 'react-router-dom';

function NotFoundPage() {
  return (
    <div className="text-center mt-5">
      <h1>404</h1>
      <h2>Page Not Found</h2>
      <p className="lead">Sorry, the page you are looking for does not exist.</p>
      <Link to="/" className="btn btn-primary">Go to Homepage</Link>
    </div>
  );
}

export default NotFoundPage;