import zmail
import os
import ctypes, sys
import re

debug = 0

devices = ["um480","unraid"]

def is_admin():
    try:
        return debug or ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # 主程序写在这里
	server = zmail.server('xxxxx@qq.com', 'xxxxxxxxx')  #e-mail & password

	(message_count, mailbox_size)  = server.stat()
	print(f"邮件数量：{message_count}")
	print(f'占用空间：{mailbox_size/1000000:.2f}MB')
	
	step = 3
	
	def get_ipMail(device,message_count,cnt):
		st=message_count-(cnt+1)*step+1
		ed=message_count-cnt*step
		print('check:',st,'~',ed)
		if(st<1):
			print(f"No {device} mail")
			os._exit(0)
		mails = server.get_mails(subject=f'{device} IP地址',start_index=st,end_index=ed)
		return mails
	
	for device in devices:
		print(device)
		cnt = 0
		mails = get_ipMail(device,message_count,cnt)
		
		while(not mails):
			cnt+=1
			mails = get_ipMail(device,message_count,cnt)
		
		ipv6_str = mails[-1]['content_text'][0]
		result = re.findall(r"([a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})", ipv6_str, re.I)[0][0]
		ipv6_addr = f'{result} {device}.hosts'
		print("\n"+ipv6_addr+'\n')
		
		with open('C:/Windows/System32/drivers/etc/hosts','r',encoding='utf-8') as f:
			hosts = f.read()
		print(hosts)
		
		pattern = re.compile(rf"240.*? {device}\.hosts")
		
		um480_dns = re.findall(pattern,hosts)
		print(um480_dns)
		if(um480_dns):
			hosts = re.sub(pattern, ipv6_addr, hosts)
		else:
			hosts += "\n"+ipv6_addr
		print(hosts)
		
		with open('C:/Windows/System32/drivers/etc/hosts','w',encoding='utf-8') as f:
			f.write(hosts)
	
else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)


