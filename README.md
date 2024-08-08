# mddns
基于e-mail的伪ddns

需要有ipv6

需要安装的python库：
```
pip install zmail
```

使用方法：
```
1、使用update_mail.py将nas的ipv6地址发送到邮箱
2、其他windows设备使用mddns.py获取邮件，将“设备名.hosts”的ipv6地址写入hosts文件
```

然后就可以愉快地使用域名“设备名.hosts”访问你的nas了

在系统中写个定时任务，就可以假装实现了ddns，如果个人或者家庭使用的话，还是很方便的

linux或其他系统，需要修改下hosts文件的路径，操作应该是一致的

注意修改python文件中的设备名，如有公网ipv4的话，也可以把ipv6的正则替换为ipv4
