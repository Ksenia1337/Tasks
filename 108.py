def convert_volume(amount, unit):
    """
    Converts a given volume to a string representation using cups, tablespoons, and teaspoons.

    Args:
        amount: The volume to convert.
        unit: The unit of the volume ('cup', 'tablespoon', or 'teaspoon').

    Returns:
         A string representing the volume in the specified format.
    """

    if unit == "cup":
        teaspoons = amount * 16 * 3
    elif unit == "tablespoon":
        teaspoons = amount * 3
    elif unit == "teaspoon":
        teaspoons = amount
    else:
      return "Invalid unit"

    cups = teaspoons // (16 * 3)
    teaspoons %= (16 * 3)
    tablespoons = teaspoons // 3
    teaspoons %= 3


    output = []
    if cups > 0:
        output.append(f"{cups} cup{'s' if cups > 1 else ''}")
    if tablespoons > 0:
        output.append(f"{tablespoons} tablespoon{'s' if tablespoons > 1 else ''}")
    if teaspoons > 0:
        output.append(f"{teaspoons} teaspoon{'s' if teaspoons > 1 else ''}")

    return ", ".join(output) if output else "0 teaspoons"


if __name__ == "__main__":
  test_cases = [
      (59, "teaspoon"),
      (2, "cup"),
      (20, "tablespoon"),
      (0, "teaspoon"),
      (16, "tablespoon"),
      (1, "cup"),
      (120, "teaspoon"),
      (1, "invalid"),
      (1, "tablespoon")

  ]
  for amount, unit in test_cases:
    print (f"{amount} {unit} is equal to {convert_volume(amount, unit)}")