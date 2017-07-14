file_old = open('fractal_train_test.prototxt', mode='r', encoding='gbk')
file_new = open('cifar10-fractal_train_test.prototxt', mode='w', encoding='utf-8')

text = file_old.read()

file_new.write(text)