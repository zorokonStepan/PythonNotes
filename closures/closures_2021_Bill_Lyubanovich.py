# Prostoy_Python_Sovremenny_stil_programmirovania_2021_Bill_Lyubanovich

def knights(saying):

    def inner():
        return "We are the knights who say: '%s'" % saying

    return inner


if __name__ == "__main__":
    a = knights('Duck')
    b = knights('Hasenpfeffer')

    print(a)  # <function knights.<locals>.inner at 0x000001756809FF60>
    print(b)  # <function knights.<locals>.inner at 0x00000175680A0860>

    print(a())  # We are the knights who say: 'Duck'
    print(b())  # We are the knights who say: 'Hasenpfeffer'
