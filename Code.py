import qrcode
import os
import time
log = []
t = time.strftime('%Y-%m-%d-%B-%A %H:%M:%S', time.localtime())
log.append("时间:" + t)
qr = qrcode.QRCode(
	version=10,
	error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=7,
	border=1
)
def create_log_file(log):
    if os.path.exists("log.txt") == False:
        file = open("log.txt", "w")
        file.write(log)
        file.close
    else:
        file = open("log.txt", "a")
        file.write("\n" + log)
        file.close
url = input("请输入链接或文字:")
log.append("链接:" + url)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
name = input("请输入文件名:")
filename = name + ".png"
log.append("文件名:" + filename)
img.save(filename)
create_log_file(str(log))
