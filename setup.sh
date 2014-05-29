#!/usr/bin/env bash

# Create ubuntu 14.04 server
# apt-get update
# apt-get -y upgrade
apt-get install -y gnuplot-nox libtemplate-perl libhtml-template-perl libhtml-template-expr-perl
apt-get install -y gnuplot  make git autoconf python-pip
pip install pyrax

# install tsung
cd ~
wget http://tsung.erlang-projects.org/dist/tsung-1.5.0.tar.gz
tar xvf tsung-1.5.0.tar.gz
cd tsung-1.5.1
chmod 755 configure
./configure
make
make install

# get tsung becnhmarking directory
cd ~
git clone https://github.com/obulpathi/csi-marconi.git
cp -r csi-marconi/load ~/.tsung
cp csi-marconi/pyrax.cfg ~/.pyrax.cfg
cp csi-marconi/credentials.conf ~/.credentials.conf

# update pyrax.cfg and credentials.conf
sed -i "s/REGION/${REGION}/g" ~/.pyrax.cfg
sed -i "s/USERNAME/${MARCONI_USERNAME}/g" ~/.credentials.conf
sed -i "s/PASSWORD/${PASSWORD}/g" ~/.credentials.conf
sed -i "s/TENANT_ID/${TENANT_ID}/g" ~/.credentials.conf

cd ~/.tsung/
# Update the tsung.xml
# for a single node setup, skip the next step
# Update the <clients> section of ~/.tsung/tsung.xml, to point to your tsung machines. (Do not use IP addresses here.)
# Update the <servers> section, to point to your marconi server.
sed -i "s/DATACENTER/${DATACENTER}/g" tsung.xml
# Replace all auth tokens, with a valid auth token. (This is intentionally manual, to avoid accidentally stressing the production auth.)
sed -i "s/AUTH_TOKEN/${AUTH_TOKEN}/g" auth.csv
sed -i "s/TENANT_ID/${TENANT_ID}/" auth.csv
# Update ~/.tsung/projectid.csv, to include the tenant ID of your account.
sed -i "s/PROJECT_ID/${PROJECT_ID}/g" projectid.csv

# Increase file descriptors available.
echo root soft  nofile 9000  >> /etc/security/limits.conf
echo root hard  nofile 65000 >> /etc/security/limits.conf
