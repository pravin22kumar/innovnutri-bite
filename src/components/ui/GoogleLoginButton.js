import React from "react";
import { useAuth } from "../../context/AuthContext";
import { useNavigate } from "react-router-dom";

const GoogleLoginButton = () => {
  const { loginWithGoogle } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async () => {
    await loginWithGoogle();
    navigate("/services"); // Redirect to services after login
  };

  return (
    <button onClick={handleLogin} className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg">
      Login with Google
    </button>
  );
};

export default GoogleLoginButton;
