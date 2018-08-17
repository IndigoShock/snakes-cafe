

class Order:
    def __init__(self, uuid, category, price, name, item, quantity):
        self.uuid = uuid
        self.category = category
        self.price = price
        self.name = name
        self.item = item
        self.quantity = quantity

    # def __repr__(self):
    #     return f'<Employee ID: {self.emp_id}, Name: {self.first_name}>'
    # <Order #ba99d8... | Items: 4 | Total: $754.23>
