# Omni-B0T
Omni-B0T is an omnichannel, voice-controlled automation tool designed to streamline your social media broadcasting. Built with Python, it uses PRAW and SpeechRecognition to translate spoken commands into seamless posts across targeted subreddits and social channels.

0mni-B0t/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
└── src/
    ├── __init__.py
    ├── config.py
    ├── voice_input.py
    ├── voice_output.py
    ├── post_manager.py       <-- The orchestrator that handles cross-posting
    └── platforms/
        ├── __init__.py
        ├── reddit_client.py  <-- Your existing Reddit code
        ├── discord_client.py <-- For Discord integration
        └── bluesky_client.py <-- For decentralized open-web posting

