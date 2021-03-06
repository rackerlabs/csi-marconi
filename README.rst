==========
Load Tests
==========

Marconi uses `Tsung`_ (Tsung 1.5 or higher) to run load tests.

**Table of Contents**

.. contents::
    :local:
    :depth: 2
    :backlinks: none


.. _setting_up_load_generators:
------------------------------
Setting up the Load Generators
------------------------------

#. Create ubuntu 13.10 server
#. Install tsung in all the machines. (See Section: Installing Tsung from Source).
   One of the machines will be the controller, & the rest will be clients.
#. Enable ssh connection with no passphrase, between the tsung controller and each of the clients.
#. Update the /etc/hosts in all the machines. The controller:/etc/hosts should have entries pointing to all the clients, as well as itself.
   All the clients, should have an entry for the controller in /etc/hosts. 
   (We want to avoid the overhead of a dns lookup.)

---------------------------------------
Installing Erlang and Tsung from source
---------------------------------------

#. apt-get update
#. apt-get install -y git vim
#. git clone https://github.com/rackerlabs/csi-marconi.git 
#. Update ~/csi-marconi/tsungrc with valid REGION and TENANT_ID 
#. source tsungrc
#. bash ~/csi-marconi/setup.sh
#. reboot

---------------------------
Steps to run the load tests
---------------------------

#. Update ~/csi-marconi/tsungrc with valid AUTHENTICATION TOKEN
#. source tsungrc
#. If you are using tsung clients:
    * Update the <clients> section of ~/.tsung/tsung.xml, to point to your tsung machines. Do not use IP addresses here.
#. bash ~/csi-marconi/benchmark.sh

-----------------------
Generating Test Reports
-----------------------

#. After the test is complete, cd to the log directory generated by the tests in the controller machine.
   (eg. cd ~/.tsung/log/20130701-1635)
#. Generate html reports with '/usr/local/lib/tsung/bin/tsung_stats.pl'
#. You can run a simple web server to view reports, with 'python -m SimpleHTTPServer'
#. Enjoy your performance reports!!

---------------------------------------
Benchmarking multiple marconi endpoints
---------------------------------------

#. Create a benchmarks hosting server used for setting up the tsung controllers, running periodic benchmarks and storing benchmark logs (for Cloud Queues, this is benchmarks.cloudqueues.com server).
#. Clone https://github.com/rackerlabs/csi-marconi to benchmarks hosting server.
#. Create the required tsung controllers and clients, by following the instructions in :ref:`setting_up_load_generators`.
#. Add the tsung controller hostnames to /etc/hosts in the benchmarks hosting server.
#. Configure for passwordless SSH from benchmarks hosting server to tsung controllers.
#. cd csi-marconi
#. Add the tsung controller hostnames to fabfile.py
#. To setup the tsung controllers: fab setup
#. To benchmark the marconi endpoints using the tsung controllers: fab benchmark

==============
Security Tests
==============

To Be Updated

.. _`Tsung` : http://tsung.erlang-projects.org/
