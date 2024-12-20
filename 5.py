small_bottles = int(input("Количество бутылок объемом 1 литр и меньше: "))
large_bottles = int(input("Количество бутылок объемом больше 1 литра: "))
total = small_bottles * 0.10 + large_bottles * 0.25
print(f"Сумма, которую можно выручить: ${total:.2f}")
