#!/bin/bash

gunicorn blogcms.wsgi:application --bind 0.0.0.0:8000