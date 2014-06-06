from fabric.api import *
from jinja2 import Environment, FileSystemLoader

env.hosts = ['root@benchmarks-hkg']
#env.hosts = ['root@benchmarks-hkg', 'root@benchmarks-syd']
#env.hosts = ['root@benchmarks-dfw', 'root@benchmarks-ord', 'root@benchmarks-iad, 'root@benchmarks-lon', 'root@benchmarks-hkg', 'root@benchmarks-syd']

@parallel
def setup():
    jenv = Environment(loader=FileSystemLoader('csi-marconi'))
    region = env.host[-3:]
    tenant_id = "806067"
    run("apt-get update")
    run("apt-get upgrade -y")
    run("apt-get install -y git")
    run("git clone https://github.com/obulpathi/csi-marconi.git csi-marconi")
    run("REGION=%s TENANT_ID=%s bash /root/csi-marconi/setup.sh" % (region, tenant_id))

@parallel
def benchmark():
    region = env.host[-3:]
    tenant_id = "806067"
    auth_token = "edb708b0986d4000a86ff2b28908c728" 
    run("REGION=%s TENANT_ID=%s AUTH_TOKEN=%s bash /root/csi-marconi/benchmark.sh" % (region, tenant_id, auth_token))
    # copy the logs dir to local log server dir
    get("/root/.tsung/log/*", "/root/logs/")
