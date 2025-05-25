class Payment:
    def __init__(self, customer_name, policy_number, amount_due, amount_paid, payment_date, status):
        self.customer_name = customer_name
        self.policy_number = policy_number
        self.amount_due = amount_due
        self.amount_paid = amount_paid
        self.payment_date = payment_date
        self.status = status  # "Paid" or "Unpaid"

    def display_payment_info(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Policy Number: {self.policy_number}")
        print(f"Amount Due: {self.amount_due}")
        print(f"Amount Paid: {self.amount_paid}")
        print(f"Payment Date: {self.payment_date}")
        print(f"Status: {self.status}")

    def process_payment(self, amount, payment_date):
        self.amount_paid += amount
        self.payment_date = payment_date
        if self.amount_paid >= self.amount_due:
            self.status = "Paid"
            print(f"Payment complete for {self.customer_name}.")
        else:
            self.status = "Partial"
            print(f"Partial payment received for {self.customer_name}.")

    def send_reminder(self):
        if self.status != "Paid":
            print(f"Reminder: Payment is due for {self.customer_name} (Policy: {self.policy_number}).")

    def apply_penalty(self, penalty_amount):
        if self.status != "Paid":
            self.amount_due += penalty_amount
            print(f"Penalty of {penalty_amount} applied to {self.customer_name}. New amount due: {self.amount_due}")
