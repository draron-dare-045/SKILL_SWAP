# backend/routes/user_routes.py
from flask import Blueprint, jsonify
from models import User
from schemas import users_schema
from decorators import admin_required

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['GET'])
@admin_required()
def get_all_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))