from sympt import Theory

_all_ = []
class First_sym:
    @staticmethod
    def ot_symptoms():
        global _all_
        print("хорошо, давайте проанализируем общую клиническую картину")
        print('Что из этого?')
        sym_empty = '0: ничего из этого'
        sympt_1A = ' | '.join(Theory.I_A.get('symptoms'))
        sympt_2A = ' | '.join(Theory.II_A.get('symptoms'))
        sympt_2B = ' | '.join(Theory.II_B.get('symptoms'))
        sympt_3A = ' | '.join(Theory.III_A.get('symptoms'))
        sympt_3B = ' | '.join(Theory.III_B.get('symptoms'))
        print(f' {sym_empty}\n {sympt_1A}\n {sympt_2A}\n'
              f' {sympt_2B}\n {sympt_3A}\n {sympt_3B} ')
        while True:
            try:
                the_sym = input("Введите цифру:")
                if int(the_sym) in range(0, 7):
                    if (the_sym in sympt_1A or the_sym in sympt_2A or the_sym in sympt_2B
                            or the_sym in sympt_3A or the_sym in sympt_3B or
                            the_sym in sym_empty):
                        _all_.append(int(the_sym))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")

class Second_sym:
    @staticmethod
    def ab_symptoms():
        global _all_
        print("хорошо, давайте проанализируем абдоминальные симптомы")
        print('Что из этого?')
        ab_empty = '0: ничего из этого'
        ab_sympt_1A = ' | '.join(Theory.I_A.get('abd_symptoms'))
        ab_sympt_1B = ' | '.join(Theory.I_B.get('abd_symptoms'))
        ab_sympt_2A = ' | '.join(Theory.II_A.get('abd_symptoms'))
        ab_sympt_2B = ' | '.join(Theory.II_B.get('abd_symptoms'))
        ab_sympt_3A = ' | '.join(Theory.III_A.get('abd_symptoms'))
        ab_sympt_3B = ' | '.join(Theory.III_B.get('abd_symptoms'))
        print(f' {ab_empty}\n {ab_sympt_1A}\n {ab_sympt_1B}\n {ab_sympt_2A}\n'
              f' {ab_sympt_2B}\n {ab_sympt_3A}\n {ab_sympt_3B} ')
        while True:
            try:
                the_sym = input("Введите цифру:")
                if int(the_sym) in range(0, 7):
                    if (the_sym in ab_sympt_1A or the_sym in ab_sympt_1B or the_sym in ab_sympt_2A or
                            the_sym in ab_sympt_2B or the_sym in ab_sympt_3A or the_sym in ab_sympt_3B or
                            the_sym in ab_empty):
                        _all_.append(int(the_sym))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")
                continue


class Third_sym:
    @staticmethod
    def ren_symptoms():
        global _all_
        print("хорошо, теперь проанализируем рентгенологическую картину")
        print('Что из этого?')
        ren_empty = '0: ничего из этого'
        ren_sympt_1A = ' | '.join(Theory.I_A.get('rengen'))
        ren_sympt_2A = ' | '.join(Theory.II_A.get('rengen'))
        ren_sympt_2B = ' | '.join(Theory.II_B.get('rengen'))
        ren_sympt_3A = ' | '.join(Theory.III_A.get('rengen'))
        ren_sympt_3B = ' | '.join(Theory.III_B.get('rengen'))
        print(f' {ren_empty}\n {ren_sympt_1A}\n {ren_sympt_2A}\n'
              f' {ren_sympt_2B}\n {ren_sympt_3A}\n {ren_sympt_3B} ')
        while True:
            try:
                the_sym = input("Введите цифру:")
                if int(the_sym) in range(0, 7):
                    if (the_sym in ren_sympt_1A or the_sym in ren_sympt_2A or the_sym in ren_sympt_2B or
                            the_sym in ren_sympt_3A or the_sym in ren_sympt_3B or
                            the_sym in ren_empty):
                        _all_.append(int(the_sym))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")
