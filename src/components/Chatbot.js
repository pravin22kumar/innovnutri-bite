import React, { useState, useEffect, useRef } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import { Button } from "../components/ui/Button";
import { useGemini } from "../hooks/useGemini";
import { db, doc, getDoc, updateDoc, arrayUnion } from "../firebase";

const Chatbot = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const chatboxRef = useRef(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const { fetchGeminiResponse, loading } = useGemini();

  useEffect(() => {
    if (!user) {
      navigate("/login");
    } else {
      const fetchChatHistory = async () => {
        const chatRef = doc(db, "users", user.uid);
        const chatSnap = await getDoc(chatRef);

        if (chatSnap.exists() && chatSnap.data().chatHistory.length > 0) {
          setMessages(chatSnap.data().chatHistory);
        } else {
          const initialMessage = {
            message: `Hello! I'm InnovNutri Bite AI Bot, your personal nutrition assistant. 
            To create a personalized meal plan, I'll need some details from you:
            - Age
            - Height
            - Weight
            - Dietary needs (vegetarian/non-vegetarian/vegan, allergies, etc.)
            - Lifestyle (sedentary, active, athletic)
            - Cultural preferences
            - Budget for food
            
            Please provide this information to get started!`,
            role: "bot",
          };
          setMessages([initialMessage]);

          if (user) {
            await updateDoc(chatRef, {
              chatHistory: arrayUnion(initialMessage),
            });
          }
        }
      };

      fetchChatHistory();
    }
  }, [user, navigate]);

  useEffect(() => {
    setTimeout(() => {
      chatboxRef.current?.scrollTo({
        top: chatboxRef.current.scrollHeight,
        behavior: "smooth",
      });
    }, 100);
  }, [messages]);

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", message: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    const botResponse = await fetchGeminiResponse(input);
    const botMessage = { role: "bot", message: botResponse };
    setMessages((prev) => [...prev, botMessage]);

    if (user) {
      const chatRef = doc(db, "users", user.uid);
      await updateDoc(chatRef, {
        chatHistory: arrayUnion(userMessage, botMessage),
      });
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSendMessage();
    }
  };

  return (
    <div className="w-full max-w-lg mx-auto mt-10 p-4 bg-white shadow-lg rounded-xl">
      <h2 className="text-2xl font-bold text-center text-green-600 mb-4">
        InnovNutri Bite Bot
      </h2>

      <div ref={chatboxRef} className="h-64 overflow-y-auto border p-2 rounded-lg bg-gray-100">
        {messages.map((msg, index) => (
          <div 
            key={index} 
            className={`p-2 my-1 break-words ${msg.role === "bot" ? "text-left" : "text-right"}`}
          >
            <span className={`px-3 py-2 rounded-lg inline-block max-w-[80%] ${msg.role === "bot" ? "bg-green-200" : "bg-blue-200"}`}>
              {msg.message}
            </span>
          </div>
        ))}
      </div>

      <div className="mt-4 flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Type your message..."
          className="flex-1 p-2 border rounded-l-lg focus:outline-none"
        />
        <Button 
          onClick={handleSendMessage} 
          className="bg-green-500 text-white px-4 py-2 rounded-r-lg"
          disabled={loading}
        >
          {loading ? "Loading..." : "Send"}
        </Button>
      </div>
    </div>
  );
};

export default Chatbot;
