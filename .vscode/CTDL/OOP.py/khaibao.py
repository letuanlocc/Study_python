class Vehicle:
    wheels_count = 0  # Thuộc tính lớp

    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels
        Vehicle.wheels_count += wheels

    @staticmethod
    def is_motorized(vehicle_type):
        return vehicle_type in ['Car', 'Bike', 'Truck']  # Một phương thức kiểm tra loại phương tiện

    @classmethod
    def get_total_wheels(cls):
        return cls.wheels_count  # Trả về tổng số bánh của tất cả phương tiện đã tạo

# Tạo các đối tượng
car = Vehicle("Car", 4)
bike = Vehicle("Bike", 2)

# Gọi phương thức tĩnh
print(Vehicle.is_motorized("Car"))  # Output: True

# Gọi phương thức lớp
print(Vehicle.get_total_wheels())  # Output: 6
