import model
import view

def start():

    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()

        match choice:

            case 1:
                model.open_file()
                view.show_massage('Файл открыт')

            case 2:
                model.save_file()
                view.show_massage('Файл сохранен')

            case 3:
                view.show_contacts(pb,'Телефонная книга пуста')

            case 4:
                model.add_contact(view.add_contact())
                view.show_massage('Контакт добавлен')

            case 5:
                if view.show_contacts(pb,'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер контакта, который хотите изменить: ')
                    contact = view.change_contact(pb,index)
                    model.change_contact(contact,index)
                    view.show_massage(f'Контакт {model.get_phone_book()[index-1].get("name")} изменен')

            case 6:
                search = view.input_serch('Введите искомый контакт: ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Котакт не найден')

            case 7:
                delcont = view.input_serch('Введите контакт, который хотите удалить: ')
                del_list = model.find_contact(delcont)
                if view.show_contacts(del_list, 'Котакт не найден'):
                    del_num = view.input_del('Введите enter, чтобы удалить все выбранные контакты или номер контакта: ', len(del_list))
                    model.del_contact(del_list,del_num)
                    view.show_massage(f'Контакт удален')

            case 8:
                yes_or_no = view.input_yn('Хотите сохранить файл (Y/N) ? : ')
                if yes_or_no == 'y':
                    model.save_file()
                    view.show_massage('Файл сохранен')
                view.show_massage('Конец работы')
                return





