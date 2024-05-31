from tkinter import *

class Clin_rec:
    def recomendation(self):
        print("Также рекомендую ознакомиться с проектом клинических рекомендаций по НЭК")
        print('https://neonatology.pro/wp-content/uploads/2014/08/Protokol_NEC_2014.pdf')

        while True:
            try:
                ask = int(input("Прислать QR-code на клин. рекомендации? 1-Да | 2-Нет"))
                if ask == 1:
                    print('Хорошо, скидываю QR-qode!')
                    window = Tk()
                    qr_code = PhotoImage(file='NEK.png')
                    Label(window, image=qr_code).pack()
                    mainloop()
                    break
                elif ask == 2:
                    break
                else:
                    print('Неправильное число')
                    continue
            except ValueError:
                print('Я не понял вас, повторите попытку!')
                continue
