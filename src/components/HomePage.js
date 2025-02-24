import React from "react";
import { Link } from "react-scroll";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const { user, loginWithGoogle, logout } = useAuth();
  const navigate = useNavigate();

  const handleServiceClick = (service) => {
    if (!user) {
      navigate("/login", { state: { redirectTo: service } });
    } else {
      navigate(`/${service}`);
    }
  };

  return (
    <div className="w-full h-screen overflow-y-scroll snap-y snap-mandatory">
      {/* Navbar */}
      <nav className="fixed top-0 w-full bg-white shadow-md p-4 flex justify-between items-center z-50">
        <h1 className="text-2xl font-bold text-green-600">InnovNutri Bite</h1>
        <div className="flex items-center space-x-4">
          {user ? (
            <div className="flex items-center space-x-2">
              <img src={user.photoURL} alt="Profile" className="w-10 h-10 rounded-full" />
              <span className="text-gray-700">{user.displayName}</span>
              <button
                onClick={logout}
                className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition"
              >
                Logout
              </button>
            </div>
          ) : (
            <button
              onClick={loginWithGoogle}
              className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition"
            >
              Login with Google
            </button>
          )}
        </div>
      </nav>

      {/* Home Section */}
      <section id="home" className="h-screen flex flex-col justify-center items-center bg-blue-100 text-center p-6">
        <h2 className="text-5xl font-extrabold text-green-700">Welcome to InnovNutri Bite</h2>
        <p className="text-lg text-gray-700 mt-4 max-w-2xl">Your personalized guide to a healthier lifestyle.</p>
        <button
          onClick={() => handleServiceClick("chatbot")}
          className="mt-6 bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition"
        >
          Try Our AI Chatbot
        </button>
      </section>

      {/* About Section (Updated with a Service-like Look) */}
      <section id="about" className="h-screen flex flex-col justify-center items-center bg-gray-100 text-center p-6">
        <h2 className="text-4xl font-bold text-gray-800">About Us</h2>
        <p className="text-lg text-gray-700 mt-4 max-w-3xl">
          InnovNutri Bite helps you make informed nutrition decisions with AI-powered insights and personalized meal plans.
        </p>
        <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-6 bg-white shadow-lg rounded-2xl cursor-pointer hover:scale-105 transition transform hover:bg-green-100">
            <h3 className="text-lg font-semibold">💡 Our Mission</h3>
            <p className="text-gray-600 text-sm mt-2">To provide accessible and science-backed nutrition guidance for everyone.</p>
          </div>
          <div className="p-6 bg-white shadow-lg rounded-2xl cursor-pointer hover:scale-105 transition transform hover:bg-green-100">
            <h3 className="text-lg font-semibold">🛠️ How It Works</h3>
            <p className="text-gray-600 text-sm mt-2">We analyze your dietary needs and suggest AI-generated meal plans.</p>
          </div>
          <div className="p-6 bg-white shadow-lg rounded-2xl cursor-pointer hover:scale-105 transition transform hover:bg-green-100">
            <h3 className="text-lg font-semibold">📈 Why Choose Us?</h3>
            <p className="text-gray-600 text-sm mt-2">We integrate real-time grocery prices and AI insights for personalized nutrition.</p>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="h-screen flex flex-col justify-center items-center bg-yellow-100 text-center p-6">
        <h2 className="text-4xl font-bold text-yellow-800">Our Services</h2>
        <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div onClick={() => handleServiceClick("chatbot")} className="p-6 bg-white shadow-lg rounded-2xl cursor-pointer hover:scale-105 transition transform hover:bg-green-100">
            <h3 className="text-lg font-semibold">🤖 AI Nutrition Chatbot</h3>
            <p className="text-gray-600 text-sm mt-2">Get instant, AI-powered nutrition advice.</p>
          </div>
          <div onClick={() => handleServiceClick("causes")} className="p-6 bg-white shadow-lg rounded-2xl cursor-pointer hover:scale-105 transition transform hover:bg-green-100">
            <h3 className="text-lg font-semibold">📉 Causes of Poor Nutrition</h3>
            <p className="text-gray-600 text-sm mt-2">Learn the impact of poor dietary choices.</p>
          </div>
          <div onClick={() => handleServiceClick("mealplan")} className="p-6 bg-white shadow-lg rounded-2xl cursor-pointer hover:scale-105 transition transform hover:bg-green-100">
            <h3 className="text-lg font-semibold">🥗 Personalized Meal Plans</h3>
            <p className="text-gray-600 text-sm mt-2">Customized meal suggestions based on your needs.</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
