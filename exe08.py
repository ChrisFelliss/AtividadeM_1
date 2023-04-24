def funcao(num):
    try:
        int(num)
    except:
        return Exception
    if type(num) == str:
        return Exception
    elif num >= 0:
        return True
    elif num < 0:
        return False

assert funcao(float("inf")) == Exception