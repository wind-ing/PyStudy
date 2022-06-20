"""
程序描述：
将目录“Gif拆分文件夹”下面的gif拆分成帧，并在当前目录下以同名文件夹放置
"""
import os
from PIL import Image


def mkdir(imname):
    """
    获取Gif的名字，根据它的名字创建文件夹保存拆分的帧

    :param imname: 需要拆分的Gif的名字
    :return:
    """
    file_name = imname[0:-4]
    os.makedirs(file_name)
    im = Image.open('Gif拆分文件夹\\{0}'.format(imname))
    try:
        im.save('{0}\\picframe{1:02d}.png'.format(file_name, im.tell()))
        while True:
            im.seek(im.tell() + 1)
            im.save('{0}\\picframe{1:02d}.png'.format(file_name, im.tell()))
    except:
        print("处理结束")


def file_name_global(file_dir):
    """
    获取一个目录名，得到文件

    :param file_dir: 需要拆分的Gif所在的目录
    :return:
    """
    for files in os.listdir(file_dir):
        if not os.path.exists(files[0:-4]):
            mkdir(files)


file_name_global("Gif拆分文件夹")
