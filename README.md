# Discord Bot 🤖

A feature-rich Discord bot built with **Python** and **discord.py**, offering moderation tools, role management, entertainment commands, and interactive utilities for your Discord server.

##  Features

###  Moderation
- **Automatic Content Filtering**: Detects and removes messages containing prohibited words
- **Smart Warning System**: Sends private warnings to users when they violate content rules
- **Customizable Word List**: Easy to modify banned words list

###  Role Management
- **Self-Service Roles**: Users can assign/remove roles independently
- **Secret Role System**: Special role assignment with controlled access
- **Role Verification**: Prevents duplicate role assignments

###  Fun & Entertainment
- **Interactive Greetings**: Personalized welcome messages
- **Random Jokes**: Powered by the [pyjokes](https://github.com/pyjokes/pyjokes) library
- **Bot Responsiveness**: Real-time ping/pong functionality
- **Message Interaction**: Smart reply system

###  Utility Commands
- **Bot Information**: Version details, author info, and feature overview
- **Help System**: Comprehensive command listing with descriptions
- **Direct Messaging**: Private communication capabilities
- **Interactive Polls**: Create yes/no polls with emoji reactions

##  Command Reference

| Command | Description | Usage |
|---------|-------------|-------|
| `/hello` | Bot sends a personalized greeting | `/hello` |
| `/ping` | Check bot latency and responsiveness | `/ping` |
| `/joke` | Get a random programming joke | `/joke` |
| `/info` | Display bot information and stats | `/info` |
| `/helpme` | Show all available commands | `/helpme` |
| `/assign` | Assign yourself the secret role | `/assign` |
| `/remove` | Remove your secret role | `/remove` |
| `/poll <question>` | Create a yes/no poll with reactions | `/poll Should we add music bot?` |
| `/dm <message>` | Send yourself a direct message | `/dm Remember to check logs` |
| `/reply` | Bot responds to your message | `/reply` |
| `/botinfo`| Gives soft info related to Bot| `/botinfo`|

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- A Discord account and server
- Basic knowledge of Discord bot setup

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/cognitioo/discord-bot.git
   cd discord-bot
   ```

2. **Set Up Virtual Environment** (Recommended)
   ```bash
   # Create virtual environment
   python -m venv discord-bot-env
   
   # Activate virtual environment
   # Windows:
   discord-bot-env\Scripts\activate
   
   # Linux/macOS:
   source discord-bot-env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   
   Create a `.env` file in the project root:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   ```
   
   > **⚠️ Important**: Never share your bot token publicly! Keep your `.env` file secure.

5. **Run the Bot**
   ```bash
   python bot.py
   ```

## 🔧 Configuration

### Getting Your Discord Bot Token

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or select an existing one
3. Navigate to the "Bot" section
4. Copy your bot token and paste it in the `.env` file
5. Ensure your bot has the necessary permissions in your server

### Required Bot Permissions
- Send Messages
- Read Message History
- Manage Roles (for role commands)
- Add Reactions (for polls)
- Send Direct Messages

## 📁 Project Structure

```
discord-bot/
├── bot.py              # Main bot file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

##  Changelog

### v1.0.0
- Initial release with core functionality
- Moderation system implementation
- Role management features
- Fun commands and utilities

##  Troubleshooting

### Common Issues

**Bot doesn't respond to commands:**
- Check if the bot is online in your server
- Verify bot permissions
- Ensure the bot token is correct in `.env`

**Role assignment fails:**
- Check if bot has "Manage Roles" permission
- Ensure bot's role is higher than the role being assigned

**Installation problems:**
- Make sure you're using Python 3.8+
- Try updating pip: `pip install --upgrade pip`

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Author

**cognitioo** - [GitHub Profile](https://github.com/cognitioo)

##  Acknowledgments

- [discord.py](https://discordpy.readthedocs.io/) - The Discord API wrapper
- [pyjokes](https://github.com/pyjokes/pyjokes) - Random joke generation
- Discord community for inspiration and support

##  Upcoming Feature

### v2.0.0 - AI Integration (Coming Soon)
A new possible update which i think will be good update and if this post get maybe 3 stars I'll publish it here :

####  Intelligent AI Assistant
- **LLM Integration**: Advanced AI powered by state-of-the-art language models
- **Context-Aware Responses**: AI adapts its personality and knowledge to match your server's theme
- **Server-Specific Training**: Tailored responses for gaming, development, community, or any server type

####  Smart Query System
**New Command**: `/ai <your_question>`

**Examples:**
- `/ai How many Pokéballs exist in the Pokémon universe?` 
- `/ai What's the best strategy for late-game in League of Legends?`
- `/ai Explain quantum computing in simple terms`

####  Key Benefits
- **No More Google Searches for small things**: Get instant, accurate answers directly in Discord
- **Server-Themed Responses**: Gaming servers get gaming-focused answers, tech servers get technical explanations
- **Fact-Checking Capabilities**: Reliable information verification (similar to @grok on X/Twitter)
- **Real-Time Knowledge**: Stay updated with current information and trends

####  Technical Features
- **Customizable AI Personality**: Server admins can adjust the AI's tone and focus areas
- **Rate Limiting**: Prevents spam while ensuring fair usage
- **Privacy-First**: No conversation data stored permanently
- **Multi-Language Support**: Communicate in your preferred language

**Expected Release**: Q2 2025

*Stay tuned for this game-changing update that will make your Discord server the smartest community on the platform!*

---

**⭐ If you find this bot useful, please consider giving it a star!**

For questions, suggestions, or support, feel free to open an issue or contact the maintainer.
