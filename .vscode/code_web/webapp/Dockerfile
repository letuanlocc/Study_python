# Dùng image Python chính thức
FROM python:3.11

# Cập nhật apt và cài thư viện hệ thống cho ODBC và SQL Server
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    freetds-dev \
    tdsodbc \
    && rm -rf /var/lib/apt/lists/*

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy toàn bộ project vào container
COPY . .

# Nâng cấp pip và cài thư viện Python
RUN pip install --upgrade pip
RUN pip install -r global_requirements.txt

# Mở port cho Django (mặc định là 8000)
EXPOSE 8000

# Lệnh chạy Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
