from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import subprocess
from kivy.core.window import Window
import platform

class E_LibraryApp(App):
    icon_path = 'C:\\Users\\sampathkumar\\Downloads\\icons8-library-64.png'
    
    def build(self):
        Window.set_icon(self.icon_path)
        
        self.semesters = {
            'Semester 6': [
                {
                    'name': 'Python Programming',
                    'Textbook': 'C:\\Users\\sampathkumar\\OneDrive\\Desktop\\E-LIBRARY\\Assests\\system\\python.pdf',
                    'Previous Question Paper': 'path_to_Previous Question Paper1.pdf',
                    'Question Bank': 'path_to_Question Bank1.pdf'
                },
                {
                    'name': 'Operating System (OS)',
                    'Textbook': 'path_to_Textbook2.pdf',
                    'Previous Question Paper': 'path_to_Previous Question Paper2.pdf',
                    'Question Bank': 'path_to_Question Bank2.pdf'
                },
                {
                    'name':'Software Engineering (SE)',
                    'Textbook':'path',
                    'Previous Question Paper':'path',
                    'Question Bank':'path'
                },
                {
                    'name':'System Software and Compiler Design (SSCD)',
                    'Textbook':'path',
                    'Previous Question Paper':'path',
                    'Question Bank':'path'
                }
                
            ],
            'Semester 5': [
                {
                    'name': 'Computer Networks (CN)',
                    'Textbook': 'path_to_Textbook3.pdf',
                    'Previous Question Paper': 'path_to_Previous Question Paper3.pdf',
                    'Question Bank': 'path_to_Question Bank3.pdf'
                },
                {
                    'name': 'Automata Theory (AT)',
                    'Textbook': 'path_to_Textbook4.pdf',
                    'Previous Question Paper': 'path_to_Previous Question Paper4.pdf',
                    'Question Bank': 'path_to_Question Bank4.pdf'
                },
                {
                    'name': 'Discrete Mathematics (DMS)',
                    'Textbook': 'path_to_Textbook4.pdf',
                    'Previous Question Paper': 'path_to_Previous Question Paper4.pdf',
                    'Question Bank': 'path_to_Question Bank4.pdf'
                },
                {
                    'name': 'Database Management System (DBMS)',
                    'Textbook': 'path_to_Textbook4.pdf',
                    'Previous Question Paper': 'path_to_Previous Question Paper4.pdf',
                    'Question Bank': 'path_to_Question Bank4.pdf'
                }

            ]
        }
        
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=70)
        self.semester_buttons = []
        
        for semester in self.semesters:
            button = Button(
                text=semester,
                size_hint_y=None,
                height=150,
                background_color=(0.0, 0.5, 1.0, 1.0) 
            )
            button.bind(on_release=self.show_books)
            self.semester_buttons.append(button)
            self.layout.add_widget(button)
            
        return self.layout
    
    def show_books(self, button):
        self.layout.clear_widgets()
        semester_name = button.text
        books = self.semesters.get(semester_name, [])
        
        scroll_view = ScrollView()
        scroll_layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        
        for book_data in books:
            book_button = Button(
                text=book_data['name'],
                size_hint_y=None,
                height=60,
                background_color=(0.0, 1.0, 0.5, 1.0) 
            )
            book_button.bind(on_release=lambda btn, data=book_data: self.show_document_options(data))
            scroll_layout.add_widget(book_button)
        
        back_button = Button(
            text="Back",
            size_hint_y=None,
            height=40,
            background_color=(1.0, 0.0, 0.0, 1.0)
        )
        back_button.bind(on_release=self.go_back)
        scroll_layout.add_widget(back_button)
        
        scroll_view.add_widget(scroll_layout)
        self.layout.add_widget(scroll_view)
    
    def show_document_options(self, book_data):
        self.layout.clear_widgets()
        
        doc_types = ['Textbook', 'Previous Question Paper', 'Question Bank']
        
        document_buttons = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        for doc_type in doc_types:
            if book_data.get(doc_type):
                doc_button = Button(
                    text=doc_type.replace('_', ' ').title(),
                    size_hint_y=None,
                    height=40,
                    background_color=(0.0, 0.5, 1.0, 1.0) 
                )
                doc_button.bind(on_release=lambda btn, data=book_data, doc=doc_type: self.open_document(data[doc]))
                document_buttons.add_widget(doc_button)
        
        back_button = Button(
            text="Back",
            size_hint_y=None,
            height=40,
            background_color=(1.0, 0.0, 0.0, 1.0)
        )
        back_button.bind(on_release=lambda btn: self.show_books_from_document_options())
        
        self.layout.add_widget(Label(text=f"Select a document type for {book_data['name']}:", size_hint_y=None, height=40))
        self.layout.add_widget(document_buttons)
        self.layout.add_widget(back_button)
    
    def show_books_from_document_options(self):
        self.layout.clear_widgets()
        
        for semester_button in self.semester_buttons:
            self.layout.add_widget(semester_button)
    
    def open_document(self, document_path):
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(['start', '', document_path], shell=True)
            else:
                subprocess.Popen(['xdg-open', document_path])
        except Exception as e:
            print("Error opening document:", e)
            
    def go_back(self, button):
        self.layout.clear_widgets()
        
        for semester_button in self.semester_buttons:
            self.layout.add_widget(semester_button)

if __name__ == '__main__':
    E_LibraryApp().run()
