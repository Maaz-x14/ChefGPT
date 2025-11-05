## ChefGPT

Your AI sous-chef — crafting creative restaurants and menus, one cuisine at a time.

ChefGPT takes a single cuisine name — “Italian,” “Pakistani,” “Japanese” — and generates a full fictional restaurant concept complete with:

A unique restaurant name

Themed description

Fully-fledged menu (appetizers, mains, desserts, beverages)

Creative dish names, flavor descriptions, and local currency prices

Built in Python, ChefGPT uses LLM-powered text generation under the hood to design entire menus in seconds.

🧠 How It Works

ChefGPT uses a prompt chain that takes your cuisine type as input, runs it through a language model, and formats a complete restaurant concept in a readable structure.

You → enter a cuisine type
↓
ChefGPT → creates a restaurant name + themed menu
↓
Output → beautifully written restaurant concept ready to serve

Example:

Enter a cuisine type (e.g. Italian, Mongolian, Japanese):
> Pakistani

Output:

🏷️ Restaurant Name: Nawaazish
📜 Menu for “Spice & Theory: A Taste of Pakistan”

Then a full detailed menu (appetizers, mains, desserts, beverages) with creative writing and PKR prices.

🏗️ Project Structure
ChefGPT/
├── chains/         # Prompt and response chains for cuisine → menu generation
├── config/         # Configuration files (API keys, prompt templates, constants)
├── utils/          # Helper functions (I/O, text formatting, etc.)
├── main.py         # Entry point — runs the ChefGPT assistant
├── .env            # Environment variables (API keys, etc.)
└── .gitignore

⚙️ Setup Instructions

Clone the Repository

git clone https://github.com/Maaz-x14/ChefGPT.git
cd ChefGPT

Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate    # For Windows: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

(If missing, add packages like openai, python-dotenv, etc.)

Configure Environment
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
MODEL=gpt-4-turbo

Run the App

python main.py

🧾 Example Output
🍽️ ChefGPT
Your AI sous-chef — crafting creative restaurants and menus, one cuisine at a time.

Enter a cuisine type (e.g. Italian, Mongolian, Japanese):
> Pakistani

Result:

🏷️ Restaurant Name
Nawaazish

📜 Menu
Spice & Theory: A Taste of Pakistan

Appetizers:
- Samosa Chaat (PKR 350): Crispy samosas in tangy yogurt and chutneys.
- Seekh Kebab (PKR 550): Minced beef skewers grilled to perfection.

Mains:
- Chicken Karahi (PKR 1200): Tomato-based curry bursting with ginger and garlic.
- Biryani (PKR 1100): Aromatic rice layered with spiced chicken.

Desserts:
- Gulab Jamun (PKR 400): Syrupy milk balls soaked in rose syrup.

💡 Why ChefGPT?

Instant creativity: Generate new restaurant ideas in seconds.

Localized menus: Auto-adds culturally relevant dishes and currencies.

Perfect for developers & creators: Use it for restaurant mockups, UI demos, or culinary data generation.

Fully modular: Swap chains, prompts, or models with minimal code changes.

🧩 Extending the Project

You can easily enhance ChefGPT by:

Adding multiple-cuisine menus (fusion restaurants).

Including dish images via image generation APIs.

Creating a Streamlit or Flask web interface.

Adding a “random theme” mode (street food, fine dining, vegan, etc.).

Saving menus as JSON or Markdown exports.

🛠️ Tech Stack

Python 3.10+

OpenAI API (LLM text generation)

dotenv for environment management

Modular structure for future web or API integration

🤝 Contributing

Got a great idea for new features or menu formats?

Fork the repo

Create a new branch (feature/menu-export)

Submit a PR

Please follow standard Python formatting (PEP-8) and keep commits clean.

📄 License

MIT License © Maaz-x14

👨‍🍳 Author

Built with flavor and code by Maaz-x14
💬 Reach out on GitHub for ideas, collaborations, or just foodie banter.
