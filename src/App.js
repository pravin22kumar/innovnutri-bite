import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import HomePage from "./components/HomePage";
import ChatbotPage from "./components/ChatbotPage";
import GoogleLogin from "./components/GoogleLogin";
import MealPlannerPage from "./components/MealPlannerPage";
import CausesPage from "./components/causespage"; // Import Causes Page

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<GoogleLogin />} />
          <Route path="/chatbot" element={<ChatbotPage />} />
          <Route path="/mealplan" element={<MealPlannerPage />} />
          <Route path="/causes" element={<CausesPage />} />

          {/* 404: Redirect invalid URLs to Home */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
