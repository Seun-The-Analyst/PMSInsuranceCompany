class PolicyHolder:
    def __init__(self, name, policy_number, age, address, phone, email, policy_type, premium_amount, start_date, end_date):
        self.name = name
        self.policy_number = policy_number
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.policy_type = policy_type
        self.premium_amount = premium_amount
        self.start_date = start_date
        self.end_date = end_date

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Policy Number: {self.policy_number}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Policy Type: {self.policy_type}")
        print(f"Premium Amount: {self.premium_amount}")
        print(f"Policy Start Date: {self.start_date}")
        print(f"Policy End Date: {self.end_date}")

class PolicyManagementSystem:
    def __init__(self):
        self.active_policyholders = []
        self.suspended_policyholders = []

    def register_policyholder(self, policyholder):
        self.active_policyholders.append(policyholder)
        print(f"Policyholder {policyholder.name} registered successfully.")

    def suspend_policyholder(self, policy_number):
        for holder in self.active_policyholders:
            if holder.policy_number == policy_number:
                self.active_policyholders.remove(holder)
                self.suspended_policyholders.append(holder)
                print(f"Policyholder {holder.name} suspended.")
                return
        print("Policyholder not found.")

    def reactivate_policyholder(self, policy_number):
        for holder in self.suspended_policyholders:
            if holder.policy_number == policy_number:
                self.suspended_policyholders.remove(holder)
                self.active_policyholders.append(holder)
                print(f"Policyholder {holder.name} reactivated.")
                return
        print("Policyholder not found in suspended list.")
