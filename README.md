# Automatic-Zoom-Meeting-Scheduler-with-Email-Integration

This is a repository for the Automatic Zoom Meeting Scheduler with Email Integration project.

## Description

The Automatic Zoom Meeting Scheduler with Email Integration is a Python-based application that automates scheduling Zoom meetings and sending meeting invitations via email. It leverages the Zoom API and Gmail API to handle meeting requests and automate the scheduling process seamlessly.

## Features

- Seamless integration with Zoom and Gmail APIs
- Automated retrieval of meeting requests from Gmail
- Efficient scheduling of Zoom meetings
- Automatic distribution of meeting links to attendees via email

## Prerequisites

To run this application, you need to have the following prerequisites:

- Python 3.7 or higher
- Zoom API credentials
- Gmail API credentials

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Zoom API credentials and Gmail API credentials by following the instructions in the 'credentials' section.

## Usage

To use the Automatic Zoom Meeting Scheduler with Email Integration, follow these steps:

1. Set up your Zoom API credentials and Gmail API credentials by following the instructions in the 'credentials' section.
2. Run the main.py file using the following command:
   ```
   python main.py
   ```
3. The application will automatically retrieve meeting requests from your Gmail account, schedule Zoom meetings, and send meeting invitations via email.

## Credentials

To use the Automatic Zoom Meeting Scheduler with Email Integration, you need to set up your Zoom API credentials and Gmail API credentials.

### Zoom API Credentials

To obtain your Zoom API credentials, follow these steps:

1. Go to the Zoom App Marketplace (https://marketplace.zoom.us/).
2. Sign in to your Zoom account.
3. Navigate to the Develop -> Build App section.
4. Click on the 'Create' button to create a new app.
5. Select the 'JWT' app type.
6. Fill in the required information and click on the 'Create' button.
7. Once your app is created, you will see your 'API Key' and 'API Secret'.
8. Copy the 'API Key' and 'API Secret' and use them as your Zoom API credentials.

### Gmail API Credentials

To obtain your Gmail API credentials, follow these steps:

1. Go to the Google Cloud Console (https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the Gmail API for your project.
4. Create credentials for your project.
5. Download the credentials file (JSON format) and save it as 'credentials.json' in the project directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
