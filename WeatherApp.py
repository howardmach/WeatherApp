# WeatherApp.py
# Entry point for the Weather App Flask application

from app import create_app

# Create the Flask application instance using the factory pattern
app = create_app()

if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)