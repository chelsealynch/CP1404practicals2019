from kivy.app import App
from kivy.lang import Builder


class ScoreCalculator(App):
    def build(self):
        self.title = "Score Calculator"
        self.root = Builder.load_file('score_calculator.kv')
        return self.root

    def calculate_score(self):
        if self.root.ids.input_score.text < 50:
            self.root.ids.score_label.text = "Fail"
        elif self.root.ids.input_score.text >= 50:
            self.root.ids.score_label.text = "Pass"

    def clear_text(self):
        self.root.ids.score_label.text = "Enter your score"
        self.root.ids.input_score.text = ""


ScoreCalculator().run()
