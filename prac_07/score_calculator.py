from kivy.app import App
from kivy.lang import Builder


class ScoreCalculator(App):
    def build(self):
        self.title = "Score Calculator"
        self.root = Builder.load_file('score_calculator.kv')
        return self.root

    def convert_score(self):
        try:
            value = int(self.root.ids.input_score.text)
            return value
        except ValueError:
            return 0

    def calculate_score(self):
        value = self.convert_score()
        if value < 50:
            self.root.ids.result_label.text = "Fail"
        elif value >= 50:
            self.root.ids.result_label.text = "Pass"

    def clear_text(self):
        self.root.ids.result_label.text = "Enter your score"
        self.root.ids.input_score.text = ""


ScoreCalculator().run()
