
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget
from task_dialog import TaskDialog
from database import init_db, Session
from models import Task

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("نظام إدارة المهام الذكي")
        self.resize(600, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        self.add_task_btn = QPushButton("➕ إضافة مهمة جديدة")
        self.add_task_btn.clicked.connect(self.open_add_task_dialog)
        layout.addWidget(self.add_task_btn)

        self.central_widget.setLayout(layout)

        init_db()
        self.load_tasks()

    def open_add_task_dialog(self):
        dialog = TaskDialog()
        if dialog.exec_():
            self.load_tasks()

    def load_tasks(self):
        self.task_list.clear()
        session = Session()
        tasks = session.query(Task).all()
        for task in tasks:
            self.task_list.addItem(f"{task.title} - {task.description}")
        session.close()
