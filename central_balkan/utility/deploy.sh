#!/bin/bash

scp -r ./ centralbalkan:~/code/centralbalkan/central_balkan/ &&
ssh -t centralbalkan 'sudo service nginx restart && sudo service supervisor restart'
