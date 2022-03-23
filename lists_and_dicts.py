def run():
    my_list=[1, "Hello", True, 4.5]
    my_dict={"firstname": "Ian", "lastname":"Oliva"}

    super_list = [
        {"firstname": "Ian", "lastname":"Oliva"},
        {"firstname": "Titi", "lastname":"Bb"},
        {"firstname": "Facundo", "lastname":"García"},
        {"firstname": "Benito", "lastname":"Martinez"},
        {"firstname": "Edgar", "lastname":"Oliva"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6-43]
    }

    for key, value in super_dict.items():
        print(key,"-",value)
    print("\n")

    for values in super_list:
        for key,value in values.items():
            print(key,"-",value)
    print("\n")
    
    for values in super_list:
        print(values["firstname"],values["lastname"])
    print("\n")


if __name__== '__main__':
    run()