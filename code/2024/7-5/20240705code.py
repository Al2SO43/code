import os
import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def search_files_for_string(directory, search_string, include_extensions=None, exclude_extensions=None):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if include_extensions and file_extension not in include_extensions:
                continue
            if exclude_extensions and file_extension in exclude_extensions:
                continue

            file_path = os.path.join(root, file)
            try:
                encoding = detect_file_encoding(file_path)
                with open(file_path, 'r', encoding=encoding) as f:
                    line_number = 0
                    for line in f:
                        line_number += 1
                        if search_string == line.strip():
                            print(f"在文件 {file_path} 的第 {line_number} 行找到完全匹配的字符 '{search_string}'")
            except Exception as e:
                print(f"无法读取文件 {file_path}: {e}")

if __name__ == "__main__":
    directory = input("请输入要搜索的文件夹路径: ")
    search_string = input("请输入要搜索的字符: ")
    
    include_extensions = input("请输入要查询的文件后缀（多个后缀用逗号分隔，不输入则查询所有文件）: ")
    exclude_extensions = input("请输入不查询的文件后缀（多个后缀用逗号分隔，不输入则不排除任何文件）: ")
    
    include_extensions = include_extensions.split(',') if include_extensions else None
    exclude_extensions = exclude_extensions.split(',') if exclude_extensions else None
    
    search_files_for_string(directory, search_string, include_extensions, exclude_extensions)
    input("按任意键退出...")
