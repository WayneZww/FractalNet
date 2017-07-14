file_old = open('train.crox.prototxt', mode='r', encoding='utf-16-le')
file_new = open('train.prototxt', mode='w', encoding='utf-8')

text = file_old.read()

file_new.write(text)