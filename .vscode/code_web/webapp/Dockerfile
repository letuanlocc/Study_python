# Dùng image Python chính thức
FROM python:3.11

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy toàn bộ project vào container
COPY . .

# Cài thư viện từ requirements
RUN pip install --upgrade pip
RUN pip install -r global_requirements.txt

# Mở port cho Django (mặc định là 8000)
EXPOSE 8000
#http://127.0.0.1:8000/
# Lệnh chạy Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]