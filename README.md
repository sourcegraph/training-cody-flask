# Flask Refactor Demo

This example demonstrates Cody's ability to refactor an existing codebase, adding tests and new functionality quickly and effectively.

## Application Structure

The application is built with Flask and organized using a blueprint architecture:

- `app.py` - Main application entry point that configures Flask and registers blueprints
- `flask_refactor/routes/main.py` - Contains the main blueprint for web routes
- `flask_refactor/routes/api.py` - Contains the API blueprint for API endpoints
- `flask_refactor/templates/` - Contains HTML templates
- `flask_refactor/static/` - Contains static assets (CSS, JS, images)

## Setup Instructions

### Setting up a virtual environment with uv

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. Follow these steps to set up your environment:

1. Install uv (if not already installed):

```bash
pip install uv
```

2. Create a virtual environment:

```bash
uv venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

On Windows, use:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
uv pip install -r requirements.txt
```

## Running the Application

After setting up the environment and installing dependencies:

```bash
python app.py
```

The application will start in debug mode and be accessible at http://127.0.0.1:5000/

## Development

The application uses Flask's blueprint structure to organize routes:
- Main blueprint handles web pages
- API blueprint handles API endpoints

To add new routes, extend the appropriate blueprint files in the `flask_refactor/routes/` directory.