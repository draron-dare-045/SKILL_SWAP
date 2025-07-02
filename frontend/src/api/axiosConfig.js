// frontend/src/api/axiosConfig.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://skill-swap-rx1l.onrender.com/api', // Your Flask backend URL
});

// Use an interceptor to add the auth token to every request
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;