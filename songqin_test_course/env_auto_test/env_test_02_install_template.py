import paramiko

#SSHClient

# 实例化SSHClient
client = paramiko.SSHClient()

# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接SSH服务端，以用户名和密码进行认证
client.connect(hostname='192.168.1.105', port=22, username='root', password='123456')

# 打开一个Channel并执行命令
stdin, stdout, stderr = client.exec_command('df -h ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

# 打印执行结果
print(stdout.read().decode('utf-8'))

# 关闭SSHClient
client.close()

# -------------密钥链接方式--------------

# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/ch/.ssh/id_rsa')

# 实例化SSHClient
client = paramiko.SSHClient()

# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接SSH服务端，以用户名和密码进行认证
client.connect(hostname='10.0.0.1', port=22, username='root', pkey=private)

# -------------SSHClient封装transport--------------
import paramiko

# 创建一个通道
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='root', password='123')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df -h')
print(stdout.read().decode('utf-8'))

transport.close()

import paramiko

# 获取Transport实例
tran = paramiko.Transport(('10.0.0.3', 22))

# 连接SSH服务端，使用password
tran.connect(username="root", password='123456')
# 或使用
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/root/.ssh/id_rsa')
# 连接SSH服务端，使用pkey指定私钥
tran.connect(username="root", pkey=private)

# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

# 设置上传的本地/远程文件路径
localpath = "/Users/root/Downloads/1.txt"
remotepath = "/tmp/1.txt"

# 执行上传动作
sftp.put(localpath, remotepath)
# 执行下载动作
sftp.get(remotepath, localpath)

tran.close()

#SFTPlient

import paramiko

# 获取Transport实例
tran = paramiko.Transport(('10.0.0.3', 22))

# 连接SSH服务端，使用password
tran.connect(username="root", password='123456')
# 或使用
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/root/.ssh/id_rsa')
# 连接SSH服务端，使用pkey指定私钥
tran.connect(username="root", pkey=private)

# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

# 设置上传的本地/远程文件路径
localpath = "/Users/root/Downloads/1.txt"
remotepath = "/tmp/1.txt"

# 执行上传动作
sftp.put(localpath, remotepath)
# 执行下载动作
sftp.get(remotepath, localpath)

tran.close()

# 综合实例
class SSHConnection(object):

    def __init__(self, host_dict):
        self.host = host_dict['host']
        self.port = host_dict['port']
        self.username = host_dict['username']
        self.pwd = host_dict['pwd']
        self.__k = None

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def run_cmd(self, command):
        """
         执行shell命令,返回字典
         return {'color': 'red','res':error}或
         return {'color': 'green', 'res':res}
        :param command:
        :return:
        """
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        res = unicode_utils.to_str(stdout.read())
        # 获取错误信息
        error = unicode_utils.to_str(stderr.read())
        # 如果有错误信息，返回error
        # 否则返回res
        if error.strip():
            return {'color': 'red', 'res': error}
        else:
            return {'color': 'green', 'res': res}

    def upload(self, local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path, confirm=True)
        # print(os.stat(local_path).st_mode)
        # 增加权限
        # sftp.chmod(target_path, os.stat(local_path).st_mode)
        sftp.chmod(target_path, 0o755)  # 注意这里的权限是八进制的，八进制需要使用0o作为前缀

    def download(self, target_path, local_path):
        # 连接，下载
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 下载至服务器 /tmp/test.py
        sftp.get(target_path, local_path)

    # 销毁
    def __del__(self):
        self.close()
# unicode_utils.py
def to_str(bytes_or_str):
    """
    把byte类型转换为str
    :param bytes_or_str:
    :return:
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value



