SISS Web Service
===================
.. image:: https://travis-ci.com/TrentaIcedCoffee/SISS.svg?branch=build
    :target: https://travis-ci.com/TrentaIcedCoffee/SISS/  

SISS web services including transaction matching, ...

Env
------------
.. code-block:: bash

    Ubuntu Server 16.04 LTS
    AWS codepipeline

Deploy
------------
Install Python 3.6 (from ppa, works WITH python3.5); AWS codedeploy-agent

.. code-block:: bash

    ./scripts/init_env

Set environment variables (``/home/ubuntu/.env`` is loaded)

AWS codepipeline release

Create superusers