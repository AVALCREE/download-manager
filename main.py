from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import requests
import os
import subprocess
import sys
import time

DOWNLOAD_FOLDER = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
REQUIREMENTS_FILE = 'requirements.txt'

PRIORITY_MAP = {
    'low': 1,
    'medium': 2,
    'high': 3,
    'ultra': 4
}

def create_requirements_file():
    with open(REQUIREMENTS_FILE, 'w') as f:
        f.write('requests\nkivy\n')

def install_requirements():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', REQUIREMENTS_FILE])

class DownloadManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.priority = 'medium'  # Default priority

        self.url_label = Label(text='Enter URL:')
        self.add_widget(self.url_label)
        self.url_input = TextInput(multiline=False)
        self.add_widget(self.url_input)

        self.download_button = Button(text='Download')
        self.download_button.bind(on_press=self.download_file)
        self.add_widget(self.download_button)

        self.priority_label = Label(text='Select Priority:')
        self.add_widget(self.priority_label)
        
        # Priority buttons
        priorities = ['low', 'medium', 'high', 'ultra']
        for pr in priorities:
            button = Button(text=pr.capitalize())
            button.bind(on_press=self.set_priority)
            self.add_widget(button)

    def set_priority(self, instance):
        self.priority = instance.text.lower()
        self.show_popup("Priority Selected", f"Priority set to {self.priority.capitalize()}")

    def download_file(self, instance):
        url = self.url_input.text
        filename = url.split('/')[-1]  # Extract filename from URL
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)

        if self.priority not in PRIORITY_MAP:
            self.show_popup("Error", "Invalid priority. Please select a valid priority.")
            return

        self.show_popup("Downloading", f"Downloading {filename} with {self.priority} priority...")

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            time.sleep(0.1 * PRIORITY_MAP[self.priority])  # Simulate download delay based on priority
            self.show_popup("Success", f"Downloaded {filename} successfully.")
            os.startfile(DOWNLOAD_FOLDER)
        except requests.RequestException as e:
            self.show_popup("Error", f"Failed to download file: {e}")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

class MyApp(App):
    def build(self):
        # Create requirements.txt and install requirements
        create_requirements_file()
        install_requirements()
        return DownloadManager()

if __name__ == '__main__':
    MyApp().run()
