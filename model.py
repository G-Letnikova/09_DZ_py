phone_book = []
path = 'phone_book.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        phone_book.append(contact)

def get_phone_book():
    return phone_book

def add_contact(contact):
    phone_book.append(contact)

def change_contact(contact: dict, index: int) :
    phone_book.pop(index-1)
    phone_book.insert(index-1,contact)


def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def find_contact(search: str) -> list[dict]:
    res = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                res.append(contact)
    return res

def del_contact(del_list: list[dict], num: int):
    if num:
        phone_book.pop(phone_book.index(del_list[num-1]))
    else:
        for contact in del_list:
            for cont in phone_book:
                if contact == cont:
                    phone_book.pop(phone_book.index(cont))