# Ако сортираме резултатите и винаги взимаме
# Най-малкия от бирата с най-малкия от картофите
# Което е същото да взимаме най-големия от бирата с най-големия от картофите
# Ще получим оптимален резултат
def max_score(beers, fries):
  beers = sorted(beers)
  fries = sorted(fries)

  result = 0

  for index in range(0, len(beers)):
    result += beers[index] * fries[index]

  return result

print(max_score([10, 11], [1, 5]) == 65)
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]) == 1442560)
