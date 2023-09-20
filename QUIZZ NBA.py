




import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox as mb


LARGE_FONT = ("ariel", 18)

class quiz_general(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, QUIZLEGENDES, QUIZTEAM, QUIZRECORDS, QUIZGARBAGE):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()





class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Sélectionne une catégorie :", font=LARGE_FONT, bg='#EEEEEE', fg='#263138')
        label.place(x=410, y=150)

        img = PhotoImage(file="Trashtalk.gif")
        can1 = Canvas(self, width=500, height=500, bg='#EEEEEE')
        item = can1.create_image(200, 200, image=img)
        can1.image=img
        can1.place(x=205, y=360)

        img2 = PhotoImage(file="ball.gif")
        can2 = Canvas(self, width=256, height=256, bg='#EEEEEE')
        item2 = can2.create_image(130, 130, image=img2)
        can2.image=img2
        can2.place(x=50, y=160)

        '''image_accueil.place(x=-100, y=50)'''

        app_title = tk.Label(self, text="Bienvenue dans le Quiz TTFL !",
                          width=50, bg='#BC0000', fg="White", font=("ariel", 22, "bold"))
        app_title.place(x=-40, y=2)

        button = tk.Button(self, text="LEGENDES",
                           command=lambda: controller.show_frame(QUIZLEGENDES),
                             width=15, bg='#232F35', fg="White", font=("ariel", 16, "bold"))
        button.place(x=450, y=200)

        button2 = tk.Button(self, text="EQUIPES",
                            command=lambda: controller.show_frame(QUIZTEAM),
                             width=15, bg='#232F35', fg="White", font=("ariel", 16, "bold"))
        button2.place(x=450, y=250)

        button3 = tk.Button(self, text="RECORDS",
                            command=lambda: controller.show_frame(QUIZRECORDS),
                             width=15, bg='#232F35', fg="White", font=("ariel", 16, "bold"))
        button3.place(x=450, y=300)

        button4 = tk.Button(self, text="GARBAGE TIME",
                            command=lambda: controller.show_frame(QUIZGARBAGE),
                             width=15, bg='#232F35', fg="White", font=("ariel", 16, "bold"))
        button4.place(x=450, y=350)






class QUIZLEGENDES(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(questionlegend)
        self.correct = 0

        button1 = tk.Button(self, text="Abandonner lachement",
                            command=lambda: controller.show_frame(StartPage),
                            width=20, bg='#BC0000', fg="White",
                            font=("ariel", 16, "bold"))
        button1.place(x=280, y=500)


    # Compteur de score
    def display_result(self):
        # comptage des mauvaises réponses
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        # calcul du score
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Message de fin donnant le score
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # Contrôle de la réponse donnée lors du clic sur NEXT
    def check_ans(self, q_no):
        # check si la réponse est correcte
        if self.opt_selected.get() == answerlegend[q_no]:
            return True

    # Vérifie réponse donnée, ajuste score, passe à la prochaine question (sauf si dernière)
    def next_btn(self):

        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            app.destroy()
        else:
            self.display_question()
            self.display_options()

    # BOUTONS
    def buttons(self):

        # Bouton NEXT
        next_button = tk.Button(self, text="Question suivante", command=self.next_btn,
                             width=15, bg='#BC0000', fg="White", font=("ariel", 16, "bold"))
        next_button.place(x=310, y=450)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in optionslegend[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # Affiche la question
    def display_question(self):
        q_no = tk.Label(self, text=questionlegend[self.q_no],fg='#263138', bg='#EEEEEE', width=60,
                     font=('ariel', 15, 'bold'), anchor='w')
        q_no.place(x=50, y=150)

    # Affiche le titre
    def display_title(self):
        title = tk.Label(self, text="Mettons la daronne dans le package !",
                      width=50, bg='#BC0000', fg="White", font=("ariel", 20, "bold"))
        title.place(x=-15, y=2)

    # Affichage propositions de réponses
    def radio_buttons(self):
        q_list = []
        y_pos = 230
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14), bg='#EEEEEE')
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return q_list






class QUIZTEAM(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(questionteam)
        self.correct = 0

        button1 = tk.Button(self, text="Abandonner lachement",
                            command=lambda: controller.show_frame(StartPage),
                            width=20, bg='#BC0000', fg="White",
                            font=("ariel", 16, "bold"))
        button1.place(x=280, y=500)

    # Compteur de score
    def display_result(self):
        # comptage des mauvaises réponses
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        # calcul du score
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Message de fin donnant le score
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # Contrôle de la réponse donnée lors du clic sur NEXT
    def check_ans(self, q_no):
        # check si la réponse est correcte
        if self.opt_selected.get() == answerteam[q_no]:
            return True

    # Vérifie réponse donnée, ajuste score, passe à la prochaine question (sauf si dernière)
    def next_btn(self):

        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            app.destroy()
        else:
            self.display_question()
            self.display_options()

    # BOUTONS
    def buttons(self):

        # Bouton NEXT
        next_button = tk.Button(self, text="Question suivante", command=self.next_btn,
                                width=15, bg='#BC0000', fg="White", font=("ariel", 16, "bold"))
        next_button.place(x=310, y=450)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in optionsteam[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # Affiche la question
    def display_question(self):
        q_no = tk.Label(self, text=questionteam[self.q_no], fg='#263138', bg='#EEEEEE', width=60,
                        font=('ariel', 15, 'bold'), anchor='w')
        q_no.place(x=50, y=150)

    # Affiche le titre
    def display_title(self):
        title = tk.Label(self, text="Mettons la daronne dans le package !",
                         width=50, bg='#BC0000', fg="White", font=("ariel", 20, "bold"))
        title.place(x=-15, y=2)

    # Affichage propositions de réponses
    def radio_buttons(self):
        q_list = []
        y_pos = 230
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self, text=" ", variable=self.opt_selected,
                                       value=len(q_list) + 1, font=("ariel", 14), bg='#EEEEEE')
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return q_list





class QUIZRECORDS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(questionrec)
        self.correct = 0

        button1 = tk.Button(self, text="Abandonner lachement",
                            command=lambda: controller.show_frame(StartPage),
                            width=20, bg='#BC0000', fg="White",
                            font=("ariel", 16, "bold"))
        button1.place(x=280, y=500)

    # Compteur de score
    def display_result(self):
        # comptage des mauvaises réponses
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        # calcul du score
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Message de fin donnant le score
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # Contrôle de la réponse donnée lors du clic sur NEXT
    def check_ans(self, q_no):
        # check si la réponse est correcte
        if self.opt_selected.get() == answerrec[q_no]:
            return True

    # Vérifie réponse donnée, ajuste score, passe à la prochaine question (sauf si dernière)
    def next_btn(self):

        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            app.destroy()
        else:
            self.display_question()
            self.display_options()

    # BOUTONS
    def buttons(self):

        # Bouton NEXT
        next_button = tk.Button(self, text="Question suivante", command=self.next_btn,
                                width=15, bg='#BC0000', fg="White", font=("ariel", 16, "bold"))
        next_button.place(x=310, y=450)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in optionsrec[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # Affiche la question
    def display_question(self):
        q_no = tk.Label(self, text=questionrec[self.q_no], fg='#263138', bg='#EEEEEE', width=60,
                        font=('ariel', 15, 'bold'), anchor='w')
        q_no.place(x=50, y=150)

    # Affiche le titre
    def display_title(self):
        title = tk.Label(self, text="Mettons la daronne dans le package !",
                         width=50, bg='#BC0000', fg="White", font=("ariel", 20, "bold"))
        title.place(x=-15, y=2)

    # Affichage propositions de réponses
    def radio_buttons(self):
        q_list = []
        y_pos = 230
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self, text=" ", variable=self.opt_selected,
                                       value=len(q_list) + 1, font=("ariel", 14), bg='#EEEEEE')
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return q_list





class QUIZGARBAGE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(questiongarb)
        self.correct = 0

        button1 = tk.Button(self, text="Abandonner lachement",
                            command=lambda: controller.show_frame(StartPage),
                            width=20, bg='#BC0000', fg="White",
                            font=("ariel", 16, "bold"))
        button1.place(x=280, y=500)

    # Compteur de score
    def display_result(self):
        # comptage des mauvaises réponses
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        # calcul du score
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Message de fin donnant le score
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # Contrôle de la réponse donnée lors du clic sur NEXT
    def check_ans(self, q_no):
        # check si la réponse est correcte
        if self.opt_selected.get() == answergarb[q_no]:
            return True

    # Vérifie réponse donnée, ajuste score, passe à la prochaine question (sauf si dernière)
    def next_btn(self):

        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            app.destroy()
        else:
            self.display_question()
            self.display_options()

    # BOUTONS
    def buttons(self):

        # Bouton NEXT
        next_button = tk.Button(self, text="Question suivante", command=self.next_btn,
                                width=15, bg='#BC0000', fg="White", font=("ariel", 16, "bold"))
        next_button.place(x=310, y=450)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in optionsgarb[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # Affiche la question
    def display_question(self):
        q_no = tk.Label(self, text=questiongarb[self.q_no], fg='#263138', bg='#EEEEEE', width=60,
                        font=('ariel', 15, 'bold'), anchor='w')
        q_no.place(x=50, y=150)

    # Affiche le titre
    def display_title(self):
        title = tk.Label(self, text="Mettons la daronne dans le package !",
                         width=50, bg='#BC0000', fg="White", font=("ariel", 20, "bold"))
        title.place(x=-15, y=2)

    # Affichage propositions de réponses
    def radio_buttons(self):
        q_list = []
        y_pos = 230
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self, text=" ", variable=self.opt_selected,
                                       value=len(q_list) + 1, font=("ariel", 14), bg='#EEEEEE')
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return q_list






### DEBUT DU CODE ###
# Chargement de la base de questions (json file)
with open('QUESTIONS_LEGEND.json') as flegend:
    data = json.load(flegend)
questionlegend = (data['queslegend'])
optionslegend = (data['proplegend'])
answerlegend = (data['anslegend'])

with open('QUESTIONS_TEAM.json') as fteam:
    data = json.load(fteam)
questionteam = (data['questeam'])
optionsteam = (data['propteam'])
answerteam = (data['ansteam'])

with open('QUESTIONS_RECORD.json') as frecord:
    data = json.load(frecord)
questionrec = (data['quesrec'])
optionsrec = (data['proprec'])
answerrec = (data['ansrec'])

with open('QUESTIONS_GARBAGE.json') as fgarbage:
    data = json.load(fgarbage)
questiongarb = (data['quesgarb'])
optionsgarb = (data['propgarb'])
answergarb = (data['ansgarb'])


app = quiz_general()


app.geometry("800x600")
app.title("Tu crois tout savoir sur le basket americain ?")
app.iconbitmap("ball.ico")
app.config(bg='#EEEEEE')


app.mainloop()