# backend/seed.py
from app import create_app
from extensions import db
from models import User

def seed_admin():
    """
    Creates the default admin user if one does not already exist.
    """
    # Create an application context to be able to interact with the database
    app = create_app()
    with app.app_context():
        # Check if an admin user already exists to prevent creating duplicates
        if User.query.filter_by(role='admin').first():
            print("Admin user already exists. Skipping seed.")
            return

        # Define the details for the new admin user
        admin_user = User(
            username='breana',
            email='breana@skillswap.com',
            role='admin'  # This is the crucial part that grants admin privileges
        )
        
        # Set the password for the admin user.
        # It is highly recommended to change this password for a real application.
        admin_user.set_password('breana')
        
        # Add the new admin user object to the database session
        db.session.add(admin_user)
        
        # Commit the session to save the new user to the database
        db.session.commit()

        print("Admin user 'admin' created successfully.")