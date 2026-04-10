def make_payment(P):
    """
    verification of the ability to make a payment
    :param P: the amount of money
    :return: the result, is it possible or not
    """
    try:
        P = float(P)

        if 20 <= P <= 1000:
            print('Успех')
        else:
            print('Повторить попытку')

    except(TypeError, ValueError):
        print('Не удалось преобразовать в число')

make_payment(800)
