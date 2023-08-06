import time
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

kivy.require("1.11.1")


class YoutubePlayer(App):
    def build(self):
        self.title = "YouTube Player"
        self.layout = BoxLayout(orientation="vertical", spacing=10)
        self.url_input = TextInput(
            multiline=False, hint_text="Enter YouTube URL", size_hint_y=None, height=50
        )
        self.play_button = Button(
            text="Play Video", size_hint_y=None, height=50, on_press=self.play_video
        )
        self.answer_input = TextInput(
            multiline=False, hint_text="Answer here", size_hint_y=None, height=50
        )
        self.layout.add_widget(self.url_input)
        self.layout.add_widget(self.answer_input)
        self.layout.add_widget(self.play_button)
        return self.layout

    def play_video(self, instance):
        youtube_url = self.url_input.text
        if "youtube.com" in youtube_url or "youtu.be" in youtube_url:
            webbrowser.open(youtube_url)
            driver = webdriver.Chrome()
            time.sleep(5)
            like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.yt-spec-button-shape-next")))
            aria_pressed = like_button.get_attribute("aria-pressed")
            print(f"aria-pressed value: {aria_pressed}")
            time.sleep(55)


        else:
            self.url_input.text = "Invalid YouTube URL"

    


if __name__ == "__main__":
    YoutubePlayer().run()