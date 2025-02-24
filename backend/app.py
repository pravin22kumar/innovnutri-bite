import streamlit as st
import pandas as pd
import json
from datetime import datetime
if st.button("🔙 Back to InnovNutriBite"):
    st.markdown('<meta http-equiv="refresh" content="0;URL=\'https://innovnutribite.web.app/\'" />', unsafe_allow_html=True)

# Load food database
def load_food_database():
    return {
        "USA": {
            "breakfast": {
                "balanced": [
                    {
                        "name": "Avocado Toast with Eggs",
                        "calories": 450,
                        "protein": 20,
                        "carbs": 50,
                        "fats": 18,
                        "ingredients": ["whole wheat bread", "avocado", "eggs", "olive oil", "pepper"]
                    },
                    {
                        "name": "Greek Yogurt Parfait",
                        "calories": 400,
                        "protein": 22,
                        "carbs": 55,
                        "fats": 10,
                        "ingredients": ["Greek yogurt", "granola", "blueberries", "honey"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Oatmeal with Nuts & Fruits",
                        "calories": 400,
                        "protein": 15,
                        "carbs": 55,
                        "fats": 12,
                        "ingredients": ["oats", "almond milk", "bananas", "walnuts", "honey"]
                    },
                    {
                        "name": "Vegetable Scramble",
                        "calories": 380,
                        "protein": 20,
                        "carbs": 30,
                        "fats": 18,
                        "ingredients": ["eggs", "bell peppers", "spinach", "cheese"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Smoothie Bowl",
                        "calories": 350,
                        "protein": 12,
                        "carbs": 60,
                        "fats": 8,
                        "ingredients": ["banana", "strawberries", "almond butter", "chia seeds", "oat milk"]
                    },
                    {
                        "name": "Tofu Scramble",
                        "calories": 400,
                        "protein": 22,
                        "carbs": 30,
                        "fats": 15,
                        "ingredients": ["tofu", "turmeric", "onions", "spinach", "mushrooms"]
                    }
                ],
                "keto": [
                    {
                        "name": "Scrambled Eggs with Avocado",
                        "calories": 500,
                        "protein": 22,
                        "carbs": 10,
                        "fats": 40,
                        "ingredients": ["eggs", "avocado", "cheese", "butter"]
                    },
                    {
                        "name": "Bacon & Cheese Omelet",
                        "calories": 550,
                        "protein": 30,
                        "carbs": 5,
                        "fats": 45,
                        "ingredients": ["eggs", "bacon", "cheese", "butter"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein Pancakes",
                        "calories": 500,
                        "protein": 35,
                        "carbs": 45,
                        "fats": 10,
                        "ingredients": ["oats", "whey protein", "almond milk", "eggs"]
                    },
                    {
                        "name": "Chicken & Egg Breakfast Bowl",
                        "calories": 550,
                        "protein": 40,
                        "carbs": 35,
                        "fats": 20,
                        "ingredients": ["chicken breast", "eggs", "spinach", "sweet potatoes"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Egg & Cheese Muffins",
                        "calories": 400,
                        "protein": 30,
                        "carbs": 10,
                        "fats": 25,
                        "ingredients": ["eggs", "cheese", "spinach", "mushrooms"]
                    },
                    {
                        "name": "Avocado & Salmon Roll",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 8,
                        "fats": 30,
                        "ingredients": ["avocado", "smoked salmon", "cream cheese", "lettuce wrap"]
                    }
                ]
            },"lunch": {
                "balanced": [
                    {
                        "name": "Grilled Chicken Salad",
                        "calories": 600,
                        "protein": 40,
                        "carbs": 50,
                        "fats": 15,
                        "ingredients": ["chicken breast", "lettuce", "tomatoes", "avocado", "vinaigrette"]
                    },
                    {
                        "name": "Quinoa & Veggie Bowl",
                        "calories": 550,
                        "protein": 25,
                        "carbs": 65,
                        "fats": 10,
                        "ingredients": ["quinoa", "chickpeas", "zucchini", "peppers", "olive oil"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Caprese Salad with Whole Wheat Bread",
                        "calories": 500,
                        "protein": 20,
                        "carbs": 55,
                        "fats": 18,
                        "ingredients": ["mozzarella", "tomatoes", "basil", "whole wheat bread", "balsamic glaze"]
                    },
                    {
                        "name": "Lentil Soup with Brown Rice",
                        "calories": 550,
                        "protein": 25,
                        "carbs": 70,
                        "fats": 10,
                        "ingredients": ["lentils", "carrots", "celery", "garlic", "brown rice"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Chickpea & Avocado Wrap",
                        "calories": 520,
                        "protein": 22,
                        "carbs": 65,
                        "fats": 15,
                        "ingredients": ["whole wheat wrap", "chickpeas", "avocado", "lettuce", "hummus"]
                    },
                    {
                        "name": "Quinoa & Black Bean Bowl",
                        "calories": 500,
                        "protein": 20,
                        "carbs": 60,
                        "fats": 12,
                        "ingredients": ["quinoa", "black beans", "corn", "tomatoes", "cilantro"]
                    }
                ],
                "keto": [
                    {
                        "name": "Caesar Salad with Grilled Chicken",
                        "calories": 550,
                        "protein": 40,
                        "carbs": 10,
                        "fats": 35,
                        "ingredients": ["romaine lettuce", "chicken breast", "parmesan", "Caesar dressing"]
                    },
                    {
                        "name": "Zucchini Noodles with Pesto & Shrimp",
                        "calories": 500,
                        "protein": 35,
                        "carbs": 8,
                        "fats": 30,
                        "ingredients": ["zucchini noodles", "shrimp", "pesto", "pine nuts", "olive oil"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Turkey & Quinoa Stuffed Peppers",
                        "calories": 600,
                        "protein": 50,
                        "carbs": 45,
                        "fats": 15,
                        "ingredients": ["ground turkey", "quinoa", "bell peppers", "tomatoes", "cheese"]
                    },
                    {
                        "name": "Grilled Salmon with Asparagus",
                        "calories": 650,
                        "protein": 55,
                        "carbs": 30,
                        "fats": 25,
                        "ingredients": ["salmon", "asparagus", "butter", "garlic"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Egg Salad Lettuce Wraps",
                        "calories": 450,
                        "protein": 30,
                        "carbs": 10,
                        "fats": 30,
                        "ingredients": ["eggs", "mayonnaise", "lettuce", "mustard"]
                    },
                    {
                        "name": "Chicken Stir-Fry with Cauliflower Rice",
                        "calories": 500,
                        "protein": 45,
                        "carbs": 15,
                        "fats": 20,
                        "ingredients": ["chicken", "broccoli", "cauliflower rice", "soy sauce"]
                    }
                ]
            },
            "dinner": {
                "balanced": [
                    {
                        "name": "Salmon with Quinoa",
                        "calories": 650,
                        "protein": 45,
                        "carbs": 50,
                        "fats": 20,
                        "ingredients": ["salmon", "quinoa", "spinach", "olive oil"]
                    },
                    {
                        "name": "Steak with Roasted Vegetables",
                        "calories": 700,
                        "protein": 50,
                        "carbs": 40,
                        "fats": 30,
                        "ingredients": ["steak", "carrots", "broccoli", "garlic butter"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Stuffed Bell Peppers with Rice & Beans",
                        "calories": 600,
                        "protein": 25,
                        "carbs": 70,
                        "fats": 12,
                        "ingredients": ["bell peppers", "black beans", "brown rice", "cheese", "tomatoes"]
                    },
                    {
                        "name": "Mushroom Risotto",
                        "calories": 650,
                        "protein": 20,
                        "carbs": 80,
                        "fats": 15,
                        "ingredients": ["arborio rice", "mushrooms", "parmesan", "garlic", "butter"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Lentil & Sweet Potato Curry",
                        "calories": 600,
                        "protein": 22,
                        "carbs": 75,
                        "fats": 10,
                        "ingredients": ["lentils", "sweet potatoes", "coconut milk", "curry powder"]
                    },
                    {
                        "name": "Tofu Stir-Fry with Brown Rice",
                        "calories": 550,
                        "protein": 25,
                        "carbs": 65,
                        "fats": 12,
                        "ingredients": ["tofu", "broccoli", "bell peppers", "brown rice", "soy sauce"]
                    }
                ],
                "keto": [
                    {
                        "name": "Grilled Ribeye with Garlic Butter",
                        "calories": 700,
                        "protein": 55,
                        "carbs": 5,
                        "fats": 50,
                        "ingredients": ["ribeye steak", "butter", "garlic", "rosemary"]
                    },
                    {
                        "name": "Baked Salmon with Creamed Spinach",
                        "calories": 650,
                        "protein": 50,
                        "carbs": 8,
                        "fats": 40,
                        "ingredients": ["salmon", "spinach", "cream cheese", "butter"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Grilled Chicken with Brown Rice",
                        "calories": 700,
                        "protein": 60,
                        "carbs": 50,
                        "fats": 15,
                        "ingredients": ["chicken breast", "brown rice", "green beans"]
                    },
                    {
                        "name": "Beef & Sweet Potato Hash",
                        "calories": 650,
                        "protein": 50,
                        "carbs": 55,
                        "fats": 15,
                        "ingredients": ["ground beef", "sweet potatoes", "onions", "garlic"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Garlic Butter Shrimp with Zucchini Noodles",
                        "calories": 500,
                        "protein": 40,
                        "carbs": 10,
                        "fats": 30,
                        "ingredients": ["shrimp", "zucchini noodles", "butter", "garlic"]
                    },
                    {
                        "name": "Baked Chicken Thighs with Roasted Brussels Sprouts",
                        "calories": 600,
                        "protein": 50,
                        "carbs": 15,
                        "fats": 35,
                        "ingredients": ["chicken thighs", "brussels sprouts", "olive oil", "parmesan"]
                    }
                ]
            }
        
        },
        "India": {
            "breakfast": {
                "balanced": [
                    {
                        "name": "South Indian Breakfast Platter",
                        "calories": 550,
                        "protein": 18,
                        "carbs": 75,
                        "fats": 22,
                        "ingredients": ["idli", "dosa", "sambar", "coconut chutney", "upma", "filter coffee"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "North Indian Breakfast Combo",
                        "calories": 680,
                        "protein": 22,
                        "carbs": 85,
                        "fats": 28,
                        "ingredients": ["paratha", "chole", "yogurt", "pickle", "butter", "chai"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Poha with Sprouts",
                        "calories": 420,
                        "protein": 15,
                        "carbs": 65,
                        "fats": 12,
                        "ingredients": ["flattened rice", "peanuts", "sprouts", "onions", "curry leaves", "lemon"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Power Packed Uttapam",
                        "calories": 580,
                        "protein": 20,
                        "carbs": 75,
                        "fats": 18,
                        "ingredients": ["rice batter", "urad dal", "vegetables", "sambar", "chutney", "ghee"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Indian Breakfast Bowl",
                        "calories": 450,
                        "protein": 16,
                        "carbs": 70,
                        "fats": 15,
                        "ingredients": ["ragi dosa", "vegetable curry", "coconut chutney", "sprouts", "fruit"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "High Energy Vegan Platter",
                        "calories": 580,
                        "protein": 20,
                        "carbs": 80,
                        "fats": 18,
                        "ingredients": ["quinoa upma", "chickpea curry", "tofu scramble", "almond milk", "dates"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Indian Breakfast",
                        "calories": 550,
                        "protein": 30,
                        "carbs": 8,
                        "fats": 45,
                        "ingredients": ["paneer bhurji", "almond flour roti", "coconut chutney", "butter coffee"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Low Carb Indian Start",
                        "calories": 620,
                        "protein": 35,
                        "carbs": 10,
                        "fats": 48,
                        "ingredients": ["egg bhurji", "cheese", "avocado", "coconut curry", "bulletproof chai"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein Rich Indian Breakfast",
                        "calories": 650,
                        "protein": 45,
                        "carbs": 55,
                        "fats": 25,
                        "ingredients": ["egg curry", "paneer paratha", "greek yogurt", "sprouts salad", "whey shake"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Power Protein Platter",
                        "calories": 720,
                        "protein": 50,
                        "carbs": 60,
                        "fats": 28,
                        "ingredients": ["chicken tikka", "egg whites", "moong dal cheela", "protein smoothie"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low Carb Indian Start",
                        "calories": 480,
                        "protein": 35,
                        "carbs": 15,
                        "fats": 32,
                        "ingredients": ["cauliflower upma", "paneer bhurji", "coconut chutney", "almond milk coffee"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "lunch": {
                "balanced": [
                    {
                        "name": "Traditional Indian Thali",
                        "calories": 750,
                        "protein": 25,
                        "carbs": 90,
                        "fats": 30,
                        "ingredients": ["roti", "dal", "rice", "sabzi", "raita", "pickle"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Deluxe Indian Platter",
                        "calories": 950,
                        "protein": 35,
                        "carbs": 110,
                        "fats": 38,
                        "ingredients": ["biryani", "dal makhani", "naan", "paneer curry", "raita", "dessert"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Veggie Special Thali",
                        "calories": 680,
                        "protein": 22,
                        "carbs": 85,
                        "fats": 28,
                        "ingredients": ["pulao", "dal tadka", "paneer curry", "roti", "raita", "salad"],
                        "activity_level": ["All"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Indian Lunch",
                        "calories": 620,
                        "protein": 20,
                        "carbs": 80,
                        "fats": 25,
                        "ingredients": ["brown rice", "chickpea curry", "tofu curry", "roti", "salad"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Indian Lunch",
                        "calories": 650,
                        "protein": 40,
                        "carbs": 12,
                        "fats": 50,
                        "ingredients": ["chicken curry", "cauliflower rice", "spinach paneer", "avocado raita"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein Packed Indian Lunch",
                        "calories": 780,
                        "protein": 55,
                        "carbs": 65,
                        "fats": 35,
                        "ingredients": ["chicken tikka", "paneer curry", "dal", "roti", "greek yogurt"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low Carb Indian Lunch",
                        "calories": 580,
                        "protein": 35,
                        "carbs": 20,
                        "fats": 42,
                        "ingredients": ["chicken curry", "paneer bhurji", "cauliflower rice", "cucumber raita"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "dinner": {
                "balanced": [
                    {
                        "name": "Light Indian Dinner",
                        "calories": 650,
                        "protein": 22,
                        "carbs": 80,
                        "fats": 25,
                        "ingredients": ["dal", "roti", "vegetable curry", "rice", "raita", "salad"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Royal Indian Dinner",
                        "calories": 850,
                        "protein": 30,
                        "carbs": 95,
                        "fats": 35,
                        "ingredients": ["butter chicken", "naan", "pulao", "dal makhani", "raita", "dessert"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Night Platter",
                        "calories": 600,
                        "protein": 20,
                        "carbs": 75,
                        "fats": 25,
                        "ingredients": ["paneer tikka", "roti", "jeera rice", "dal", "raita", "salad"],
                        "activity_level": ["All"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Indian Dinner",
                        "calories": 550,
                        "protein": 18,
                        "carbs": 70,
                        "fats": 22,
                        "ingredients": ["tofu curry", "roti", "brown rice", "mixed vegetable curry", "salad"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Indian Night Meal",
                        "calories": 600,
                        "protein": 35,
                        "carbs": 10,
                        "fats": 48,
                        "ingredients": ["tandoori chicken", "paneer curry", "cauliflower rice", "spinach"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "High Protein Indian Dinner",
                        "calories": 700,
                        "protein": 50,
                        "carbs": 55,
                        "fats": 30,
                        "ingredients": ["grilled chicken", "egg curry", "dal", "roti", "greek yogurt"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low Carb Indian Dinner",
                        "calories": 550,
                        "protein": 35,
                        "carbs": 18,
                        "fats": 40,
                        "ingredients": ["chicken tikka", "paneer curry", "cauliflower rice", "green salad"],
                        "activity_level": ["All"]
                    }
                ]
            }
        },
        
        "Japan": {
            "breakfast": {
                "balanced": [
                    {
                        "name": "Traditional Japanese Breakfast Set",
                        "calories": 500,
                        "protein": 25,
                        "carbs": 65,
                        "fats": 15,
                        "ingredients": ["steamed rice", "grilled salmon", "miso soup", "natto", "pickled vegetables"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Enhanced Japanese Breakfast",
                        "calories": 650,
                        "protein": 35,
                        "carbs": 75,
                        "fats": 20,
                        "ingredients": ["brown rice", "mackerel", "miso soup", "tamagoyaki", "seaweed salad", "tofu"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Japanese Morning Bowl",
                        "calories": 450,
                        "protein": 18,
                        "carbs": 70,
                        "fats": 12,
                        "ingredients": ["brown rice", "grilled tofu", "vegetable miso soup", "seaweed", "pickled vegetables"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "High Energy Vegan Japanese Breakfast",
                        "calories": 600,
                        "protein": 25,
                        "carbs": 85,
                        "fats": 18,
                        "ingredients": ["quinoa", "tempeh", "mushroom soup", "avocado", "edamame", "nori"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Japanese Breakfast",
                        "calories": 480,
                        "protein": 20,
                        "carbs": 75,
                        "fats": 15,
                        "ingredients": ["rice", "tamagoyaki", "vegetable miso soup", "tofu", "Japanese pickles"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Power Vegetarian Japanese Bowl",
                        "calories": 620,
                        "protein": 28,
                        "carbs": 85,
                        "fats": 20,
                        "ingredients": ["brown rice", "egg", "tofu steak", "seaweed salad", "mushrooms", "miso soup"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Japanese Breakfast",
                        "calories": 550,
                        "protein": 35,
                        "carbs": 10,
                        "fats": 42,
                        "ingredients": ["grilled mackerel", "onsen egg", "avocado", "nori", "shirataki noodles"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "High Energy Keto Japanese Morning",
                        "calories": 700,
                        "protein": 45,
                        "carbs": 12,
                        "fats": 55,
                        "ingredients": ["salmon sashimi", "eggs", "avocado", "chicken tsukune", "keto miso soup"],
                        "activity_level": ["Very Active", "Extra Active"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein-Rich Japanese Breakfast",
                        "calories": 600,
                        "protein": 45,
                        "carbs": 45,
                        "fats": 25,
                        "ingredients": ["grilled fish", "egg whites", "tofu", "natto", "low-fat milk"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Athletic Japanese Morning",
                        "calories": 750,
                        "protein": 55,
                        "carbs": 60,
                        "fats": 30,
                        "ingredients": ["salmon", "egg whites", "protein-enriched rice", "tofu", "edamame"],
                        "activity_level": ["Very Active", "Extra Active"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low-Carb Japanese Start",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 15,
                        "fats": 30,
                        "ingredients": ["grilled fish", "egg", "tofu", "seaweed salad", "shirataki noodles"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "lunch": {
                "balanced": [
                    {
                        "name": "Traditional Bento Box",
                        "calories": 600,
                        "protein": 30,
                        "carbs": 75,
                        "fats": 20,
                        "ingredients": ["rice", "grilled chicken", "vegetables", "egg roll", "miso soup"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Deluxe Japanese Lunch Set",
                        "calories": 800,
                        "protein": 40,
                        "carbs": 90,
                        "fats": 25,
                        "ingredients": ["brown rice", "salmon teriyaki", "soba noodles", "tempura", "miso soup"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Japanese Lunch Bowl",
                        "calories": 550,
                        "protein": 20,
                        "carbs": 80,
                        "fats": 18,
                        "ingredients": ["brown rice", "tofu teriyaki", "vegetable tempura", "seaweed salad", "miso soup"],
                        "activity_level": ["All"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Bento",
                        "calories": 580,
                        "protein": 25,
                        "carbs": 75,
                        "fats": 20,
                        "ingredients": ["rice", "egg", "vegetable tempura", "tofu", "pickled vegetables"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Japanese Lunch Plate",
                        "calories": 650,
                        "protein": 45,
                        "carbs": 12,
                        "fats": 48,
                        "ingredients": ["sashimi assortment", "avocado", "shirataki noodles", "egg", "seaweed salad"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein-Packed Japanese Lunch",
                        "calories": 700,
                        "protein": 55,
                        "carbs": 50,
                        "fats": 30,
                        "ingredients": ["chicken katsu", "tofu", "egg", "edamame", "protein rice"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low-Carb Japanese Lunch Set",
                        "calories": 500,
                        "protein": 40,
                        "carbs": 20,
                        "fats": 35,
                        "ingredients": ["grilled mackerel", "tofu", "vegetable stir-fry", "shirataki noodles", "miso soup"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "dinner": {
                "balanced": [
                    {
                        "name": "Traditional Japanese Dinner",
                        "calories": 650,
                        "protein": 35,
                        "carbs": 80,
                        "fats": 22,
                        "ingredients": ["rice", "grilled fish", "vegetables", "miso soup", "pickled sides"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Deluxe Japanese Dinner Set",
                        "calories": 850,
                        "protein": 45,
                        "carbs": 95,
                        "fats": 30,
                        "ingredients": ["rice", "sukiyaki", "sashimi", "tempura", "miso soup"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Japanese Dinner",
                        "calories": 580,
                        "protein": 25,
                        "carbs": 85,
                        "fats": 20,
                        "ingredients": ["brown rice", "vegetable tempura", "mushroom soup", "tofu steak", "seaweed salad"],
                        "activity_level": ["All"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Japanese Evening Meal",
                        "calories": 600,
                        "protein": 28,
                        "carbs": 80,
                        "fats": 22,
                        "ingredients": ["rice", "vegetable curry", "tofu", "vegetable tempura", "miso soup"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Japanese Dinner",
                        "calories": 700,
                        "protein": 48,
                        "carbs": 15,
                        "fats": 52,
                        "ingredients": ["sashimi platter", "keto tempura", "shirataki noodles", "avocado", "miso soup"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "High-Protein Japanese Dinner",
                        "calories": 750,
                        "protein": 60,
                        "carbs": 55,
                        "fats": 35,
                        "ingredients": ["grilled chicken", "fish", "tofu", "egg", "edamame"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low-Carb Japanese Evening Plate",
                        "calories": 550,
                        "protein": 45,
                        "carbs": 20,
                        "fats": 38,
                        "ingredients": ["sashimi", "grilled chicken", "tofu", "shirataki noodles", "vegetable stir-fry"],
                        "activity_level": ["All"]
                    }
                ]
            }
        },
        "Italy": {
            "breakfast": {
                "balanced": [
                    {
                        "name": "Classic Italian Breakfast",
                        "calories": 380,
                        "protein": 12,
                        "carbs": 55,
                        "fats": 16,
                        "ingredients": ["whole grain cornetto", "cappuccino", "fresh fruits", "honey", "yogurt"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Energetic Italian Start",
                        "calories": 520,
                        "protein": 18,
                        "carbs": 65,
                        "fats": 22,
                        "ingredients": ["ricotta toast", "fresh oranges", "nuts", "whole grain bread", "olive oil"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Italian Morning",
                        "calories": 420,
                        "protein": 15,
                        "carbs": 60,
                        "fats": 18,
                        "ingredients": ["plant-based yogurt", "granola", "fresh figs", "almond milk", "chia seeds"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Power Vegan Colazione",
                        "calories": 550,
                        "protein": 20,
                        "carbs": 75,
                        "fats": 22,
                        "ingredients": ["overnight oats", "plant milk", "banana", "almond butter", "hemp seeds"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Breakfast Plate",
                        "calories": 450,
                        "protein": 18,
                        "carbs": 58,
                        "fats": 20,
                        "ingredients": ["ricotta cheese", "honey", "whole grain bread", "fresh fruit", "nuts"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Active Vegetarian Start",
                        "calories": 600,
                        "protein": 25,
                        "carbs": 70,
                        "fats": 28,
                        "ingredients": ["greek yogurt", "granola", "dried fruits", "honey", "mixed nuts"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "keto": [
                    {
                        "name": "Italian Keto Breakfast",
                        "calories": 550,
                        "protein": 30,
                        "carbs": 8,
                        "fats": 45,
                        "ingredients": ["frittata", "mozzarella", "spinach", "olive oil", "mushrooms"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "High Energy Keto Start",
                        "calories": 650,
                        "protein": 35,
                        "carbs": 10,
                        "fats": 55,
                        "ingredients": ["eggs", "prosciutto", "avocado", "olives", "keto bread"],
                        "activity_level": ["Very Active", "Extra Active"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein Rich Italian Morning",
                        "calories": 580,
                        "protein": 42,
                        "carbs": 45,
                        "fats": 25,
                        "ingredients": ["egg whites", "ricotta", "protein bread", "turkey", "spinach"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Athletic Italian Breakfast",
                        "calories": 680,
                        "protein": 50,
                        "carbs": 55,
                        "fats": 28,
                        "ingredients": ["protein pancakes", "greek yogurt", "cottage cheese", "nuts", "berries"],
                        "activity_level": ["Very Active", "Extra Active"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low Carb Italian Start",
                        "calories": 480,
                        "protein": 28,
                        "carbs": 15,
                        "fats": 35,
                        "ingredients": ["eggs", "mozzarella", "tomatoes", "basil", "olive oil"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "lunch": {
                "balanced": [
                    {
                        "name": "Classic Italian Lunch",
                        "calories": 650,
                        "protein": 28,
                        "carbs": 75,
                        "fats": 25,
                        "ingredients": ["whole grain pasta", "tomato sauce", "parmesan", "vegetables", "olive oil"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Mediterranean Power Lunch",
                        "calories": 850,
                        "protein": 35,
                        "carbs": 90,
                        "fats": 35,
                        "ingredients": ["farro", "grilled fish", "vegetables", "legumes", "olive oil"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Italian Plate",
                        "calories": 580,
                        "protein": 22,
                        "carbs": 75,
                        "fats": 24,
                        "ingredients": ["lentil pasta", "marinara sauce", "vegetables", "nutritional yeast", "olive oil"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Energetic Vegan Italian",
                        "calories": 720,
                        "protein": 28,
                        "carbs": 90,
                        "fats": 30,
                        "ingredients": ["quinoa", "chickpeas", "grilled vegetables", "pine nuts", "pesto"],
                        "activity_level": ["Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Italian Lunch",
                        "calories": 620,
                        "protein": 25,
                        "carbs": 80,
                        "fats": 22,
                        "ingredients": ["pasta", "mushrooms", "parmesan", "vegetables", "truffle oil"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Italian Bowl",
                        "calories": 650,
                        "protein": 35,
                        "carbs": 12,
                        "fats": 52,
                        "ingredients": ["zucchini noodles", "meatballs", "low-carb marinara", "mozzarella", "olive oil"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein Packed Italian",
                        "calories": 680,
                        "protein": 45,
                        "carbs": 55,
                        "fats": 30,
                        "ingredients": ["chicken breast", "quinoa", "pesto", "mozzarella", "vegetables"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low Carb Italian Feast",
                        "calories": 550,
                        "protein": 35,
                        "carbs": 20,
                        "fats": 38,
                        "ingredients": ["grilled chicken", "eggplant", "zucchini", "mozzarella", "pesto"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "dinner": {
                "balanced": [
                    {
                        "name": "Traditional Italian Dinner",
                        "calories": 720,
                        "protein": 32,
                        "carbs": 85,
                        "fats": 28,
                        "ingredients": ["risotto", "grilled fish", "vegetables", "parmesan", "olive oil"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Active Italian Evening",
                        "calories": 880,
                        "protein": 40,
                        "carbs": 95,
                        "fats": 35,
                        "ingredients": ["whole grain pasta", "seafood", "vegetables", "garlic bread", "olive oil"],
                        "activity_level": ["Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Italian Night",
                        "calories": 620,
                        "protein": 25,
                        "carbs": 80,
                        "fats": 26,
                        "ingredients": ["lentil pasta", "vegetable ragu", "cashew cheese", "vegetables", "herbs"],
                        "activity_level": ["All"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Italian Evening",
                        "calories": 680,
                        "protein": 28,
                        "carbs": 85,
                        "fats": 25,
                        "ingredients": ["eggplant parmesan", "quinoa", "mozzarella", "vegetables", "tomato sauce"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Italian Dinner",
                        "calories": 700,
                        "protein": 40,
                        "carbs": 15,
                        "fats": 55,
                        "ingredients": ["chicken cacciatore", "cauliflower rice", "mozzarella", "olives", "olive oil"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "High Protein Italian Night",
                        "calories": 750,
                        "protein": 55,
                        "carbs": 45,
                        "fats": 35,
                        "ingredients": ["grilled steak", "beans", "parmesan", "vegetables", "olive oil"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low Carb Italian Evening",
                        "calories": 600,
                        "protein": 38,
                        "carbs": 18,
                        "fats": 42,
                        "ingredients": ["fish", "grilled vegetables", "pesto", "olives", "olive oil"],
                        "activity_level": ["All"]
                    }
                ]
            }
        },
        "Mexico": {
            "breakfast": {
                "balanced": [
                    {
                        "name": "Huevos Rancheros",
                        "calories": 550,
                        "protein": 25,
                        "carbs": 45,
                        "fats": 28,
                        "ingredients": ["corn tortillas", "eggs", "black beans", "salsa roja", "avocado", "queso fresco"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Chilaquiles Verdes",
                        "calories": 680,
                        "protein": 30,
                        "carbs": 65,
                        "fats": 35,
                        "ingredients": ["corn tortillas", "salsa verde", "chicken", "crema", "queso fresco", "onions"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Enfrijoladas",
                        "calories": 450,
                        "protein": 18,
                        "carbs": 60,
                        "fats": 20,
                        "ingredients": ["corn tortillas", "refried beans", "queso fresco", "crema", "avocado", "lettuce"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Mexican Breakfast Quesadillas",
                        "calories": 580,
                        "protein": 22,
                        "carbs": 65,
                        "fats": 28,
                        "ingredients": ["flour tortillas", "cheese", "mushrooms", "peppers", "onions", "guacamole"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Tofu Scramble Tacos",
                        "calories": 420,
                        "protein": 20,
                        "carbs": 45,
                        "fats": 22,
                        "ingredients": ["corn tortillas", "tofu", "black beans", "nutritional yeast", "avocado", "salsa"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Mexican Breakfast Bowl",
                        "calories": 550,
                        "protein": 25,
                        "carbs": 70,
                        "fats": 25,
                        "ingredients": ["quinoa", "black beans", "tempeh", "avocado", "pico de gallo", "corn"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "keto": [
                    {
                        "name": "Mexican Keto Bowl",
                        "calories": 550,
                        "protein": 35,
                        "carbs": 8,
                        "fats": 45,
                        "ingredients": ["eggs", "avocado", "cheese", "chorizo", "bell peppers", "sour cream"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Keto Breakfast Fajitas",
                        "calories": 620,
                        "protein": 40,
                        "carbs": 10,
                        "fats": 48,
                        "ingredients": ["eggs", "steak", "cheese", "bell peppers", "onions", "guacamole"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Mexican Protein Platter",
                        "calories": 650,
                        "protein": 45,
                        "carbs": 35,
                        "fats": 35,
                        "ingredients": ["egg whites", "chicken breast", "black beans", "cottage cheese", "pico de gallo"],
                        "activity_level": ["All"]
                    },
                    {
                        "name": "Protein-Packed Breakfast Burrito",
                        "calories": 720,
                        "protein": 50,
                        "carbs": 45,
                        "fats": 38,
                        "ingredients": ["eggs", "turkey chorizo", "black beans", "cheese", "greek yogurt", "salsa"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low-Carb Mexican Skillet",
                        "calories": 480,
                        "protein": 35,
                        "carbs": 15,
                        "fats": 32,
                        "ingredients": ["eggs", "chorizo", "cheese", "avocado", "peppers", "sour cream"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "lunch": {
                "balanced": [
                    {
                        "name": "Chicken Fajita Bowl",
                        "calories": 650,
                        "protein": 35,
                        "carbs": 65,
                        "fats": 28,
                        "ingredients": ["rice", "chicken", "bell peppers", "onions", "beans", "guacamole"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Carne Asada Plate",
                        "calories": 850,
                        "protein": 45,
                        "carbs": 75,
                        "fats": 35,
                        "ingredients": ["steak", "rice", "beans", "tortillas", "pico de gallo", "guacamole"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetarian Enchiladas",
                        "calories": 580,
                        "protein": 22,
                        "carbs": 75,
                        "fats": 25,
                        "ingredients": ["corn tortillas", "cheese", "beans", "vegetables", "enchilada sauce", "crema"],
                        "activity_level": ["All"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Taco Bowl",
                        "calories": 520,
                        "protein": 20,
                        "carbs": 70,
                        "fats": 22,
                        "ingredients": ["brown rice", "black beans", "sofritas", "corn", "guacamole", "salsa"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Taco Salad",
                        "calories": 580,
                        "protein": 38,
                        "carbs": 12,
                        "fats": 45,
                        "ingredients": ["ground beef", "lettuce", "cheese", "avocado", "sour cream", "olives"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "High-Protein Mexican Bowl",
                        "calories": 680,
                        "protein": 55,
                        "carbs": 45,
                        "fats": 30,
                        "ingredients": ["chicken breast", "steak", "black beans", "quinoa", "cheese", "pico de gallo"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low-Carb Fajita Plate",
                        "calories": 520,
                        "protein": 40,
                        "carbs": 18,
                        "fats": 35,
                        "ingredients": ["chicken", "bell peppers", "onions", "guacamole", "sour cream", "cheese"],
                        "activity_level": ["All"]
                    }
                ]
            },
            "dinner": {
                "balanced": [
                    {
                        "name": "Traditional Mexican Combo",
                        "calories": 750,
                        "protein": 38,
                        "carbs": 85,
                        "fats": 32,
                        "ingredients": ["enchiladas", "rice", "beans", "guacamole", "pico de gallo", "crema"],
                        "activity_level": ["Sedentary", "Lightly Active"]
                    },
                    {
                        "name": "Seafood Molcajete",
                        "calories": 880,
                        "protein": 45,
                        "carbs": 70,
                        "fats": 45,
                        "ingredients": ["shrimp", "fish", "octopus", "rice", "vegetables", "tortillas"],
                        "activity_level": ["Moderately Active", "Very Active", "Extra Active"]
                    }
                ],
                "vegetarian": [
                    {
                        "name": "Vegetable Chile Rellenos",
                        "calories": 620,
                        "protein": 25,
                        "carbs": 65,
                        "fats": 35,
                        "ingredients": ["poblano peppers", "cheese", "rice", "beans", "salsa roja", "crema"],
                        "activity_level": ["All"]
                    }
                ],
                "vegan": [
                    {
                        "name": "Vegan Mexican Platter",
                        "calories": 580,
                        "protein": 22,
                        "carbs": 75,
                        "fats": 28,
                        "ingredients": ["jackfruit carnitas", "rice", "black beans", "guacamole", "tortillas", "salsa"],
                        "activity_level": ["All"]
                    }
                ],
                "keto": [
                    {
                        "name": "Keto Mexican Platter",
                        "calories": 650,
                        "protein": 45,
                        "carbs": 12,
                        "fats": 50,
                        "ingredients": ["carne asada", "cheese", "guacamole", "lettuce", "sour cream", "pico de gallo"],
                        "activity_level": ["All"]
                    }
                ],
                "high-protein": [
                    {
                        "name": "Protein Fiesta Plate",
                        "calories": 750,
                        "protein": 60,
                        "carbs": 45,
                        "fats": 35,
                        "ingredients": ["grilled chicken", "steak", "shrimp", "black beans", "cheese", "pico de gallo"],
                        "activity_level": ["All"]
                    }
                ],
                "low-carb": [
                    {
                        "name": "Low-Carb Mexican Feast",
                        "calories": 580,
                        "protein": 45,
                        "carbs": 20,
                        "fats": 38,
                        "ingredients": ["carne asada", "chicken", "lettuce wraps", "cheese", "guacamole", "pico de gallo"],
                        "activity_level": ["All"]
                    }
                ]
            }
        }
    }
    

def calculate_bmr(weight_kg, height_cm, age, gender):
    """Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation"""
    if gender == "Male":
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

def calculate_daily_calories(bmr, activity_level):
    """Calculate daily caloric needs based on activity level"""
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9
    }
    return bmr * activity_multipliers[activity_level]

def get_macro_distribution(diet_type):
    """Return macro distribution based on diet type"""
    macro_distributions = {
        "balanced": {"protein": 0.3, "carbs": 0.4, "fats": 0.3},
        "keto": {"protein": 0.3, "carbs": 0.1, "fats": 0.6},
        "high-protein": {"protein": 0.4, "carbs": 0.3, "fats": 0.3},
        "low-carb": {"protein": 0.35, "carbs": 0.25, "fats": 0.4}
    }
    return macro_distributions.get(diet_type, macro_distributions["balanced"])

def main():
    st.title("🥗 AI Nutrition Assistant")
    
    # Initialize session state
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    
    # Sidebar for user input
    with st.sidebar:
        st.header("Personal Details")
        
        name = st.text_input("Name", key="name")
        age = st.number_input("Age", 18, 100, 30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        
        # Height input with unit conversion
        height_unit = st.selectbox("Height Unit", ["cm", "feet"])
        if height_unit == "cm":
            height = st.number_input("Height (cm)", 100, 250, 170)
        else:
            feet = st.number_input("Feet", 4, 7, 5)
            inches = st.number_input("Inches", 0, 11, 8)
            height = (feet * 30.48) + (inches * 2.54)
        
        # Weight input with unit conversion
        weight_unit = st.selectbox("Weight Unit", ["kg", "lbs"])
        if weight_unit == "kg":
            weight = st.number_input("Weight (kg)", 40, 200, 70)
        else:
            weight_lbs = st.number_input("Weight (lbs)", 88, 440, 154)
            weight = weight_lbs * 0.453592
        
        country = st.selectbox("Country", ["USA", "India", "Japan", "Italy", "Mexico"])
        diet_type = st.selectbox("Diet Type", 
            ["Balanced", "Vegetarian", "Vegan", "Keto", "High-Protein", "Low-Carb"])
        activity_level = st.selectbox("Activity Level",
            ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"])
        
        meal_time = st.selectbox("Meal Time", ["Breakfast", "Lunch", "Dinner"])
        
        if st.button("Generate Meal Plan"):
            # Calculate daily nutritional needs
            bmr = calculate_bmr(weight, height, age, gender)
            daily_calories = calculate_daily_calories(bmr, activity_level)
            macro_dist = get_macro_distribution(diet_type.lower())
            
            st.session_state.user_data = {
                "name": name,
                "daily_calories": daily_calories,
                "macro_distribution": macro_dist,
                "meal_time": meal_time.lower(),
                "country": country,
                "diet_type": diet_type.lower()
            }

    # Main content area
    if st.session_state.user_data:
        st.header(f"Hello {st.session_state.user_data['name']}! 👋")
        
        # Display daily nutritional needs
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Daily Calories", f"{int(st.session_state.user_data['daily_calories'])} kcal")
        with col2:
            st.metric("Protein", f"{int(st.session_state.user_data['daily_calories'] * st.session_state.user_data['macro_distribution']['protein'] / 4)}g")
        with col3:
            st.metric("Carbs", f"{int(st.session_state.user_data['daily_calories'] * st.session_state.user_data['macro_distribution']['carbs'] / 4)}g")

        # Load and display meal suggestions
        food_db = load_food_database()
        if (country_meals := food_db.get(st.session_state.user_data['country'])):
            if (time_meals := country_meals.get(st.session_state.user_data['meal_time'])):
                if (diet_meals := time_meals.get(st.session_state.user_data['diet_type'])):
                    st.subheader("Suggested Meals")
                    for meal in diet_meals:
                        with st.expander(f"🍽 {meal['name']}"):
                            st.write("*Nutritional Information:*")
                            st.write(f"- Calories: {meal['calories']} kcal")
                            st.write(f"- Protein: {meal['protein']}g")
                            st.write(f"- Carbs: {meal['carbs']}g")
                            st.write(f"- Fats: {meal['fats']}g")
                            
                            st.write("*Ingredients:*")
                            for ingredient in meal['ingredients']:
                                st.write(f"- {ingredient}")
                            
                            if st.button(f"Get Alternative to {meal['name']}"):
                                st.write("Alternative meals would be suggested here...")
                else:
                    st.warning("No meals found for your diet type. Try a different combination.")

if __name__ == "__main__":
    main()