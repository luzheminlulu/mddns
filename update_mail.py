import os
import re
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr

def getIPv6Address():
	for i in range(30):
		try:
			cmd_output = os.popen("ipconfig /all").read()
			print(cmd_output)
			result = re.findall(r"(240[a-f0-9](:[a-f0-9]{1,4}){7})", cmd_output, re.I)
			print(result)
			ipv6 = "%s"%result[0][0]
			print("获取ipv6地址成功：%s"%ipv6)
			return ipv6
		except:
			print('ipv6获取失败,重试次数：%d次'%i)
			time.sleep(10)
	return "[NULL]"

if __name__ == "__main__":
	ipv6 = getIPv6Address()
	file_dir  =  os.path.dirname(os.path.abspath(__file__))+"/ipv6_lppz.txt"
	
	f=open(file_dir,"r")
	last_ipvaddr_6 = f.read()
	f.close()
	
	if(ipv6 != last_ipvaddr_6):
		print('地址发生变化！')

		for i in range(5):
			try:
				msg=MIMEText("um480 IP地址:<br>%s"%ipv6,'plain','utf-8')
				msg['From']=formataddr(["lulu",'xxxxx@qq.com'])
				msg['To']=formataddr(["lulu",'xxxxx@qq.com'])
				msg['Subject']="um480 IP地址"
				server=smtplib.SMTP_SSL("smtp.qq.com",465)
				server.login("xxxxx@qq.com","xxxxxxxxx")
				server.sendmail('xxxxx@qq.com',['xxxxxx@qq.com',],msg.as_string())
				server.quit()
				print('邮件发送成功！')
				f=open(file_dir,"w")
				f.write(ipv6)
				f.close()
				print('更新文件成功！')
				break
			except:
				print('发生错误,重试次数：%d次！'%i)
				time.sleep(20)
				
	else:
		print('地址未发生变化！')
		pass


