# Build stage for frontend
FROM node:24-alpine as frontend-builder
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend .
RUN npm run build

# Build stage for backend
FROM python:3.13-alpine as backend-builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend .
RUN python manage.py collectstatic --noinput


# Final stage
FROM python:3.13-alpine
LABEL authors="bastianlobe"

# Install runtime dependencies
RUN apk add --no-cache nginx gettext py3-gunicorn && \
    mkdir -p /app  /usr/share/nginx/html /app/data

# Copy built artifacts and Python dependencies
COPY --from=frontend-builder /app/dist /usr/share/nginx/html
COPY --from=backend-builder /app /app
COPY --from=backend-builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=backend-builder /usr/local/bin /usr/local/bin

# Configure nginx
COPY nginx.conf /etc/nginx/http.d/default.conf
COPY scripts /scripts

# Create necessary directories
RUN mkdir -p /app/data/media

WORKDIR /app

EXPOSE 6753
ENTRYPOINT ["/scripts/entrypoint.sh"]