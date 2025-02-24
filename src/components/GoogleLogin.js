import React, { useEffect } from "react";
import { useAuth } from "../context/AuthContext";
import { useLocation, useNavigate } from "react-router-dom";

const GoogleLogin = () => {
  const { user, loginWithGoogle } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    if (user) {
      // Redirect to the service page the user was trying to access
      const redirectTo = location.state?.redirectTo || "/";
      navigate(`/${redirectTo}`);
    }
  }, [user, navigate, location.state]);

  return (
    <div className="h-screen flex flex-col justify-center items-center bg-gray-100">
      <h2 className="text-3xl font-bold text-green-600 mb-4">Login to Continue</h2>
      <button 
        onClick={loginWithGoogle} 
        className="bg-green-500 hover:bg-green-600 text-white px-6 py-3 rounded-lg text-lg"
      >
        Login with Google
      </button>
    </div>
  );
};

export default GoogleLogin;
