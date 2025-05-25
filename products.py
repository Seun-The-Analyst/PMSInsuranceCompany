class InsuranceProduct:
    def __init__(self, product_id, name, description, coverage_amount, premium, term_years, product_type, additional_services=None, active=True):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.coverage_amount = coverage_amount
        self.premium = premium
        self.term_years = term_years
        self.product_type = product_type  # e.g., 'Life', 'Health', 'Auto', 'Home'
        self.additional_services = additional_services if additional_services else []
        self.active = active  # Indicates if the product is active or suspended

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Coverage Amount: {self.coverage_amount}")
        print(f"Premium: {self.premium}")
        print(f"Term (years): {self.term_years}")
        print(f"Product Type: {self.product_type}")
        print(f"Additional Services: {', '.join(self.additional_services) if self.additional_services else 'None'}")
        print(f"Status: {'Active' if self.active else 'Suspended'}")

class ProductManager:
    def __init__(self):
        self.products = []

    def create_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' created successfully.")

    def update_product(self, product_id, **kwargs):
        for product in self.products:
            if product.product_id == product_id:
                for key, value in kwargs.items():
                    if hasattr(product, key):
                        setattr(product, key, value)
                print(f"Product '{product_id}' updated successfully.")
                return
        print(f"Product '{product_id}' not found.")

    def suspend_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                product.active = False
                print(f"Product '{product_id}' suspended.")
                return
        print(f"Product '{product_id}' not found.")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product '{product_id}' removed.")
                return
        print(f"Product '{product_id}' not found.")
