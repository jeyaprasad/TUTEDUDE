text1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(text1 + "\n")
print("Data successfully written to output.txt.\n")

text2 = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(text2 + "\n")
print("Data successfully appended.\n")

print("Final content of output.txt:")
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())
