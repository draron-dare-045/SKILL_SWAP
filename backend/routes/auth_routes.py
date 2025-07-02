# backend/routes/auth_routes.py
from flask import Blueprint, request, jsonify
from models import User
from schemas import user_schema
from extensions import db, bcrypt
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    # Check if user already exists
    if User.query.filter_by(email=data['email']).first() or User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User with that email or username already exists"}), 400
    
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password']) # Password is automatically hashed
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        # Add user role to the JWT claims
        additional_claims = {"role": user.role, "username": user.username}
        access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401