import os
from app import app

if __name__ == "__main__":
    app.debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    host = os.environ.get('IP' , '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))

    try:
        print(f"Starting server at http://{host}:{port} (Debug={app.debug})")
        app.run(host=host, port=port)
    except Exception as e:
        print(f"Error: {e}")
