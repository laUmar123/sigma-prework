def calculate_max_and_min(numbers: list):
  max = numbers[0]
  min = numbers[0]

  for i in numbers:
    if i > max:
      max = i

    if i < min :
      min = i

  return [min, max]