#!/bin/sh
gunicorn -w ${APP_THREADS} -b 0.0.0.0:${APP_PORT} ${APP_MODULE}:app