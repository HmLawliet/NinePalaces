from PIL import Image
import paddlehub as hub

def nine_gongge(path,name):
    # 读取文件
    im = Image.open(path)
    # 宽高各除 3，获取裁剪后的单张图片大小
    width = im.size[0]//3
    height = im.size[1]//3
    # 裁剪图片的左上角坐标
    start_x = 0
    start_y = 0
    # 用于给图片命名
    im_index = 1
    # 循环裁剪图片
    for _ in range(3):
        for _ in range(3):
            # 裁剪图片并保存
            crop = im.crop((start_x, start_y, start_x+width, start_y+height))
            crop.save(f'{name}_{im_index}.jpg')
            # 将左上角坐标的 x 轴向右移动
            start_x += width
            im_index += 1
        # 当第一行裁剪完后 x 继续从 0 开始裁剪
        start_x = 0
        # 裁剪第二行
        start_y += height


def toggle_background(org_paht, bg_path, ):
    # 加载模型
    humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
    # 抠图
    results = humanseg.segmentation(data={'image':['xscn.jpeg']})
    # 读取背景图片
    bg = Image.open('bg.jpg')
    # 读取原图
    im = Image.open('humanseg_output/xscn.png').convert('RGBA')
    im.thumbnail((bg.size[1], bg.size[1]))
    # 分离通道
    r, g, b, a = im.split()
    # 将抠好的图片粘贴到背景上
    bg.paste(im, (bg.size[0]-bg.size[1], 0), mask=a)
    bg.save('xscn.jpg')

if __name__ == "__main__":
    nine_gongge(r'D:\Projects\funnyImage\static\OIP.jpg','yaoming') 