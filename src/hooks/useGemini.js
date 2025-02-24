import { useState } from "react";
import axios from "axios";

const GEMINI_API_KEY = process.env.REACT_APP_GEMINI_API_KEY || "";

if (!GEMINI_API_KEY) {
  console.error("❌ ERROR: Gemini API Key is missing. Check your .env file!");
}

export const useGemini = () => {
  const [loading, setLoading] = useState(false);
  const [conversationHistory, setConversationHistory] = useState([]);

  const fetchGeminiResponse = async (userMessage) => {
    setLoading(true);
    console.log("✅ User Message:", userMessage);

    try {
      if (!GEMINI_API_KEY) {
        throw new Error("API Key is missing. Set it in the .env file.");
      }

      // 🛑 FIX: Ensure conversation history is formatted correctly
      const updatedHistory = [
        ...conversationHistory.map((msg) => ({
          role: msg.role,
          parts: msg.parts
        })),
        { role: "user", parts: [{ text: userMessage }] }
      ];

      const requestBody = {
        contents: updatedHistory
      };

      console.log("📩 Request Payload:", JSON.stringify(requestBody, null, 2));

      // 🔹 API Call
      const response = await axios.post(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${GEMINI_API_KEY}`,
        requestBody,
        { headers: { "Content-Type": "application/json" } }
      );

      console.log("✅ Full API Response:", response.data);

      const botResponse =
        response.data?.candidates?.[0]?.content?.parts?.[0]?.text ||
        "Sorry, I couldn't generate a response.";

      // ✅ FIX: Store correct conversation format
      setConversationHistory((prev) => [
        ...prev,
        { role: "user", parts: [{ text: userMessage }] },
        { role: "model", parts: [{ text: botResponse }] } // Use "model" instead of "bot"
      ]);

      return botResponse;
    } catch (error) {
      console.error("❌ Gemini API Error:", error.response?.data || error.message);
      return "Sorry, I encountered an error while processing your request.";
    } finally {
      setLoading(false);
    }
  };

  return { fetchGeminiResponse, loading };
};
