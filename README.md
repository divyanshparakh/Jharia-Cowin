# Jharia-Cowin: CoWIN Vaccine Slot Notifier

![CoWIN Logo](https://img.shields.io/badge/CoWIN-Vaccine%20Slot%20Notifier-blueviolet?style=flat-square)  
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT)  
[![Heroku Deploy](https://img.shields.io/badge/Deploy-Heroku-purple?style=flat-square&logo=heroku)](https://heroku.com)  

## Overview

Jharia-Cowin is a Python-based Telegram bot designed to monitor the CoWIN API for COVID-19 vaccine slot availability in India. It sends real-time notifications via Telegram when slots become available for booking, helping users secure appointments during high-demand periods. The bot runs continuously, polling the API at regular intervals, and includes audio alerts for local development/testing.

This project demonstrates skills in:
- API integration (CoWIN public API and Telegram Bot API)
- Real-time monitoring and notification systems
- Environment variable management for secure configuration
- Cross-platform compatibility (local PC with sound alerts and cloud deployment on Heroku)
- Error handling and resilient polling

Originally built during the COVID-19 pandemic (circa 2021), it showcases practical automation for public health tools. The repo includes all necessary files for local setup, Heroku deployment, and dependencies.

## Features

- **Real-Time Slot Checking**: Polls the CoWIN API every 60 seconds for vaccine slots by PIN code and date.
- **Telegram Notifications**: Sends instant messages to a specified chat when slots are available, including details like center name and age limit.
- **Audio Alerts**: Plays sound notifications (e.g., ding-dong for startup, air-raid for slot availability) during local runs using Pygame.
- **Customizable**: Configurable via environment variables for PIN code, Telegram bot token, and chat ID.
- **Heroku-Ready Deployment**: Includes `Procfile` for easy cloud hosting to run 24/7 without local hardware.
- **Error Resilience**: Handles API failures, internet issues, and empty responses with retries and notifications.
- **Cross-Platform Clearing**: Clears console output for clean logging on Windows/Linux.

## Tech Stack

- **Language**: Python 3.8+
- **Libraries**:
  - `requests`: For API calls to CoWIN and Telegram.
  - `pygame`: For audio playback (local alerts).
  - `python-dotenv`: For loading environment variables from `.env`.
  - `termcolor`: For colored console output.
- **APIs**:
  - CoWIN Public API (v2) for slot data.
  - Telegram Bot API for notifications.
- **Deployment**: Heroku (via `Procfile` and `runtime.txt`).
- **Other Tools**: Git for version control, with `.gitignore` to exclude sensitive files.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher.
- A Telegram bot token (create one via [BotFather](https://t.me/botfather)).
- A CoWIN-compatible PIN code for your area.
- Optional: Audio files in the `sound/` directory for local alerts.

### Local Setup
1. Clone the repository:
   ```
   git clone https://github.com/divyanshparakh/Jharia-Cowin.git
   cd Jharia-Cowin
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following:
   ```
   ChatID=your_telegram_chat_id
   TokenID=your_telegram_bot_token
   Pincode=your_area_pincode (e.g., 826001 for Jharia)
   PORT=8000  # Optional, for Heroku-like local testing
   ```
   - **Note**: `.env` is ignored by Git for security. Never commit sensitive info!

4. Run the bot:
   ```
   python bot.py
   ```
   - It will start polling and send a "App has been Started!" message to Telegram.
   - On slot availability, you'll get audio alerts and colored console logs.

### Heroku Deployment
This repo is pre-configured for Heroku to run as a background worker (e.g., for 24/7 operation).

1. Create a Heroku account and install the Heroku CLI.
2. Log in:
   ```
   heroku login
   ```

3. Create a new app:
   ```
   heroku create jharia-cowin-bot
   ```

4. Set environment variables on Heroku (instead of `.env`):
   ```
   heroku config:set ChatID=your_chat_id
   heroku config:set TokenID=your_bot_token
   heroku config:set Pincode=your_pincode
   heroku config:set ON_HEROKU=true  # Disables local-specific features like sound
   ```

5. Push to Heroku:
   ```
   git push heroku main
   ```

6. Scale the worker:
   ```
   heroku ps:scale worker=1
   ```
   - The `Procfile` defines the process: `worker: python bot.py`. This tells Heroku to run the bot as a non-web worker process.
   - `runtime.txt` specifies the Python version (e.g., `python-3.8.10`) for consistent builds.

   **What is Procfile?** It's a simple text file used by Heroku to declare what commands should be executed to start your app. In this case, it ensures the bot runs continuously as a worker dyno, ideal for background tasks like API polling.

## Usage

- **Local Run**: Execute `python bot.py`. Monitor the console for logs. Audio will play on events.
- **Customization**:
  - Change `SLEEP_TIME` in code for polling frequency (default: 60 seconds).
  - Update `Date` logic if checking multiple dates.
  - Extend for multiple PIN codes by modifying `PARAMS`.
- **Testing**: Simulate slots by mocking API responses or using test data.
- **Stopping**: Ctrl+C in terminal. On Heroku, scale down with `heroku ps:scale worker=0`.

### Example Notification
When a slot is found:
- Telegram: "Center Name (for 18+)"
- Console: Red blinking text for available slots.

## File Structure

- `bot.py`: Main script with API polling and notification logic.
- `requirements.txt`: List of Python dependencies.
- `.env`: Template for environment variables (not committed).
- `.gitignore`: Excludes sensitive files like `.env` and pycache.
- `Procfile`: Heroku process declaration.
- `runtime.txt`: Specifies Python runtime for Heroku.
- `sound/`: Directory with audio files (`dingdong.wav` for startup, `airraid.wav` for alerts).
- Other files: Historical commits like `divz11` (possibly a branch or old file; ignore for core functionality).

## Potential Improvements
- Add support for multiple dates/PIN codes.
- Integrate email/SMS notifications.
- Webhook-based Telegram updates for efficiency.
- Dockerize for broader deployment options.
- Unit tests for API response handling.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- GitHub: [divyanshparakh](https://github.com/divyanshparakh/)
- Email: divyanshparakh11@gmail.com

Feel free to fork, contribute, or reach out with questions! This project was built to make a real-world impact during a crisis, highlighting automation's role in accessibility.
