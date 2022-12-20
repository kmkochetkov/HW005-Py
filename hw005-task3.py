# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
#
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

#

# Кодирование данных
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

#  Декодирование данных
def rle_decoder(data):
    decode = ''
    count=''
    for char in data:
        if char.isdigit():
            count+= char
        else:
            decode += char *int(count)
            count = ''
    return decode


print('Исходные данные в файле "hw005-task3_data.txt"')
file1 = open('hw005-task3_data.txt','r')
dat = file1.readline()

#dat = ('aaabbbbccbbb')
#
print('Данные, запакованные методом RLE в файле "hw005-task3_zip.txt"')
file2 = open('hw005-task3_zip.txt','w')
file2.write(rle_encode(dat))
file1.close()
file2.close()

print('Восстановленные данные в файле "hw005-task3_unzip.txt"')
file2 = open('hw005-task3_zip.txt','r')
file3 = open('hw005-task3_unzip.txt','w')
dat = file2.readline()
file3.write(rle_decoder(dat))
file2.close()
file3.close()


