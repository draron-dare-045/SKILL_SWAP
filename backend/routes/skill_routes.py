# backend/routes/skill_routes.py
from flask import Blueprint, request, jsonify
from models import Skill
from schemas import skill_schema, skills_schema
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators import admin_required

skill_bp = Blueprint('skill_bp', __name__)

# ANYONE (even unauthenticated) can view skills
@skill_bp.route('/', methods=['GET'])
def get_all_skills():
    skills = Skill.query.all()
    return jsonify(skills_schema.dump(skills))

# LOGGED-IN USERS can create a skill
@skill_bp.route('/', methods=['POST'])
@jwt_required()
def create_skill():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_skill = Skill(
        name=data['name'],
        description=data.get('description', ''),
        user_id=user_id
    )
    db.session.add(new_skill)
    db.session.commit()
    return jsonify(skill_schema.dump(new_skill)), 201

# ADMINS ONLY can update or delete skills
@skill_bp.route('/<int:id>', methods=['PUT'])
@admin_required()
def update_skill(id):
    skill = Skill.query.get_or_404(id)
    data = request.get_json()
    skill.name = data.get('name', skill.name)
    skill.description = data.get('description', skill.description)
    db.session.commit()
    return jsonify(skill_schema.dump(skill))

@skill_bp.route('/<int:id>', methods=['DELETE'])
@admin_required()
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({"message": "Skill deleted successfully"}), 200