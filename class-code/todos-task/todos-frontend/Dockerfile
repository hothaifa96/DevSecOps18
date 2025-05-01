FROM nginx:alpine

WORKDIR /usr/share/nginx/html

# Copy static files
COPY index.html styles.css app.js ./

# Create environment configuration script

# Update index.html to load env-config.js
RUN sed -i '/<\/head>/i <script src="env-config.js"></script>' /usr/share/nginx/html/index.html

# Configure nginx for CORS
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# Use the entrypoint script to inject environment variables at runtime

CMD ["nginx", "-g", "daemon off;"]