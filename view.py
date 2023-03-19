import text_fields

def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n'))-1

    while True:
        choice = input('Выберете пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Введите число от 1 до {length_menu}')


def show_contacts(book: list[dict], error_massage: str):
    if not book:
        print(error_massage)
        return False
    else:
        for i, contact in enumerate(book,1):
            print(f"{i}.  {contact.get('name'):<15} "
                  f"{contact.get('phone'):<15} "
                  f"{contact.get('comment'):<15}")
        return True

def add_contact() -> dict:
    name = input('Имя: ')
    phone = input('Телефон: ')
    comment = input('Комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def input_index(massage: str):
    return int(input(massage))


def change_contact(book: list[dict], index: int):
    print('Введите новые данные или enter: ')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}

def show_massage(massage: str):
    print('-' * len(massage))
    print(massage)
    print('-' * len(massage))

def input_serch(massage):
    return input(massage)

def input_yn(massage):
    return input(massage).lower()

def input_del(massage: str, len_del_list) -> int:
    num = input(massage)
    if num == '':
        return 0
    while True:
        if num.isdigit() and 0 < int(num) <= len_del_list:
            return int(num)
        else:
            num = input(massage)

