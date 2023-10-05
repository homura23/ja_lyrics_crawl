import pandas as pd

# 从文本文件中读取数据
with open("lyrics_only_ja.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 创建包含ID、名称和歌词的列表
data_list = []
song_id = None
song_name = None
lyrics = []

# 解析文本数据并填充列表
for line in lines:
    line = line.strip()
    if line.isnumeric():
        if song_id is not None:
            data_list.append([song_id, song_name, " ".join(lyrics)])
        song_id = int(line)
        song_name = None
        lyrics = []
    elif song_name is None:
        song_name = line
    else:
        lyrics.append(line)

# 添加最后一个歌曲的数据
if song_id is not None:
    data_list.append([song_id, song_name, " ".join(lyrics)])

# 创建DataFrame
df = pd.DataFrame(data_list, columns=["ID", "name", "lyrics"])

# 将DataFrame保存为CSV文件
df.to_csv("lyrics_data.csv", index=False)

print("CSV文件已保存为lyrics_data.csv")
