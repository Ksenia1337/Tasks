num_souvenirs = int(input("Введите количество сувениров: "))
num_trinkets = int(input("Введите количество безделушек: "))
weight_souvenir = 75
weight_trinket = 112
total_weight = (num_souvenirs * weight_souvenir) + (num_trinkets * weight_trinket)
print(f"Общий вес посылки составляет", (total_weight), "граммов.")
