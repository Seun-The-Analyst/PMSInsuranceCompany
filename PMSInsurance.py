from Policyholders import PolicyHolder
from products import InsuranceProduct, ProductManager
from payments import Payment

# Policy Holder Usage:
holder1 = PolicyHolder(
    name="Jane Smith",
    policy_number="INS123456",
    age=40,
    address="456 Elm St",
    phone="555-1234",
    email="jane.smith@email.com",
    policy_type="Life Insurance",
    premium_amount=1200.50,
    start_date="2024-01-01",
    end_date="2025-01-01"
)

holder2 = PolicyHolder(
    name="John Doe",
    policy_number="INS654321",
    age=35,
    address="123 Main St",
    phone="555-5678",
    email="john.doe@email.com",
    policy_type="Health Insurance",
    premium_amount=800.75,
    start_date="2023-06-01",
    end_date="2024-06-01"
)

holder3 = PolicyHolder(
    name="Alice Johnson",
    policy_number="INS789012",
    age=30,
    address="789 Oak St",
    phone="555-8765",
    email="alice.johnson@email.com",
    policy_type="Auto Insurance",
    premium_amount=600.00,
    start_date="2023-03-15",
    end_date="2024-03-15"
)

holder4 = PolicyHolder(
    name="Bob Lee",
    policy_number="INS345678",
    age=45,
    address="321 Pine St",
    phone="555-4321",
    email="bob.lee@email.com",
    policy_type="Home Insurance",
    premium_amount=1500.00,
    start_date="2023-09-01",
    end_date="2024-09-01"
)

holder5 = PolicyHolder(
    name="Maria Gomez",
    policy_number="INS567890",
    age=28,
    address="654 Maple St",
    phone="555-6789",
    email="maria.gomez@email.com",
    policy_type="Travel Insurance",
    premium_amount=300.00,
    start_date="2023-12-01",
    end_date="2024-12-01"

)

# Store all holders in a list and display their info
holders = [holder1, holder2, holder3, holder4, holder5]
for holder in holders:
    holder.display_info()
    print("\n" + "-"*50 + "\n")  # Add spacing and a separator between outputs


# Insurance Product Usage:
products = [
    InsuranceProduct(
        product_id="LIFE001",
        name="Standard Life Insurance",
        description="Provides life coverage for the insured.",
        coverage_amount=100000,
        premium=500,
        term_years=20,
        product_type="Life",
        additional_services=["Accidental Death Benefit", "Critical Illness Rider"]
    ),
    InsuranceProduct(
        product_id="AUTO001",
        name="Comprehensive Auto Insurance",
        description="Covers damages to your car and third-party liability.",
        coverage_amount=20000,
        premium=300,
        term_years=1,
        product_type="Auto",
        additional_services=["Roadside Assistance", "Rental Car Coverage"]
    ),
    InsuranceProduct(
        product_id="HEALTH001",
        name="Family Health Plan",
        description="Health insurance for the entire family.",
        coverage_amount=50000,
        premium=800,
        term_years=1,
        product_type="Health",
        additional_services=["Telemedicine", "Annual Health Checkup"]
    ),
    InsuranceProduct(
        product_id="HOME001",
        name="Homeowners Insurance",
        description="Covers damages to your home and personal property.",
        coverage_amount=250000,
        premium=1200,
        term_years=1,
        product_type="Home",
        additional_services=["Home Security System", "Personal Liability Coverage"]
    ),
    InsuranceProduct(
        product_id="TRAVEL001",
        name="Travel Insurance",
        description="Covers trip cancellations, medical emergencies, and lost luggage.",
        coverage_amount=15000,
        premium=200,
        term_years=1,
        product_type="Travel",
        additional_services=["Trip Interruption Coverage", "Emergency Medical Assistance"]
    )
]

# Display all products
for product in products:
    product.display_product_info()
    print("-" * 40)

# Example ProductManager usage with the same products list
manager = ProductManager()
for product in products:
    manager.create_product(product)

# Update a product
manager.update_product("LIFE001", premium=600, description="Updated life coverage.")

# Suspend a product
manager.suspend_product("AUTO001")

# Remove a product
manager.remove_product("TRAVEL001")

# Display all products after updates
print("\nProducts after updates:\n")
for product in manager.products:
    product.display_product_info()
    print("-" * 40)




# Payment Usage for 5 customers:
payments = [
    Payment("Jane Smith", "INS123456", 1200.50, 1200.50, "2024-01-10", "Paid"),
    Payment("John Doe", "INS654321", 800.00, 0.00, None, "Unpaid"),
    Payment("Alice Johnson", "INS789012", 950.00, 950.00, "2024-02-15", "Paid"),
    Payment("Bob Lee", "INS345678", 1100.00, 0.00, None, "Unpaid"),
    Payment("Maria Gomez", "INS567890", 1500.00, 1500.00, "2024-03-05", "Paid")
]

# Example usage:
for payment in payments:
    payment.display_payment_info()
    payment.send_reminder()
    payment.apply_penalty(50)
    print("-" * 40)