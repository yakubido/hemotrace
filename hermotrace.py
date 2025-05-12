import os, config
import click
# from flask_migrate import Migrate
from application import db, api
from application import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app)

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.context_processor
def inject_version():
  return {"version": config.Config.VERSION}