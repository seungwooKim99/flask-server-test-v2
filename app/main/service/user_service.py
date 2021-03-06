#user 모델에 관련된 쿼리문 작성 파일
from app.main import db
from app.main.model.user import User

#회원가입한 회원 정볼를 user모델(즉, user테이블에 넣기)
def save_new_user(data): 
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            username=data['username'],
            password=data['password'],
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': '회원가입 되었습니다. '
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': '이미 가입된 회원입니다.',
        }# 체를 JSON으로 포맷 하기 위해 jsonify 를 사용할 필요가 없습니다 . Flask-restplus가 자동으로 수행합니다.
        return response_object, 409


def get_all_users():
    return User.query.all()

def get_a_user(id):
    return User.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit() 