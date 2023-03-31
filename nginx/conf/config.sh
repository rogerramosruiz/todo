#!/bin/bash
envsubst '${AUTH_SERVER},${TASK_SERVER},${FRONTEND_SERVER}' < /home/conf/default.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'