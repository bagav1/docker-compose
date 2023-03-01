FROM mongo:5.0.10
ADD init-mongo.js /docker-entrypoint-initdb.d/
RUN chmod 0755 /docker-entrypoint-initdb.d/init-mongo.js
EXPOSE 27017