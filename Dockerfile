FROM django:1.10-python3

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -e .
ENV DJANGO_SETTINGS_MODULE=pdp7_pt.settings_production
