from flask import Blueprint, request, jsonify

from app import db
from libs.exceptions import BadRequestException
from models.users import User

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

@users_blueprint.route('/', methods=['GET'])
def get_users():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        users = User.query.paginate(page=page, per_page=per_page).items
        return jsonify([user.serialize for user in users])

    except Exception as e:
        return {'error': str(e)}, 500

@users_blueprint.route('/', methods=['POST'])
def create_user():
    try:
        if request.json is None:
            raise BadRequestException('No request body payload found')
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            raise BadRequestException('Missing username and/or password')
        
        if User.query.filter_by(username=username).first():
            raise BadRequestException('Username is already taken')
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user.serialize, 201

    except BadRequestException as e:
        return {'error': str(e)}, 400
    except Exception as e:
        return {'error': str(e)}, 500
