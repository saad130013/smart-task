
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def add_task(title, description):
    session = Session()
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()
    session.close()

def get_tasks():
    session = Session()
    tasks = session.query(Task).all()
    session.close()
    return tasks
