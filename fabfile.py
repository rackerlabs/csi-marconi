import getpass

from fabric.api import env, run, parallel


hosts = ['root@benchmarks-dfw', 'root@benchmarks-ord', 'root@benchmarks-iad',
         'root@benchmarks-lon', 'root@benchmarks-hkg', 'root@benchmarks-syd']


@parallel
def _setup(tenant_id):
    region = env.host[-3:]
    run("apt-get update")
    run("apt-get upgrade -y")
    run("apt-get install -y git")
    run("git clone https://github.com/rackerlabs/csi-marconi.git csi-marconi")
    run("REGION=%s TENANT_ID=%s bash /root/csi-marconi/setup.sh" %
        (region, tenant_id))


def setup():
    tenant_id = raw_input('Enter tenant_id: ')
    env.host = hosts
    _setup(tenant_id)


@parallel
def _benchmark(tenant_id, auth_token):
    region = env.host[-3:]
    run("REGION=%s TENANT_ID=%s AUTH_TOKEN=%s bash /root/csi-marconi/benchmark.sh" %
        (region, tenant_id, auth_token))
    # copy the logs dir to local log server dir
    get("/root/.tsung/log/*", "/root/logs/")


def benchmark():
    tenant_id = raw_input('Enter tenant_id: ')
    auth_token = getpass.getpass('Enter auth_token: ')
    env.host = hosts
    _benchmark(tenant_id, auth_token)
