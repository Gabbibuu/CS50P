def convert(input):
  return input.replace(":)", "🙂").replace(":(", "🙁")

def main():
  print(convert(input()))

main()