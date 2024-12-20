items = []
while True:
    item = input("Введите элемент списка (или нажмите Enter для завершения): ")
    if item == "":
        break
    items.append(item)

if not items:
    formatted_string = ""
elif len(items) == 1:
    formatted_string = items[0]
else:
    formatted_string = ", ".join(items[:-1]) + " и " + items[-1]

print(formatted_string)