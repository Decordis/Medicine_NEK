def x_ray():
    ren = 'Чтобы мы смогли оценить все ЗА и ПРОТИВ нужен рентген!'
    print(ren)
    while True:
        ren = input("Сделали рентген? 1:Да 2: Нет")

        if ren == '1':
            break
        elif ren == '2':
            print("Сделайте рентген!")
            continue
        else:
            print(f'Я не понял Ваш ответ {ren}, давайте ещё раз!')


