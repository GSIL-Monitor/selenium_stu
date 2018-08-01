# from selenium import webdriver
# from PIL import Image
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# #定位百度搜索按钮
# element = driver.find_element_by_id("su")
# #获取元素坐标:{'x': 728, 'y': 192} 显示器不一样结果不一样
# print(element.location)
# #获取元素大小：{'height': 36, 'width': 100}
# print(element.size)
#
# #根据x、y坐标、高度、宽度形成元素的矩形
# left = element.location['x']
# top = element.location['y']
# right = element.location['x'] + element.size['width']
# bottom = element.location['y'] + element.size['height']
#
# #保存屏幕截图
# img_path = 'baidu_buttom.png'
# driver.save_screenshot(img_path)
#
# #根据数据，生成图片
# im = Image.open(img_path)
# im = im.crop((left, top, right, bottom))
# im.save(img_path)
