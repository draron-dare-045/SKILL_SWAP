// frontend/src/pages/AddSkillPage.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/axiosConfig';

function AddSkillPage() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
      await api.post('/skills/', { name, description });
      setSuccess('Skill added successfully! Redirecting to homepage...');
      setTimeout(() => {
        navigate('/');
      }, 2000);
    } catch (err) {
      setError('Failed to add skill. Please try again.');
      console.error(err);
    }
  };

  return (
    <div className="row justify-content-center">
      <div className="col-md-8">
        <h2>Offer a New Skill</h2>
        {error && <div className="alert alert-danger">{error}</div>}
        {success && <div className="alert alert-success">{success}</div>}
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Skill Name</label>
            <input
              type="text"
              className="form-control"
              placeholder="e.g., Python Programming, Graphic Design"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Description</label>
            <textarea
              className="form-control"
              rows="4"
              placeholder="Describe the skill you are offering."
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="btn btn-primary">Add Skill</button>
        </form>
      </div>
    </div>
  );
}

export default AddSkillPage;