"""
linux基本命令
1.文件操作
创建文件 touch xxx.txt
创建目录 mkdir ddd
删除文件 remove [-f] xxx.txt
删除目录 rm [-rf] ddd
删除空目录 rmdir ddd
改文件名 mv xxx.txt yyy.txt
添加文件内容 echo "hello" >> 文件.txt
覆盖文件内容 echo "fugai" > 文件.txt
查看文件内容 tail 文件.txt
查看文件 ll 目录

2。监控系统
监控cpu top
监控内存 free -h
监控硬盘 df -h
"""
import paramiko
import time
#创建sshclient对象
ssh = paramiko.SSHClient()
#默认接受公钥
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接远程服务器
ssh.connect("ip",22,"username","password")

# 每次执行一次exec_command,相当于重新打开一个命令进入username家目录

#执行linux命令
cmd1 = "touch haha.txt"
ssh.exec_command(cmd1)
cmd2 = "echo 'hello world' >> haha.txt"
ssh.exec_command(cmd2)


#监控linux系统
cdm1 = "mkdir test"
cmd2 = "cd testdir"
cmd3 = "touch mem.txt"
cmd4 = "free -m >> mem.txt"
cmds = [cmd1,cmd2,cmd3,cmd4]
cmds = ";".join(cmds)
ssh.exec_command(cmds)

#周期监控
for i in range(10):
    cmd4 = "free -m >> mem.txt"
    time.sleep(60)


