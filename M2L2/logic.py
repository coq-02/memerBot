# # This is how you can read the whole file
# f = open('text.txt', 'r', encoding='utf-8')
# text = f.read()
# print(text)
# f.close()

# # This is how you can change the whole file
# f = open('text.txt', 'w', encoding='utf-8')
# text = 'this is the changed text'
# f.write(text)
# f.close()

# # This is how you can add text to the file
# f = open('text.txt', 'a', encoding='utf-8')
# text = 'this is added text'
# f.write(text)
# f.close()

# Short form of read
with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())