# Discord Welcome Bot

A modular **Discord bot** built with `discord.py` that handles a customizable welcome message system using slash commands and persistent JSON storage.

## Features

* **Slash Command Group (`/hello`)** — Full configuration toolset directly integrated into Discord's UI
* **Custom Channels** — Set any text channel as the designated welcome zone per server
* **Dynamic Messages** — Personalize welcome texts with `{user}` and `{server}` placeholders
* **Persistent Storage** — Saves server settings locally using a JSON configuration file (`config.json`)
* **Admin Security** — Restricts setup commands to members with the **Manage Server** permission
* **Rich Embeds** — Sends automated, clean embed messages featuring user avatars when a new member joins

## Project Structure

```
discord-welcome-bot/
├── main.py             # Main bot script (events, commands, JSON loader)
└── config.json         # Local database for server configurations (auto-created)

```

## Requirements & Dependencies

1. **Python**: Version 3.8 or higher
2. **Library**:
* `discord.py` (ensure you have the modern version supporting slash commands)



Install the required library via terminal/CLI:

```bash
pip install discord.py

```

## Setup and Running

1. Create a new bot application on the [Discord Developer Portal](https://discord.com/developers/applications).
2. Enable the **Server Members Intent** under the **Bot** tab in your application settings.
3. Replace `"BOT_TOKEN"` in `main.py` with your actual Discord bot token:
```python
bot.run("YOUR_BOT_TOKEN_HERE")

```


4. Run the script:
```bash
python main.py

```



## Slash Commands Reference

| Command | Description | Permission Required |
| --- | --- | --- |
| `/hello add` | Sets the current channel as the active welcome channel | Manage Server |
| `/hello remove` | Disables the welcome system for the server | Manage Server |
| `/hello setmessage` | Customizes the welcome text (supports `{user}` and `{server}`) | Manage Server |
| `/hello show` | Displays the current configuration and channel settings | None |
