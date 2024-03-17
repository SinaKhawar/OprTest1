from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)

# Run the application if executed directly
if __name__ == '__main__':
    app.run(debug=True)
