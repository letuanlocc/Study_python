FROM python:3.11

RUN apt-get update && apt-get install -y curl apt-transport-https gnupg unixodbc-dev

# Import Microsoft GPG key explicitly
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
    && install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ \
    && rm microsoft.gpg

# Thêm repo của Microsoft cho Debian 12 Bookworm
RUN curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r global_requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
