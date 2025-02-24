import React from "react";
import { Link } from "react-router-dom";

const CausesPage = () => {
    return (
        <div className="min-h-screen flex flex-col items-center bg-gradient-to-r from-green-300 via-blue-200 to-purple-300 p-6">
            <div className="w-full max-w-4xl bg-white shadow-2xl rounded-lg p-6 relative">

                {/* Navigation for Quick Scroll + Back Button */}
                <nav className="sticky top-0 bg-white shadow-md rounded-lg p-3 mb-4 flex justify-between items-center z-10">
                    <Link to="/" className="text-white bg-green-600 px-4 py-2 rounded-lg font-semibold hover:bg-green-700 transition duration-300">
                        ⬅ Back to Home
                    </Link>
                    <div className="flex space-x-6">
                        <a href="#importance" className="text-blue-600 font-semibold hover:underline">Importance</a>
                        <a href="#side-effects" className="text-red-600 font-semibold hover:underline">Side Effects</a>
                        <a href="#top-foods" className="text-green-600 font-semibold hover:underline">Protein-Rich Foods</a>
                    </div>
                </nav>

                <h2 className="text-4xl font-extrabold text-gray-900 text-center mb-6">
                    Causes of Poor Nutrition: <span className="text-blue-600">Focus on Protein Intake</span>
                </h2>

                {/* Section 1: Importance of Protein */}
                <section id="importance" className="mb-8 p-6 bg-blue-100 rounded-lg shadow-lg scroll-mt-20">
                    <h3 className="text-2xl font-bold text-gray-800 mb-3">🛡️ Importance of Protein</h3>
                    <p className="text-gray-700">
                        Protein is an essential macronutrient that supports muscle growth, tissue repair, and overall health.
                        It plays a critical role in enzyme and hormone production, immune function, and maintaining skin, hair, and nails.
                        Consuming adequate protein ensures strong metabolism and sustained energy levels throughout the day.
                    </p>
                </section>

                {/* Section 2: Side Effects of Low Protein Intake */}
                <section id="side-effects" className="mb-8 p-6 bg-red-100 rounded-lg shadow-lg scroll-mt-20">
                    <h3 className="text-2xl font-bold text-gray-800 mb-3">⚠️ Side Effects of Low Protein Intake</h3>
                    <p className="text-gray-700">
                        Insufficient protein intake can lead to muscle loss, fatigue, weakened immunity, and slow wound healing.
                        It can also cause hair thinning, brittle nails, and increased cravings for unhealthy foods.
                        In severe cases, protein deficiency can result in conditions like kwashiorkor, leading to swelling and stunted growth.
                    </p>
                </section>

                {/* Section 3: Top Protein-Rich Foods */}
                <section id="top-foods" className="mb-8 p-6 bg-green-100 rounded-lg shadow-lg scroll-mt-20">
                    <h3 className="text-2xl font-bold text-gray-800 mb-3">🥗 Top Protein-Rich Foods You Must Include</h3>
                    <ul className="list-disc pl-6">
                        <li><span className="font-semibold">Legumes & Beans</span> - Great plant-based protein alternatives.</li>
                        <li><span className="font-semibold">Quinoa</span> - A protein-packed superfood rich in fiber.</li>
                        <li><span className="font-semibold">Greek Yogurt</span> - A high-protein dairy option for gut health.</li>
                    </ul>
                </section>

            </div>
        </div>
    );
};

export default CausesPage;
