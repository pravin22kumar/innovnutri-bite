import React from "react";
import { Link } from "react-router-dom";
import Chatbot from "../components/Chatbot";

const ChatbotPage = () => {
  return (
    <div className="min-h-screen flex flex-col items-center p-6 bg-gradient-to-br from-green-100 via-yellow-100 to-orange-100">
      {/* Navigation Bar */}
      <nav className="w-full max-w-4xl bg-white shadow-lg rounded-xl p-4 flex justify-between items-center mb-6 border border-green-300">
        <Link to="/" className="text-green-700 font-semibold text-lg hover:text-green-900 transition duration-300">
          🏠 Home
        </Link>
        <div className="space-x-6">
          <Link to="/mealplan" className="text-orange-700 text-lg hover:text-orange-900 transition duration-300">
            🍽️ Meal Plan
          </Link>
          <Link to="/causes" className="text-blue-700 text-lg hover:text-blue-900 transition duration-300">
            📌 Causes of Poor Nutrition
          </Link>
        </div>
      </nav>

      {/* Chatbot Section */}
      <div className="w-full max-w-4xl bg-white shadow-2xl rounded-2xl p-8 border border-gray-200">
        <h2 className="text-4xl font-extrabold text-green-700 text-center mb-6">
          🍏 InnovNutri Bite 🍏
        </h2>
        <Chatbot />
      </div>
    </div>
  );
};

export default ChatbotPage;
