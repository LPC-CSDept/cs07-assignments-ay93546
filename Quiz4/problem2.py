p_count = 0
while True:
  user_input = input("Enter string:")
  if user_input == ("stop"):
    break
  elif user_input.find("p") != -1:
    p_count += 1
print(p_count)