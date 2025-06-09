FROM nikolaik/python-nodejs:python3.13-nodejs24
LABEL authors="bastianlobe"

# Install Nginx web server
RUN apt-get update && \
    apt-get install -y nginx gettext && \
    rm -rf /var/lib/apt/lists/*

# Create a directory for the Django project
RUN mkdir App
COPY requirements.txt /App/

WORKDIR /App

### Install dependencies ###
# Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# npm
COPY frontend/package.json /App/frontend/
COPY frontend/package-lock.json /App/frontend/
RUN npm --prefix /App/frontend install

### Copy project files ###
COPY nginx.conf /etc/nginx/sites-available/default
COPY scripts /scripts
COPY backend backend
COPY frontend frontend

# Create a directory for static files
RUN mkdir /static

RUN npm --prefix /App/frontend run build
#Move files to nginx directory, so nginx can access them
RUN mv /App/frontend/dist/* /usr/share/nginx/html/

# Expose port 6753 for the container
EXPOSE 6753

# Run the boot.sh script when the container starts
ENTRYPOINT ["/scripts/entrypoint.sh"]