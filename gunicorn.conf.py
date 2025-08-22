import multiprocessing

# 绑定地址和端口
bind = "0:39998"

# 工作进程数
workers = multiprocessing.cpu_count() * 2 + 1

# worker类（对于I/O密集型应用，可以使用gevent）
worker_class = "sync"

# 最大同时连接数
worker_connections = 1000

# 超时时间
timeout = 30

# 守护进程模式（后台运行）
daemon = False

# 访问日志和错误日志
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"

# 日志级别
loglevel = "info"

# 进程名
proc_name = "myproject_gunicorn"

# 最大请求数（防止内存泄漏）
max_requests = 1000
max_requests_jitter = 50
