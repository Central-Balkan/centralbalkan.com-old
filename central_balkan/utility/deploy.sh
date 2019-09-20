CHANGE_DIR='cd /home/central_balkan/code/centralbalkan/central_balkan'
ACTIVATE_VENV='source /home/central_balkan/virtual-environments/centralbalkan/bin/activate'
PULL_MASTER='git pull origin master'
RUN_MIGRATIONS='python manage.py migrate'
RESTART_PROCESS='service supervisor restart'

ssh -t central_balkan@centralbalkan.com '\
    cd /home/central_balkan/code/centralbalkan/central_balkan && \
    source /home/central_balkan/virtual-environments/centralbalkan/bin/activate && \
    git pull origin master && \
    python manage.py migrate && \
    service supervisor restart \
    '
