import os
import re

def replace_br_tags(directory):
    # 定义正则表达式来匹配<br>标签
    br_pattern = re.compile(r'<br>')

    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') or file.endswith('.htm'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 替换<br>标签为<br />
                new_content = br_pattern.sub('<br />', content)

                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    directory = input("请输入要检测的目录路径: ")
    replace_br_tags(directory)
    print("替换完成！")
