# Telegram AI Bot

Welcome to the Telegram Bot project! This bot allows you to interact with a neural network while maintaining a conversation history. You can also delete your chat history if needed. All messages are logged in a PostgreSQL database.

## Features

- Communicate with a neural network powered by Google Generative AI.
- Maintain a history of your conversations.
- Delete chat history whenever required.
- Store all messages in a PostgreSQL database for later retrieval.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed
- PostgreSQL database server running
- A Telegram API token
- A Google API key for accessing Google Generative AI

## Getting Started

Follow these steps to set up and run the bot:

### Clone the Repository

```bash
    git clone https://github.com/bigit22/AiogramBot.git
    cd AiogramBot
```

### Set Up a Virtual Environment
```bash
    python3 -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Install Dependencies

```bash
    pip install -r requirements.txt
```

### Configure Environment Variables
Create a .env file in the root of the project and add your configuration variables:

```
    TELEGRAM_API_TOKEN=your_telegram_api_token
    GOOGLE_API_KEY=your_google_api_key
    POSTGRES_USER=your_postgres_user
    POSTGRES_PASSWORD=your_postgres_password
    POSTGRES_DB=your_postgres_database_name
    POSTGRES_HOST=your_postgres_host
```

### Running the Bot
To start the bot, run the following command:

```bash
    python main.py
```
### Contributing
If you would like to contribute to this project, please feel free to submit a pull request or create an issue for discussion.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
Aiogram - Telegram bot framework for Python.
Google Generative AI - Powerful AI tools from Google.
PostgreSQL - Reliable relational database management system.
Enjoy chatting with the neural network!

## Database Structure
This section describes the structure of the PostgreSQL database used in the Telegram AI Bot project.

### Schema: `public`

#### Table: `chat_history`

This table stores the conversation history between users and the neural network.

| Column Name   | Data Type | Constraints         | Description                                  |
|---------------|-----------|---------------------|----------------------------------------------|
| `id`          | SERIAL    | PRIMARY KEY         | Unique identifier for each message entry.    |
| `telegram_id` | INT       | NOT NULL            | Unique identifier for each user in Telegram. |
| `message`     | TEXT      | NOT NULL            | Content: prompt + model response.            |

### Additional Notes
- The `telegram_id` can be used to associate multiple messages with the same user.
- To maintain a clean history, users can delete their chat history whenever required, which will remove all messages associated with their `telegram_id`.

This structure allows for efficient storage and retrieval of conversation history while enabling scalability for future features.
