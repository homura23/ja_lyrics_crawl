import pickle

# 读取pkl文件
with open('lyric_ids_titled.pkl', 'rb') as file:
    # 使用UTF-8编码读取文本信息
    data = pickle.load(file, encoding='utf-8')

# 将文本信息写入out2.txt文件
with open('lyric_ids_titled.txt', 'w', encoding='utf-8') as file:
    for item in data:
        for value in item.values():
            file.write(str(value) + '\n')

# 显示文本信息
for item in data:
    for value in item.values():
        print(value)

