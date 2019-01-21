# verify_code_docker
用于搭建识别银河验证码的http服务，基于 flask 和 tesseract

来自地址：`https://github.com/shidenggui/yh_verify_code_docker`

尝试识别佣金宝的验证码，已成功

#安装步骤：
**1.**
（win10）需要安装tesseract，目前最新版本是4.0，win的下载地址是：`https://github.com/UB-Mannheim/tesseract/wiki`，我安装的 tesseract-ocr-w64-setup-v4.0.0.20181030.exe
安装上以后需要设置一下path环境，测试下安装是否正常
 （ubuntu16.0.4) 执行`sudo apt install tesseract-ocr` ,详见：`https://github.com/tesseract-ocr/tesseract/wiki`
 
 **检查是否安装成功：**
 
打开命令行，执行`tesseract myscan.png out` 会生成out.txt文件，如果里面内容和验证码图片内容一致即可

**2.**
修改几个参数：

1）pytesseract.py文件的tesseract_cmd参数要修改成安装目录或官方默认的地址也可以用tesseract
2）启动执行app.py
3）test.py是测试例子,执行检查输出文件



