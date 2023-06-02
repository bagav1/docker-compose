FROM php:7.4.0-fpm

RUN apt-get update && apt-get install -y \
    git \
    vim \
    libzip-dev \
    zip \
    unzip \
    libpq-dev \
    firebird-dev \
    --yes --no-install-recommends \
    libssl-dev \
    zlib1g-dev \
    libmosquitto-dev \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev 
    
RUN docker-php-ext-install zip pdo_firebird pdo_pgsql pdo_mysql

RUN docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

RUN docker-php-ext-install calendar && docker-php-ext-configure calendar

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer
