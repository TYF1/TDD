
from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "git@github.com:TYF1/TDD.git" 

env.user = 'root' 
env.password = '751603luerTYF'

# 填写你自己的主机对应的域名
env.hosts = ['175.27.191.12']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/opt/TDD/TDD' 

    run('cd %s && git pull origin master' % source_folder) 
    run("""
        cd {} &&
        pip3 install -r requirements.txt 
        """.format(source_folder)) 
    run("""
        cd {} &&
        python3 manage.py collectstatic --noinput
        """.format(source_folder)) 
    run("""
        cd {} &&
        python3 manage.py migrate
        """.format(source_folder)) 
    run("pkill -f uwsgi -9") 
    sudo('service nginx reload')