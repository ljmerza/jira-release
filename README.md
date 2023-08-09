# FastAPI Jira Project

This project provides a FastAPI server that interfaces with the Jira API to help generate a release list.

## Prerequisites

Ensure you have Python 3.7 or above installed. You can check your Python version using:

```bash
python --version
```

## Setting Up a Virtual Environment

Before you run the API, it's recommended to set up a virtual environment. This helps to manage dependencies and ensure that there aren't any conflicts with other Python projects.

1. **Install `virtualenv` if it's not installed**:

```bash
pip install virtualenv
```

2. **Navigate to your project directory and set up the virtual environment**:

```bash
virtualenv venv
```

3. **Activate the virtual environment**:

- **Linux/macOS**:

```bash
source venv/bin/activate
```

- **Windows**:

```bash
.\venv\Scripts\activate
```

You'll know you're in the virtual environment when you see `(venv)` before your command prompt.

## Installing Dependencies

With the virtual environment active, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuring Environment Variables

This project utilizes environment variables to securely manage sensitive configuration, like Jira API credentials. These environment variables are stored in an `.env` file.

1. **Locate the `.env` file**:

In the root directory of the project, you should find an `.env` file. If it doesn't exist, create one.

2. **Update the `.env` file**:

Create a `.env` file in your preferred text editor and set your configuration variables:

```env
JIRA_URL=YOUR_JIRA_URL
JIRA_USERNAME=YOUR_USERNAME_HERE
JIRA_API_TOKEN=YOUR_API_TOKEN_HERE
```

Replace `YOUR_JIRA_URL` with your Jira domain's base url, `YOUR_USERNAME_HERE` with your Jira username, and `YOUR_API_TOKEN_HERE` with your Jira API token.

Generate API token here https://id.atlassian.com/manage-profile/security/api-tokens

3. **Save and Close**:

After updating the values, save the `.env` file and close your text editor.

**Important**: Always keep your `.env` file private. Never expose sensitive credentials in your version control or other public places.

## Running the FastAPI Server

Once you've installed the dependencies, run the FastAPI server:

```bash
python index.py
```

Visit `http://127.0.0.1:8305` or `http://127.0.0.1:8305/docs` in your browser to access the documentation.

## Deactivating the Virtual Environment

After you're done, deactivate the virtual environment:

```bash
deactivate
```
