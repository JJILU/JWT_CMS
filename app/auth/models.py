from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
# from uuid import uuid4


# ========================= School Records Database ==========================

class TeacherSchoolRecord(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(50),nullable=False) 
    last_name = db.Column(db.String(50),nullable=False) 
    teacher_school_id = db.Column(db.String(50),nullable=False) 
    # filename = db.Column(db.String(500),nullable=False) 
    # filepath = db.Column(db.String(500),nullable=False) 

    def __init__(self,first_name,last_name,teacher_school_id):
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_school_id = teacher_school_id


class StudentSchoolRecord(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    id = db.Column(db.Integer,primary_key=True)   
    first_name = db.Column(db.String(50),nullable=False) 
    last_name = db.Column(db.String(50),nullable=False) 
    student_school_id = db.Column(db.String(50),nullable=False) 
    # filename = db.Column(db.String(500),nullable=False) 
    # filepath = db.Column(db.String(500),nullable=False) 

    def __init__(self,first_name,last_name,student_school_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_school_id = student_school_id



        
# ========================= Classroom Management Users ==========================

class Teacher(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    id = db.Column(db.Integer,primary_key=True)
    teacher_card_id = db.Column(db.String(50),nullable=False)
    hashed_password = db.Column(db.String(50),nullable=False)
    role = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

   
        

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: teacher card id {self.teacher_card_id}>"
    
    def __init__(self, teacher_card_id, password,role) -> None:
        self.teacher_card_id = teacher_card_id
        self.password = set_hashed_password(password)
        self.role = role

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



class Admin(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    id = db.Column(db.Integer,primary_key=True)
    admin_card_id = db.Column(db.String,nullable=False)
    hashed_password = db.Column(db.String(50))
    role = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: teacher card id {self.admin_card_id}>"
    
    def __init__(self, admin_card_id, password,role) -> None:
        self.admin_card_id = admin_card_id
        self.password = set_hashed_password(password)
        self.role = role


    # hash password at registration
    def set_hashed_password(self,password):
        return generate_password_hash(password)
    
    # compare hashed password to password submitted at login
    def check_hashed_password(self,password):
        return check_password_hash(self.hashed_password,password)
    
    # check if teacher already has account, before creating one
    @classmethod
    def get_admin_card_id(cls,admin_card_id):
        return Teacher.query.filter_by(admin_card_id=admin_card_id)
    
    # save new teacher account to table
    def save_admin(self):
        db.session.add(self)
        db.session.commit()

    # delete new teacher account to table
    def delete_admin(self):
      db.session.delete(self)
      db.session.commit()



class Student(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    id = db.Column(db.Integer,primary_key=True)
    student_card_id = db.Column(db.String,nullable=False)
    hashed_password = db.Column(db.String(50))
    role = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: teacher card id {self.student_card_id}>"
    
    def __init__(self, student_card_id, password,role) -> None:
        self.student_card_id = student_card_id
        self.password = set_hashed_password(password)
        self.role = role


    # hash password at registration
    def set_hashed_password(self,password):
        return generate_password_hash(password)
    
    # compare hashed password to password submitted at login
    def check_hashed_password(self,password):
        return check_password_hash(self.hashed_password,password)
    
    # check if teacher already has account, before creating one
    @classmethod
    def get_student_card_id(cls,student_card_id):
        return Teacher.query.filter_by(student_card_id=student_card_id)
    
    # save new teacher account to table
    def save_student(self):
        db.session.add(self)
        db.session.commit()

    # delete new teacher account to table
    def delete_student(self):
      db.session.delete(self)
      db.session.commit()      
          


#   ==============   DASHBAORD DATA ========================================
    


class AssignmentsFileUploads(db.Model):
    # id = db.Column(db.String(255),primary_key=True, default=str(uuid4()))
    id = db.Column(db.Integer,primary_key=True)   
    filename = db.Column(db.String(500),nullable=False) 
    filepath = db.Column(db.String(500),nullable=False) 

    # 1:1 ->  StudentSchoolRecord & FileUploads
    # student_school_record_id = db.Column(db.Integer,db.ForeignKey('studentschoolrecord.id'))   



       
