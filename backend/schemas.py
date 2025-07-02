# backend/schemas.py
from extensions import ma
from models import User, Skill, Exchange

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        # Exclude password hash from serialized output
        exclude = ('password_hash',)
        # Make password write-only (for registration)
        load_only = ('password',)

    password = ma.Str(required=True)
    # Nest skills for detailed user view
    skills_offered = ma.Nested('SkillSchema', many=True, exclude=('offered_by',))

class SkillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Skill
        load_instance = True
        include_fk = True
    
    # Nest user info to show who offers the skill
    offered_by = ma.Nested(UserSchema, only=('id', 'username'))

class ExchangeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exchange
        load_instance = True
        include_fk = True

    requester = ma.Nested(UserSchema, only=('id', 'username'))
    skill = ma.Nested(SkillSchema, only=('id', 'name'))

user_schema = UserSchema()
users_schema = UserSchema(many=True)
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)
exchange_schema = ExchangeSchema()
exchanges_schema = ExchangeSchema(many=True)