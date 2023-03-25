 #!/bin/bash

envsubst '${AUTH_SERVER},${TASK_SERVER}' < /home/conf/default.conf.template > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'