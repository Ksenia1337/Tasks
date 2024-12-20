points = []
while True:
    x_str = input("Введите координату x (или нажмите Enter для завершения): ")
    if not x_str:
        break
    y_str = input("Введите координату y: ")
    points.append((float(x_str), float(y_str)))

n = len(points)

if n < 2:
    print("Недостаточно точек для расчета линии наилучшего соответствия.")
else:
    sum_x = sum(x for x, _ in points)
    sum_y = sum(y for _, y in points)
    sum_xy = sum(x * y for x, y in points)
    sum_x2 = sum(x ** 2 for x, _ in points)

    m_numerator = n * sum_xy - sum_x * sum_y
    m_denominator = n * sum_x2 - sum_x ** 2

    if m_denominator == 0:
      print("Невозможно вычислить наклон, деление на ноль.")
    else:
      m = m_numerator / m_denominator
      x_mean = sum_x / n
      y_mean = sum_y / n
      b = y_mean - m * x_mean

      print(f"y = {m:.2f}x + {b:.1f}")