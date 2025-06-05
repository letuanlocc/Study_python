FROM python:3.11

# Cài các thư viện hệ thống cần thiết cho ODBC và SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg \
    unixodbc-dev

# Thêm Microsoft package key và repo
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Đặt thư mục làm việc
WORKDIR /app

# Copy project vào
COPY . .

# Cài pip và các thư viện Python
RUN pip install --upgrade pip
RUN pip install -r global_requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
