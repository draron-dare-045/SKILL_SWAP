// frontend/src/App.jsx
import { Routes, Route } from 'react-router-dom';
import { useAuth } from './context/AuthContext.jsx'; // <-- FIX HERE

import Header from './components/Header.jsx'; // Add .jsx
import ProtectedRoute from './components/ProtectedRoute.jsx'; // Add .jsx

import HomePage from './pages/HomePage.jsx'; // Add .jsx
import LoginPage from './pages/LoginPage.jsx'; // Add .jsx
import RegisterPage from './pages/RegisterPage.jsx'; // Add .jsx
import AddSkillPage from './pages/AddSkillPage.jsx'; // Add .jsx
import AdminDashboard from './pages/AdminDashboard.jsx'; // Add .jsx
import NotFoundPage from './pages/NotFoundPage.jsx'; // Add .jsx


function App() {
  const { isLoading } = useAuth();

  // Prevents flashing of protected content before auth state is loaded
  if (isLoading) {
    return <div className="d-flex justify-content-center align-items-center vh-100"><h2>Loading...</h2></div>;
  }

  return (
    <>
      <Header />
      <main className="container my-4">
        <Routes>
          {/* Public Routes */}
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />

          {/* Protected User Route */}
          <Route
            path="/add-skill"
            element={
              <ProtectedRoute>
                <AddSkillPage />
              </ProtectedRoute>
            }
          />

          {/* Protected Admin Route */}
          <Route
            path="/admin"
            element={
              <ProtectedRoute adminOnly={true}>
                <AdminDashboard />
              </ProtectedRoute>
            }
          />

          {/* Catch-all Not Found Route */}
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </main>
    </>
  );
}

export default App;