from abc import ABC, abstractmethod
from collections import defaultdict

# ---------------- Payment Classes ----------------
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"{amount} paid via cash")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"{amount} paid via credit/debit card")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"{amount} paid via UPI")

# ---------------- Vehicle Classes ----------------
class Vehicle(ABC):
    def __init__(self, license_plate, owner_name):
        self.set_license(license_plate)
        self.set_owner_name(owner_name)
        self.vechile_number = license_plate  # making it available everywhere

    @abstractmethod
    def calculate_parking_fee(self):
        pass

    def set_license(self, number):
        if number[0] not in ['B', 'C', 'T', 'S']:
            print("Invalid license number")
            return
        self.__license_plate = number

    def set_owner_name(self, name):
        self.__owner_name = name

    def get_license(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def display(self):
        print(f"Vehicle details:\t License Plate: {self.__license_plate}, "
              f"Owner: {self.__owner_name}")

class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required
        self.vechile_type = 'Bike'

    def calculate_parking_fee(self):
        return 30

    def display(self):
        print(f"Vehicle details:\t Type: {self.vechile_type}, "
              f"License: {self.get_license()}, "
              f"Owner: {self.get_owner_name()}, "
              f"Helmet Required: {self.helmet_required}")

class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats):
        super().__init__(license_plate, owner_name)
        self.seats = seats
        self.vechile_type = 'Car'

    def calculate_parking_fee(self):
        return 50

    def display(self):
        print(f"Vehicle details:\t Type: {self.vechile_type}, "
              f"License: {self.get_license()}, "
              f"Owner: {self.get_owner_name()}, "
              f"Seats: {self.seats}")

class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive
        self.vechile_type = 'SUV'

    def calculate_parking_fee(self):
        return 70

    def display(self):
        print(f"Vehicle details:\t Type: {self.vechile_type}, "
              f"License: {self.get_license()}, "
              f"Owner: {self.get_owner_name()}, "
              f"4WD: {self.four_wheel_drive}")

class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity
        self.vechile_type = 'Truck'

    def calculate_parking_fee(self):
        return 100

    def display(self):
        print(f"Vehicle details:\t Type: {self.vechile_type}, "
              f"License: {self.get_license()}, "
              f"Owner: {self.get_owner_name()}, "
              f"Max Load: {self.max_load_capacity}")

# ---------------- Parking Spot ----------------
class Parkingspot:
    def __init__(self, spot, size):
        self.spot = spot
        self.size = size
        self.occupied = False
        self.vechile = None

    def __hash__(self):
        return hash((self.spot, self.size))

    def __lt__(self, other):  # so that sorting works
        return self.spot < other.spot

    def assign_vechile(self, vechile):
        if not self.occupied:
            print('Successfully assigned')
            self.vechile = vechile
            self.occupied = True
        else:
            print('Cannot assign vehicle, already occupied')

    def remove_vechile(self):
        self.occupied = False
        self.vechile = None

# ---------------- Parking Lot ----------------
class Parkinglot:
    dic = {
        'Bike': ['S', 'M', 'L', 'XL'],
        'Car': ['M', 'L', 'XL'],
        'SUV': ['L', 'XL'],
        'Truck': ['XL']
    }

    def __init__(self, lot_name):
        self.lot_name = lot_name
        self.list_parkingspots = set()
        self.dic1 = defaultdict(int)
        print(f"{lot_name} parking lot created")

    def add_spot(self, parkingspot):
        if parkingspot in self.list_parkingspots:
            print("Spot is already present")
        else:
            self.list_parkingspots.add(parkingspot)
            self.dic1[parkingspot.size] += 1

    def show_spot(self):
        arr1 = sorted(self.list_parkingspots)
        print("Parking Status:")
        for i in arr1:
            print(f"Spot {i.spot} ({i.size})->", end=" ")
            if not i.occupied:
                print("❌")
            else:
                print(f"✅ {i.vechile.vechile_type} ({i.vechile.vechile_number})")

    def park_vechile(self, vechile):
        arr1 = sorted(self.list_parkingspots)
        for size in Parkinglot.dic[vechile.vechile_type]:
            if self.dic1[size] > 0:
                for i in arr1:
                    if not i.occupied and i.size == size:
                        print("Parked successfully")
                        self.dic1[size] -= 1
                        i.assign_vechile(vechile)
                        return
        print("Parking place is not available")

    def unpark_vechile(self, vechile, time):
        arr1 = list(self.list_parkingspots)
        for i in arr1:
            if i.vechile == vechile:
                fee = vechile.calculate_parking_fee() * time
                print(f"{vechile.vechile_type} ({vechile.vechile_number}) removed from {i.spot} "
                      f"Parking Fee = ₹{fee}")

                # Ask payment method
                print("Select Payment Method: 1. Cash 2. Card 3. UPI")
                choice = input("Enter choice: ")

                if choice == "1":
                    payment = CashPayment()
                elif choice == "2":
                    payment = CardPayment()
                elif choice == "3":
                    payment = UPIPayment()
                else:
                    print("Invalid choice, defaulting to Cash")
                    payment = CashPayment()

                payment.process_payment(fee)

                # Free the spot
                i.remove_vechile()
                self.dic1[i.size] += 1
                return
        else:
            print("Vehicle is not parked")

