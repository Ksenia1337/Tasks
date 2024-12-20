from random import randrange
## Генерируем стандартную колоду карт с четырьмя мастями и 13 номиналами в каждой
# @return список карт с каждой картой, представленной двумя символами
def createDeck():
 # Создаем список для хранения карт
 cards = []
 # Проходим по всем мастям и номиналам
 for suit in ["s", "h", "d", "c"]:
      for value in ["2", "3", "4", "5", "6", "7", "8", "9", \
 "T", "J", "Q", "K", "A"]:
 # Генерируем карту и добавляем ее в колоду
              cards.append(value + suit)
 # Возвращаем целую колоду
 return cards
## Тасуем колоду, переданную в функцию в качестве параметра
# @param cards – список карт для тасования
# @return (None)
def shuffle(cards):
 # Проходим по картам
 for i in range(0, len(cards)):
 # Выбираем случайный индекс между текущим индексом и концом списка
     other_pos = randrange(i, len(cards))
 # Меняем местами текущую карту со случайно выбранной
 temp = cards[i]
 cards[i] = cards[other_pos]
 cards[other_pos] = temp
# Отображаем колоду до и после тасования
def main():
 cards = createDeck()
 print("Исходная колода карт: ")
 print(cards)
 print()
 shuffle(cards)
 print("Перетасованная колода карт: ")
 print(cards)
# Вызываем основную функцию, только если программа не была импортирована как модуль
if __name__ == "__main__":
 main()