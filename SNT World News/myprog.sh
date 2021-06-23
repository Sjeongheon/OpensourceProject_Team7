#!/bin/bash

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.2-linux-x86_64.tar.gz
tar xvzf elasticsearch-7.6.2-linux-x86_64.tar.gz
cd elasticsearch-7.6.2/
./bin/elasticsearch -d
cd ..
pip3 install networkx
chmod 755 app.py
./app.py

