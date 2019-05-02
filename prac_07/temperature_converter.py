from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class TemperatureConverter(App):
    output_temperature = StringProperty()

    def build(self):
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperature_converter.kv')
        return self.root

    def calculate_temperature(self, text):
        temperature = self.convert_to_number(text)
        self.update_result(temperature)

    def convert_to_celsius(self):
        self.output_temperature = str(int(self.root.ids.celsius_input.text) * 9.0 / 5 + 32)
        self.root.ids.c_to_f_result.text = self.output_temperature

    def clear_text_celsius(self):
        self.root.ids.celsuis_input.text = ""

    def clear_text_fahrenheit(self):
        self.root.ids.fahrenheit_input.text = ""

    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


TemperatureConverter().run()

# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     elif choice == "F":
#         # TODO: Write this section to convert F to C and display the result
#         # Hint: celsius = 5 / 9 * (fahrenheit - 32)
#         # Remove the "pass" statement when you are done. It's a placeholder.
#         fahrenheit = float(input("Fahrenheit: "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print("Result: {:.2f} C".format(celsius))
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")
