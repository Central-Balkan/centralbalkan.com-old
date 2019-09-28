ssh -t central_balkan@centralbalkan.com '\
    cd /home/central_balkan/code/centralbalkan/central_balkan && \
    source /home/central_balkan/virtual-environments/centralbalkan/bin/activate && \
    git pull origin master && \
    pip3 install -r requirements/base.txt && \
    python manage.py migrate && \
    service supervisor restart \
    '
