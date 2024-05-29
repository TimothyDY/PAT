import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


def scale_satisfaction(event):
    value = satisfaction_var.get()
    if value == 1:
        satisfaction_label.config(text = "Very Unsatisfied")
    elif value == 2:
        satisfaction_label.config(text = "Somewhat Unsatisfied")
    elif value == 3:
        satisfaction_label.config(text = "Neutral")
    elif value == 4:
        satisfaction_label.config(text = "Somewhat Satisfied")
    elif value == 5:
        satisfaction_label.config(text = "Very Satisfied")

def scale_fun(event):
    value = fun_var.get()
    if value == 1:
        fun_label.config(text = "Very Unfun")
    elif value == 2:
        fun_label.config(text = "Somewhat Unfun")
    elif value == 3:
        fun_label.config(text = "Neutral")
    elif value == 4:
        fun_label.config(text = "Somewhat Fun")
    elif value == 5:
        fun_label.config(text = "Very Fun")

def submit_survey():
    survey_window.destroy()
    thank_you_window()

def thank_you_window():
    thank_you_window = tk.Toplevel(root)
    thank_you_window.title("Thank You!")
    thank_you_window.iconphoto(False, tk.PhotoImage(file = 'C:\\Users\\JLH\\Desktop\\Coding\\Python\\PAT\\Pokémon_UNITE_logo.png'))
    thank_you_label = tk.Label(thank_you_window, text = "Thank you for taking your time and filling out our questionnaire! We will try our best to improve the Pokémon UNITE experience")
    thank_you_label.pack(padx = 20, pady = 20)

root = tk.Tk()
root.title("Pokémon UNITE Season 19 Questionnaire")
root.iconphoto(False, tk.PhotoImage(file = 'C:\\Users\\JLH\\Desktop\\Coding\\Python\\PAT\\Pokémon_UNITE_logo.png'))
style = Style(theme = 'minty')

survey_window = ttk.Frame(root, padding="20")
survey_window.pack(fill = "both", expand = True)

question1_label = ttk.Label(survey_window, text = "1. How satisfied are you with the current ranked system")
question1_label.pack(pady = (10, 5))
satisfaction_options = ["Very unsatisfied", "Somewhat unsatisfied", "Neutral", "Satisfied", "Very satisfied", "I don't play ranked matches"]
question1_combobox = ttk.Combobox(survey_window, values =satisfaction_options)
question1_combobox.pack(pady = (0, 10))

question2_label = ttk.Label(survey_window, text = "2. How did you find out about Pokémon UNITE?")
question2_label.pack(pady = (10, 5))
social_media_options = ["Facebook", "Instagram", "Twitter", "Youtube", "Tiktok", "Word of Mouth", "Other"]
question2_combobox = ttk.Combobox(survey_window, values =social_media_options)
question2_combobox.pack(pady = (0, 10))

question3_label = ttk.Label(survey_window, text = "3. How satisfied are you with the recent balance patches?")
question3_label.pack(pady = (10, 5))
satisfaction_var = tk.IntVar()
scale = ttk.Scale(survey_window, from_=1, to=5, orient = "horizontal", variable = satisfaction_var, command = scale_satisfaction)
scale.pack(pady = (0, 10))
satisfaction_label = ttk.Label(survey_window, text = "Very Unsatisfied")
satisfaction_label.pack()

question4_label = ttk.Label(survey_window, text = "4. How would you rate your experience ?")
question4_label.pack(pady = (10, 5))
fun_var = tk.IntVar()
scale = ttk.Scale(survey_window, from_=1, to=5, orient = "horizontal", variable = fun_var, command = scale_fun)
scale.pack(pady = (0, 10))
fun_label = ttk.Label(survey_window, text = "Very Unfun")
fun_label.pack()

question5_label = ttk.Label(survey_window, text = "5. Write anymore improvements to enhance the overall enjoyment in the game")
question5_label.pack(pady = (10, 5))
question5_text = tk.Text(survey_window, height = 5)
question5_text.pack(pady = (0, 10))

submit_button = ttk.Button(survey_window, text = "Submit", command=submit_survey)
submit_button.pack(pady = (10, 20))

root.mainloop()