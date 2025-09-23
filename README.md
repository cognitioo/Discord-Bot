# Discord Bot

A feature-rich Discord bot built in **Python** using **discord.py**, with moderation tools, role management, fun commands, and interactive polls.

---

## Features

### Moderation
- Filters bad words and automatically deletes messages.
- Sends a warning to users when they use prohibited words.

### Role Management
- `/assign` – Assign yourself a secret role (e.g., Gamer).  
- `/remove` – Remove your secret role.

### Fun Commands
- `/hello` – Greet the bot.  
- `/ping` – Check bot responsiveness.  
- `/joke` – Get a random joke from [pyjokes](https://github.com/pyjokes/pyjokes).  
- `/reply` – Bot replies to your message.  

### Utility
- `/info` – Shows bot information (author, version, description).  
- `/helpme` – Lists all available commands.  
- `/dm` – Send a direct message to yourself.  
- `/poll` – Create a simple yes/no poll with reactions.

---

# 1. Clone the repository (or download the ZIP)
git clone https://github.com/cognitioo/discord-bot.git
cd discord-bot

# 2. (Optional) Create a virtual environment
python -m venv venv

# Activate the virtual environment:
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file in the project folder with your bot token:
# Open a text editor and save this as .env
DISCORD_TOKEN=YOUR_BOT_TOKEN

# 5. Run the bot
python bot.py

# 6. In Discord, use commands like:
/hello       - Bot greets you
/ping        - Check if bot is responsive
/joke        - Get a random joke
/info        - See bot information
/helpme      - List all commands
/assign      - Assign yourself the secret role
/remove      - Remove your secret role
/poll <text> - Create a yes/no poll
/dm <text>   - Bot sends you a DM
/reply       - Bot replies to your message
