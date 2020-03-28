import paramiko
import sys

# 创建SSHClient实例对象
ssh = paramiko.SSHClient()
# 调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程机器  地址、端口、用户名和密码
ssh.connect('192.168.145.130', 22, 'huangjin', 'hj130826')


def remoteRun(cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode()
    errinfo = stderr.read().decode()
    print(output + errinfo)
    return output + errinfo


# 检查是否有之前版本运行
output = remoteRun('ps -ef|grep open_platform|grep -v grep')
# 如果存在 杀死进程
if 'python3 projec/cherrypy_startup.py open_platform' in output:
    print('服务运行中，停止服务')
    parts = output.split(' ')
    print(parts)
    pid = parts[5]
    remoteRun(f'kill -9 {pid}')
# 删除原来包
print('删除原来的包')
remoteRun('open_platform.zip')
# 上传安装包
print('上传安装包')
sftp = ssh.open_sftp()
sftp.put(r'd:\open_platform.zip', '/home/open_platform.zip')
sftp.close()
# 解压安装包
print('解压安装包')
remoteRun('unzip open_platform.zip')
print('ok')
# 运行
print('运行')
remoteRun('cd /home/open_platform; chmod +x run.sh; sh run.sh')
# 检查是否运行成功
print('是否运行成功')
output = remoteRun('ps -ef|grep open_platform|grep -v grep')
if 'python3 projec/cherrypy_startup.py open_platform' in output:
    print('服务运行成功')
else:
    print('服务没有运行')
    sys.exit(3)
ssh.close()






