from extenstions import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
# from uuid import uuid4


class Teacher(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    id = db.Column(db.Integer,primary_key=True)
    teacher_card_id = db.Column(db.String,nullable=False)
    hashed_password = db.Column(db.String(50))
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: teacher card id {self.teacher_card_id}>"
    
    def __init__(self, teacher_card_id, password) -> None:
        self.teacher_card_id = teacher_card_id
        self.password = set_hashed_password(password)

    # hash password at registration
    def set_hashed_password(self,password):
        return generate_password_hash(password)
    
    # compare hashed password to password submitted at login
    def check_hashed_password(self,password):
        return check_password_hash(self.hashed_password,password)
    
    # check if teacher already has account, before creating one
    @classmethod
    def get_teacher_card_id(cls,teacher_card_id):
        return Teacher.query.filter_by(teacher_card_id=teacher_card_id)
    
    # save new teacher account to table
    def save_teacher(self):
        db.session.add(self)
        db.session.commit()

    # delete new teacher account to table
    def delete_teacher(self):
      db.session.delete(self)
      db.session.commit()
    






       
