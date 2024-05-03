from PIL import Image
import os

def convert_images_in_folder(input_folder, output_folder, input_format, output_format):
    for filename in os.listdir(input_folder):      
        if filename.endswith(input_format):
            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)
            img = img.convert("RGB")  # 将图像转换为不带Alpha通道的RGB模式
            output_filename = os.path.splitext(filename)[0] + '.' + output_format
            output_path = os.path.join(output_folder, output_filename)
            img.save(output_path, format=output_format.lower(), quality=100, subsampling=0)
            print(f"成功转换 {filename} 的格式为 {output_format}")
    print("转换完成!")  # 循环结束后打印转换完成提示

# 提示用户输入所需的参数
input_folder = input("请输入输入文件夹路径(例如:C:\\Users\\example\\Desktop\\dds):")
output_folder = input("请输入输出文件夹路径(例如:C:\\Users\\example\\Desktop\\png):")

# 如果指定的输出文件夹不存在，则创建该文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"文件夹 {output_folder} 不存在，已创建文件夹")
else:
    print(f"文件夹 {output_folder} 已存在")

input_format = input("请输入输入图像格式(例如:dds):")
output_format = input("请输入输出图像格式(例如:jpeg):")

# 执行转换
print('开始转换...')
convert_images_in_folder(input_folder, output_folder, input_format, output_format)

input("程序执行完毕，按任意键退出...")
exit()