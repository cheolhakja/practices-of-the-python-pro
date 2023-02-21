def before_refactor():
    names = ['Larry', 'Curly', 'Moe']
    message = "The Three Stooges: "
    for index, name in enumerate(names):
        if index > 0:
            message += ', '
        if index == len(names) - 1: #원래는 ,만 붙히는데 인덱스2전에만 and를 붙힌다
            message += 'and '
        message += name
    print(message)

def join_names(names):  # <1>
    name_string = ''

    for index, name in enumerate(names):
        if index > 0 and len(names) > 2:
            name_string += ','
        if index > 0:
            name_string += ' '
        if index == len(names) - 1 and len(names) > 1:
            name_string += 'and '
        name_string += name
    return name_string


def introduce(title, names):  # <2>
    print(f'{title}: {join_names(names)}')

def after_refactor() :
    introduce('The Chipmunks', ['Alvin', 'Simon', 'Theodore'])

if __name__ == '__main__':
    after_refactor()
  