from app import create_app

def test_create_app():
    app = create_app()
    assert app is not None
    assert app.name == "app"
    # Optionally, check if blueprints are registered
    assert "main" in app.blueprints