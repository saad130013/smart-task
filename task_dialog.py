
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
from models import Task
from database import Session
from ai_classifier import classify_task_text

class TaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("إضافة مهمة جديدة")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("عنوان المهمة")
        layout.addWidget(QLabel("العنوان:"))
        layout.addWidget(self.title_input)

        self.desc_input = QTextEdit()
        layout.addWidget(QLabel("الوصف:"))
        layout.addWidget(self.desc_input)

        self.ai_btn = QPushButton("🤖 اقتراح تصنيف المهمة")
        self.ai_btn.clicked.connect(self.suggest_category)
        layout.addWidget(self.ai_btn)

        self.save_btn = QPushButton("حفظ المهمة")
        self.save_btn.clicked.connect(self.save_task)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def suggest_category(self):
        description = self.desc_input.toPlainText()
        if description.strip():
            label, score = classify_task_text(description)
            self.setWindowTitle(f"اقتراح: {label} ({score:.2f})")

    def save_task(self):
        title = self.title_input.text()
        description = self.desc_input.toPlainText()
        if title.strip():
            session = Session()
            task = Task(title=title, description=description)
            session.add(task)
            session.commit()
            session.close()
            self.accept()
