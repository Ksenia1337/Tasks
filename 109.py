print("Магические даты в 20 веке:")
for год in range(1901, 2001):
    for месяц in range(1, 13):
      if месяц in [4, 6, 9, 11]:
          дней_в_месяце = 30
      elif месяц == 2:
          if (год % 4 == 0 and год % 100 != 0) or (год % 400 == 0):
              дней_в_месяце = 29
          else:
              дней_в_месяце = 28
      else:
         дней_в_месяце = 31
      for день in range (1, дней_в_месяце +1):
          if not (1 <= месяц <= 12 and 1 <= день <= 31):
              continue # Пропускаем текущую итерацию
          последние_две_цифры = год % 100
          if день * месяц == последние_две_цифры:
              print(f"{день:02d}/{месяц:02d}/{год}")