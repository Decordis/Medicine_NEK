
from get_recom import Clin_rec
from results import Result, Gets
from sympt import Theory
from symptfunc import First_sym, Second_sym, Third_sym
from xray import x_ray


class Get_programm:
    def greet(self):
        print("|-------------------------------------|")
        print("| Приветсвую, дорогой Коллега!! :)    |")
        print("|------------------------------------ |")
        print("| Я здесь, чтобы помочь Вам с НЭК     |")
        print("| Не волнуйтесь! Всё довольно просто  |")
        print("--------------------------------------|")
        print("| Я предлагаю варианты ответов,       |\n"
              "| а Вам нужно вписать лишь число!     |")
        print("| Проведем анализ и выясним,          |\n"
              "| какова вероятность развития НЭК     |")
        print("|-------------------------------------|")

        print("Для Вашего удобства, я могу показать подробную инструкцию! :)")





    def get_analis(self):
        text = "Выберите число 1 - Инструкция | 2 - Начать анализ | 3 - Выход из программы: "
        while True:
            try:
                answer = int(input(text))
                if answer == 1:
                    self.instruction()
                    continue
                elif answer == 2:
                    self.question1()
                    break
                elif answer == 3:
                    quit()
                else:
                    print(f'Простите, но я не понял Ваш ответ {answer}, давайте ещё раз')
                    continue
            except ValueError:
                print('Пиксельный ступор! Я понимаю только числа!')
                continue


    def instruction(self):
        print("-"*77)
        print('Данная программа выглядит, как тест, сейчас всё рассмотрим на примере\n')

        print("Перед Вами будет вопрос: 'Давайте проанализируем рентгенологическую картину'")
        print("Что из этого? ")
        print("'Варианты ответов: '")
        ren_empty = '0: ничего из этого'
        ren_sympt_1A = ' | '.join(Theory.I_A.get('rengen'))
        ren_sympt_1B = ' | '.join(Theory.I_B.get('rengen'))
        ren_sympt_2A = ' | '.join(Theory.II_A.get('rengen'))
        ren_sympt_2B = ' | '.join(Theory.II_B.get('rengen'))
        ren_sympt_3A = ' | '.join(Theory.III_A.get('rengen'))
        ren_sympt_3B = ' | '.join(Theory.III_B.get('rengen'))
        print(f' {ren_empty}\n {ren_sympt_1A}\n {ren_sympt_1B}\n {ren_sympt_2A}\n'
              f' {ren_sympt_2B}\n {ren_sympt_3A}\n {ren_sympt_3B} \n')

        print("'Ваш ответ:' Где Вы указываете наиболее подходящий симптом")
        print("!"*27, "ВАЖНО", "!"*27, sep='')
        print("В ответ Вы указываете ЦИФРУ, без точек, запятых, пробелов и так далее")


    def question1(self):
        while True:
            x_ray()
            First_sym().ot_symptoms()
            Second_sym().ab_symptoms()
            Third_sym().ren_symptoms()
            Result().get_result()
            Gets().get_alltherapy()
            Clin_rec().recomendation()
            break

    def close(self):
        text = ("Отлично! Надеюсь, у меня получилось помочь Вам :)\n"
                "Также Вы можете ознакомиться с другими клиническими рекомендациями на сайте:\n"
                " https://neonatology.pro/resursnyiy-tsentr/protokolyi/\n"
                "Для повторного анализа перезапустите программу \n")
        print(text)
        while True:
            try:
                answer = int(input('Нажмите 1 для выхода из программы:'))
                if answer == 1:
                  break
                else:
                    print(f'Простите, но я не понял Ваш ответ {answer}, давайте ещё раз')
                    continue
            except ValueError:
                print('Пиксельный ступор! Я понимаю только числа!')
                continue


    def start(self):
        self.greet()
        self.get_analis()
        self.close()
