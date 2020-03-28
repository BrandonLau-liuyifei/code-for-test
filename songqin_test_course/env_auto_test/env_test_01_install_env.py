# linux服务器手动安装过程
"""1。登陆服务器SSH协议登陆
    操作：使用SSH账号密码登陆
   2。检查是否有以前版本的产品在运行
    操作：1。查询产品进程ps -ef|grep apiteach|grep -v grep
         2。存在进程启动，关闭进程 kill -9 apiteach
   3。删除掉原有的代码包
    操作：rm -rf apiteach.zip
   4。上传安装包文件（手工上传文件）
   5。备份原来的安装目录
      rm -rf restapi-teach.bak
      mv restapi-teach restapi-teach.bak
   6。解压安装包文件
      unzip restapi-teach.zip
   7。运行run.sh文件，启动服务
      yum -y install dos2unix
      ./run.sh
      ps -ef|grep apiteach|grep -v grep
   8。浏览器登陆页面验证服务是否启动"""

# 创建自动化安装测试环境 安装paramiko库
import paramiko
import sys
# 打开SSHClient
ssh = paramiko.SSHClient()
# 启动信任远程机器，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#根据账号链接远程机器，地址，端口，用户名，密码
ssh.connect(hostname="192.168.1.104",
            port=22,
            username="root",
            password="xxxxx")
# #创建单个py文件
# ssh.exec_command('echo "ip=192.168.1.105">cfg.py')
# # 创建多个py文件
# for x in range(20):
#     ssh.exec_command(f'echo "ip=192.168.1.{x+1}">cfg_{x+1}.py')

# stdin,stdout,stderr 输入、输出、异常结果
stdin,stdout,stderr = ssh.exec_command(
    "ps -ef|grep apiteach|grep -v grep")
#读取完整进程信息
output = stdout.read().decode("utf-8")
print(output) #返回list列表，完整的进程信息
if 'output中的进程的用于判定' in output:
    print("老版本中的程序运行中。。。kill掉")
    parts = output.split(" ")
    parts = [part for part in parts if part]
    pid = parts[1]
    ssh.exec_command(f'kill -9 {pid}')
# 删除掉旧安装包
ssh.exec_command('rm -f restapi-teach.zip')
# 上传新的安装包
print("上传新的安装包")
sftp=ssh.open_sftp()   #sftp是linux自带的
sftp.put(r'文件存放的位置','/home/目录/') #存放文件的地址 和 服务器上的目录
sftp.close()
#备份原来的安装目录
print("备份原来的安装目录")
ssh.exec_command('rm -rf restapi-teach.bak;mv restapi-teach restapi-teach.bak')
#解压安装包
print("解压安装包",end=" ")
ssh.exec_command('unzip restapi-teach.zip')
print("ok")
# 运行
print("运行")
ssh.exec_command('cd restapi-teach;chmod 700 run.sh;dos2unix run.sh;./run.sh;sleep 5')
print("检查是否运行成功")
output = ssh.exec_command('ps -ef|grep apiteach|grep -v grep')
if 'output中的进程的用于判定' in output:
    print("新版本运行成功")
else:
    print("新版本没有运行成功")
    sys.exit()
#防火墙打开8066端口
# remoteRun('iptables -I INPUT -p TCP --dport 8066 -j ACCEPT;/sbin/service iptables save')

#进行UI自动化执行登陆
# 关闭SSHClient
ssh.close()










