word = input("Word: ")

frame_width = 30

padding = (frame_width - len(word) - 2) // 2  
top_bottom = "*" * frame_width
middle = "*" + " " * padding + word + " " * (frame_width - len(word) - 2 - padding) + "*"

print(top_bottom)
print(middle)
print(top_bottom)
