from extensions import db,fake
from app.auth.models import TeacherSchoolRecord,StudentSchoolRecord,Teacher,Admin,Student
from faker.providers import BaseProvider
from main import create_app
import random



flask_app = create_app()


# create custom providers
class CustomIDProviders(BaseProvider):
    def teacher_id(self):
        return f"T{random.randint(1000,9999)}"
    def student_id(self):
        return f"S{random.randint(1000,9999)}"
    

fake.add_provider(CustomIDProviders)


def create_teacher_school_records():
    for _ in range(10):
        new_teacher = TeacherSchoolRecord(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
           teacher_school_id=fake.teacher_id()
        )
        db.session.add(new_teacher)
    db.session.commit()   

def create_student_school_records():
    for _ in range(10):
        new_teacher = StudentSchoolRecord(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            student_school_id=fake.student_id()
        )
        db.session.add(new_teacher)
    db.session.commit()      


with flask_app.app_context():
    db.create_all()
    
    try:
        # create_teacher_school_records()
        create_student_school_records()
        print(f"Teachers & Students created successfully")
    except Exception as e:
        print(f"Failed to create teachers & students error occured {str(e)}")
        
            

