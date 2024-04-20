# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image, ImageSequence

from PIL import Image, ImageSequence


def insert_and_blink_image_in_gif(gif_path, img_path, output_path, start_frame, blink_rate):
    # 打开原始GIF
    gif = Image.open(gif_path)

    # 打开要插入的图片，并调整其大小以匹配GIF的尺寸
    img_to_insert = Image.open(img_path).resize(gif.size)

    frames = []  # 用来存储处理后的帧的列表
    i = 0  # 帧索引计数器
    blink_on = False  # 控制闪烁状态

    # 遍历原始GIF的每一帧
    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")  # 确保帧为RGBA模式以便混合

        if i >= start_frame:
            if i % blink_rate == 0:
                blink_on = not blink_on  # 每隔'blink_rate'帧切换闪烁状态

            if blink_on:
                # 如果闪烁开启，则将当前帧与要插入的图片混合
                frame = Image.blend(frame, img_to_insert.convert("RGBA"), alpha=0.5)

        frames.append(frame)  # 添加处理过或原始的帧
        i += 1  # 帧索引递增

    # 保存含有插入闪烁图片的新GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0,
                   duration=gif.info['duration'], optimize=False)



def replace_frame_in_gif(gif_path, img_path, output_path, start_frame, blink_rate):
    # 打开原始GIF
    gif = Image.open(gif_path)

    # 打开要插入的图片，并调整其大小以匹配GIF的尺寸
    img_to_insert = Image.open(img_path).resize(gif.size)

    frames = []  # 用来存储处理后的帧的列表
    i = 0  # 帧索引计数器
    blink_on = False  # 控制闪烁状态

    # 遍历原始GIF的每一帧
    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")  # 确保帧为RGBA模式以便混合

        if i >= start_frame:
            if i % blink_rate == 0:
                blink_on = not blink_on  # 每隔'blink_rate'帧切换闪烁状态

            if blink_on:
                # 如果闪烁开启，则直接使用插入的图片替换当前帧
                frame = img_to_insert.convert("RGBA")
        # else:
        #     # 确保非替换帧也是RGBA模式，以保持一致性
        #     frame = frame.convert("RGBA")

        frames.append(frame)  # 添加处理过或原始的帧
        i += 1  # 帧索引递增

    # 保存含有替换帧的新GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0,
                   duration=gif.info['duration'], optimize=False)



def count_gif_frames(file_path):
    with Image.open(file_path) as img:
        frame_count = 0
        while True:
            try:
                img.seek(frame_count)  # 移动到下一帧
                frame_count += 1
            except EOFError:
                break  # 当没有更多帧时，会抛出EOFError
        return frame_count

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}, love')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('Soyosan')
    frame_count = count_gif_frames('soyo_cry.gif')
    print(f"The GIF has {frame_count} frames.")
    frame_count = count_gif_frames('soyosan_love.gif')
    print(f"The GIF has {frame_count} frames.")
    # insert_and_blink_image_in_gif("soyo_cry.gif", "soyo_tough.png", "soyosan_love.gif", start_frame=5, blink_rate=2)
    replace_frame_in_gif("soyo_cry.gif", "soyo_tough.png", "soyosan_love.gif", start_frame=5, blink_rate=2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
