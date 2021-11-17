class Warehouse:
    warehouse_dict = {}

    def __init__(self, item, count: int):
        self.item = item
        self.count = count

    def stay_in_warehouse(self):
        if self.item in self.warehouse_dict:
            for key, value in self.warehouse_dict.items():
                if key == self.item:
                    self.warehouse_dict[key] += self.count
        else:
            self.warehouse_dict[self.item] = self.count
        return f'На складе сейчас хранится: {self.warehouse_dict}'


class Moving(Warehouse):

    def __init__(self, secondary_office, item, amount):
        self.parent_warehouse = {}
        self.secondary_office = secondary_office
        self.item = item
        self.amount = amount

    @property
    def move_to(self):
        if self.item in Warehouse.warehouse_dict:
            for key, value in Warehouse.warehouse_dict.items():
                if key == self.item and value >= self.amount:
                    Warehouse.warehouse_dict[key] -= self.amount
                    self.parent_warehouse[key] = self.amount
                elif key == self.item and value < self.amount:
                    print('На складе нет необходимого количества')
        return f'В подразделение {self.secondary_office} отгружен товар: {self.parent_warehouse}. Состояние основного склада: {Warehouse.warehouse_dict}'


class OfficeEquipment:
    def __init__(self, manufacturer, model, year, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
        self.catalog = {}


class Printer(OfficeEquipment):
    def __init__(self, label, model, year, technology, print_type, print_format, max_speed):
        OfficeEquipment.__init__(self, label, model, year)
        self.technology = technology
        self.print_type = print_type
        self.print_format = print_format
        self.max_speed = max_speed


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, year, scan_technology, weight, book_scan=bool):
        OfficeEquipment.__init__(self, manufacturer, model, year)
        self.scan_technology = scan_technology
        self.weight = weight
        self.book_scan = book_scan


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, model, year, display, display_size, copy_speed):
        OfficeEquipment.__init__(self, manufacturer, model, year)
        self.display = display
        self.display_size = display_size
        self.copy_speed = copy_speed


