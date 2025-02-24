import React from "react";
import { Link } from "react-router-dom";

const MealPlannerPage = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-cyan-700 to-green-500 flex flex-col items-center p-6">
      {/* Navigation Bar */}
      <nav className="w-full max-w-5xl bg-white shadow-lg rounded-xl p-4 flex justify-between items-center mb-8 border border-gray-300">
        <Link
          to="/"
          className="text-blue-700 font-semibold text-lg flex items-center space-x-2 transition duration-300 hover:text-blue-900 hover:scale-105"
        >
          <span className="text-xl">🏠</span>
          <span className="relative group">
            Home
            <span className="absolute left-0 w-0 h-0.5 bg-blue-700 transition-all duration-300 group-hover:w-full"></span>
          </span>
        </Link>
        <div className="space-x-6 flex">
          <Link
            to="/chatbot"
            className="relative text-blue-700 text-lg font-medium transition duration-300 hover:text-blue-900 hover:scale-105 group"
          >
            Chatbot
            <span className="absolute left-0 w-0 h-0.5 bg-blue-700 transition-all duration-300 group-hover:w-full"></span>
          </Link>
          <Link
            to="/causes"
            className="relative text-blue-700 text-lg font-medium transition duration-300 hover:text-blue-900 hover:scale-105 group"
          >
            Causes of Poor Nutrition
            <span className="absolute left-0 w-0 h-0.5 bg-blue-700 transition-all duration-300 group-hover:w-full"></span>
          </Link>
        </div>
      </nav>

      {/* Meal Planner Section */}
      <div className="w-full max-w-5xl bg-[#1A1A2E] text-white shadow-2xl rounded-2xl p-8 border border-cyan-400 relative">
        {/* Subtle Glowing Border */}
        <div className="absolute inset-0 border-2 border-cyan-500 opacity-20 rounded-2xl"></div>

        <h2 className="text-4xl font-extrabold text-cyan-300 text-center mb-6 tracking-wide">
          🍽️ Personalized Meal Planner
        </h2>
        <p className="text-lg text-gray-300 text-center mb-4">
          Get customized meal plans based on your dietary needs, budget, and preferences.
        </p>

        <div className="relative w-full h-[600px] border border-cyan-400 rounded-xl overflow-hidden shadow-lg bg-black">
          <iframe
            src="http://localhost:8501"
            className="w-full h-full"
            title="Meal Planner"
          />
        </div>
      </div>
    </div>
  );
};

export default MealPlannerPage;
