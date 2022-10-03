# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

data = ['aaali','asddd','fsdfs']

def finder():
    list = []
    letter,order= input('type the letter and give the order\n').split()
    for value in data:
        while order != 6 :
            if letter==value[int(order)]:
                print('Great guess')
                list.append(letter)

            else: 'not in word'
            finder()
        if letter

        print(list)


if __name__ == '__main__':
    finder()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
