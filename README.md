# Fast Ftp Server

该项目用来在内网渗透中快速部署一个ftp服务，方便进行文件传输。(虽然在渗透过程中可能很少会用到，有简单的http服务可以代替)

## Usage

该ftp服务默认使用匿名账户登录。

### Linux & macOS

1. 安装依赖库

    - `python3 -m pip install pyftpdlib`

2. 运行python脚本

    - `python3 ftpserver.py [path]`
    > **path** - 指定ftp文件共享目录

### Windows

windows版使用pyinstaller打包。

1. 运行ftpserver.exe程序

    - `.\ftpserver.exe [path]`
