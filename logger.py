from data_create import name_data,surname_data,phone_data,adres_data
file_name="data.txt"
def print_data():
    print("Вывод данных из файла")
    with open(file_name,'r',encoding="utf-8") as file:
        data_list=file.readlines()
        for element in data_list:
            print(element)

def data_input():
    print("Введите данные для добаление в файл")
    name=name_data()
    surname=surname_data()
    phone=phone_data()
    adres=adres_data()
    with open(file_name,'a',encoding="utf-8") as file:
        file.write(f"\n{name};{surname};{phone};{adres}")

def filter_data(data_string):
    with open(file_name,'r',encoding="utf-8") as file:
        data_list=file.readlines()
        if ";" in data_string:
            list_filgers=data_string.split(";")
        else:
            list_filgers=[data_string]
        is_found=False
        for element in data_list:
            temp_record=element.split(";")
            count=0
            for record in temp_record:
                for element_fingers in list_filgers:
                    if (element_fingers.lower() in record.lower()) and len(element_fingers)==len(record):
                        count+=1
            if count==len(list_filgers):
                print(element)
                is_found=True
    if not is_found:
        print("Таких записей не нашли(")

def delete_data(data_str):
    if ";" in data_str:
        list_filgers=data_str.split(";")
    else:
        list_filgers=[data_str]
    with open(file_name,'r',encoding="utf-8") as file:
        data_list=file.readlines()
    with open(file_name,'w',encoding="utf-8") as file:   
        
        for element in data_list:
            temp_record=element.split(";")
            count=0
            for record in temp_record:
                for element_fingers in list_filgers:
                    if (element_fingers.lower() in record.lower()) and len(element_fingers)==len(record):
                        count+=1
            if count!=len(list_filgers):
                file.write(element)
def switch_data(old_str,new_str):
    if ";" in old_str:
        list_filgers=old_str.split(";")
    else:
        list_filgers=[old_str]
    with open(file_name,'r',encoding="utf-8") as file:
        data_list=file.readlines()
    with open(file_name,'w',encoding="utf-8") as file:   
        for element in data_list:
            temp_record=element.split(";")
            count=0
            for record in temp_record:
                for element_fingers in list_filgers:
                    if (element_fingers.lower() in record.lower()) and len(element_fingers)==len(record):
                        count+=1
            if count==len(list_filgers):
                file.write(new_str)
            else:
                file.write(element)
            
   





                        