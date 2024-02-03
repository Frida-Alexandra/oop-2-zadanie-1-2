from pprint import pprint

print("№1")
print()
cook_book = {}
with open("recipes.txt", "r", encoding="utf-8") as file:
    for string in file:
        ingredient = file.readline()
        menu_list = []
        for i in range(int(ingredient)):
            x = file.readline().rstrip("\n").split(" | ")  # в список
            consistent = {
                "ingridient_name": x[0],
                "quantity": int(x[1]),
                "measure": x[2],
            }  # собираем в словарь
            menu_list.append(consistent)
        file.readline()  # читать пустую строку
        cook_book[string.strip()] = menu_list  # в словарь
    print("cook_book = ")
    pprint(cook_book)
    print()
    print("№2")
    print()

    def get_shop_list_by_dishes(dishes, person_count):
        bluda = []
        itog = {}

        for i in dishes:
            bluda += cook_book[i]

        for i in bluda:
            j = 1
            if i["ingridient_name"] not in itog.keys():
                itog.update(
                    {
                        i["ingridient_name"]: {
                            "measure": i["measure"],
                            "quantity": i["quantity"] * person_count,
                        }
                    }
                )
            else:
                j += 1
                itog.update(
                    {
                        i["ingridient_name"]: {
                            "measure": i["measure"],
                            "quantity": (i["quantity"] * j) * person_count,
                        }
                    }
                )
        return pprint(itog)


get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
