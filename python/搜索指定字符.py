import os
import chardet

def read_text_file(file_path, encoding):
    if encoding:
        with open(file_path, 'r', encoding=encoding, errors='replace') as file:
            return file.readlines()
    else:
        with open(file_path, 'r', errors='replace') as file:
            return file.readlines()

def is_text_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read(1024)
            encoding = chardet.detect(raw_data)['encoding']
            return encoding is not None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return False

def find_text_in_files(folder_path, search_text):
    results = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if is_text_file(file_path):
                lines = read_text_file(file_path, chardet.detect(open(file_path, 'rb').read())['encoding'])
                for line_number, line in enumerate(lines, 1):
                    if search_text in line:
                        results.append((file_path, line_number, line.strip()))
    return results

# 提示用户输入所需的参数
parent_folder = input("请输入要搜索的父文件夹路径：")
search_text = input("请输入要搜索的文本：")
print('正在搜索...')

# 执行搜索指定文本的操作
search_results = find_text_in_files(parent_folder, search_text)

# 显示搜索结果
if search_results:
    print(f"搜索到 {len(search_results)} 处匹配：")
    for file_path, line_number, line_content in search_results:
        print(f"文件：{file_path}，行数：{line_number}，内容：{line_content}")
else:
    print("未找到匹配的内容。")

input("按任意键退出...")
exit()