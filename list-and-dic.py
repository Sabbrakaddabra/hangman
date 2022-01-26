def run():
    my_list = [1, "hello", True, 4,5]
    my_dict = {"fristname": "Franco", "lastname":"Passerini Saud"}

    super_list = [
        {"fristname": "Franco", "lastname":"Passerini Saud"},
        {"fristname": "Maria Victoria", "lastname":"Passerini Alcaraz"},
        {"fristname": "Angie", "lastname":"Alcaraz"},
        {"fristname": "Julieta", "lastname":"Passerini"},
        {"fristname": "Bautista", "lastname":"Passerini"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums":[0.1,4.5,6.43]
    }    

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i.items())

if __name__=='__main__':
    run()