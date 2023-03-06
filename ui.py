from logger import data_input,print_data,filter_data,delete_data,switch_data
def interface():
    print("""Ввыберите режи работы:
             1-запись данных,
             2-вывод данных,
             3-поиск данных по параметрам, 
             4-удаление одной записи,
             5-изменение данных
             """)
    command_number=int(input("Введите номер команды: "))
    while command_number<1 or command_number>5:
        command_number=int(input("Введите корректный номер команды: "))
    if command_number==1:
        data_input()
    elif command_number==2:
        print_data()
    elif command_number==3:
        print("Введите параметры поиска через ';' :")
        filter_str=input()
        filter_data(filter_str)
    elif command_number==4:
        print("Введите параметры поиска через ';' :")
        delete_str=input()
        delete_data(delete_str)
    elif command_number==5:
        print("Введите строчку, которую хотите заменить через ';' :")
        old_str=input()
        print("Введите строчку, на которую хотите заменить через ';' :")
        new_str=input()
        switch_data(old_str,new_str)


        
