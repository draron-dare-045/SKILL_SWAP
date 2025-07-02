// frontend/src/pages/HomePage.jsx
import React, { useState, useEffect } from 'react';
import api from '../api/axiosConfig';

function HomePage() {
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSkills = async () => {
      try {
        const response = await api.get('/skills/');
        setSkills(response.data);
      } catch (error) {
        console.error("Failed to fetch skills:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchSkills();
  }, []);

  if (loading) return <p>Loading skills...</p>;

  return (
    <div className="text-center">
        {/* The main star icon and title from your image */}
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style={{ width: '120px', height: '120px', color: '#ffc107', marginBottom: '1.5rem' }}>
            <path fillRule="evenodd" d="M10.788 3.21c.448-1.077 1.976-1.077 2.424 0l2.082 5.007 5.404.433c1.164.093 1.636 1.545.749 2.305l-4.116 3.986 1.257 5.273c.271 1.136-.964 2.033-1.96 1.425L12 18.354 7.373 21.18c-.996.608-2.231-.29-1.96-1.425l1.257-5.273-4.116-3.986c-.887-.76-.415-2.212.749-2.305l5.404-.433 2.082-5.007z" clipRule="evenodd" />
        </svg>
        <h1 style={{fontSize: '3.5rem', fontWeight: 700, color: '#3f51b5' }}>SkillSwap</h1>
        <p className="lead text-muted mb-5">Welcome to SkillSwap – Find and offer skills!</p>

        <hr />

        <h2 className="mt-5">Available Skills</h2>
        <div className="row mt-4">
            {skills.length > 0 ? skills.map(skill => (
                <div className="col-md-4 mb-4" key={skill.id}>
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">{skill.name}</h5>
                            <p className="card-text">{skill.description}</p>
                            <footer className="blockquote-footer mt-2">Offered by <cite title="Source Title">{skill.offered_by.username}</cite></footer>
                        </div>
                    </div>
                </div>
            )) : <p>No skills offered yet. Be the first!</p>}
        </div>
    </div>
  );
}
export default HomePage;