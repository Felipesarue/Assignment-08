# # Assignment 8 This repository contains my work for Assignment 8.

## Files Included
#- main.py

## What I Practiced
#In this assignment, I practiced working with Python dictionaries and basic data aggregation. I created nested data structures to manage customers, services, and projects, and performed operations such as data lookup, updates, filtering, and summarization. I also practiced using dictionary comprehensions, functions, and basic business logic to analyze service usage, budgets, and customer activity.

# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Consulting": 220,
    "Cybersecurity": 200,
    "IT Support": 95
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "TechNova Inc",
    "contact_person": "Alice Johnson",
    "email": "alice@technova.com",
    "phone": "555-1001"
}

customer2 = {
    "company_name": "DataSphere LLC",
    "contact_person": "Bob Smith",
    "email": "bob@datasphere.com",
    "phone": "555-1002"
}

customer3 = {
    "company_name": "CloudPeak Systems",
    "contact_person": "Carol White",
    "email": "carol@cloudpeak.com",
    "phone": "555-1003"
}

customer4 = {
    "company_name": "SecureNet Corp",
    "contact_person": "David Brown",
    "email": "david@securenet.com",
    "phone": "555-1004"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)

for cid, info in customers.items():
    print(f"Customer ID: {cid}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Technology"

print("\n\nUpdating Customer Information:")
print("-" * 60)
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries
project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Sales Data Dashboard", "service": "Data Analysis", "hours": 80, "budget": 14000}
project3 = {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 150, "budget": 33000}
project4 = {"name": "Security Audit", "service": "Cybersecurity", "hours": 90, "budget": 18000}
project5 = {"name": "Helpdesk Setup", "service": "IT Support", "hours": 60, "budget": 6000}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

print("\n\nProject Information:")
print("-" * 60)
for cid, plist in projects.items():
    print(cid, plist)

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)

for cid, plist in projects.items():
    for project in plist:
        rate = services[project["service"]]
        cost = rate * project["hours"]
        print(f"{project['name']} for {cid} costs ${cost}")

# TODO 9: Customer statistics
print("\n\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", list(customers.keys()))
companies = [c["company_name"] for c in customers.values()]
print("Customer Companies:", companies)
print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
service_counts = {}

for plist in projects.values():
    for project in plist:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial aggregations
all_hours = []
all_budgets = []

for plist in projects.values():
    for p in plist:
        all_hours.append(p["hours"])
        all_budgets.append(p["budget"])

total_hours = sum(all_hours)
total_budget = sum(all_budgets)
avg_budget = total_budget / len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)

print("\n\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)

for cid, info in customers.items():
    plist = projects.get(cid, [])
    hours = sum(p["hours"] for p in plist)
    budget = sum(p["budget"] for p in plist)

    print(f"{info['company_name']} ({cid})")
    print(" Projects:", len(plist))
    print(" Total Hours:", hours)
    print(" Total Budget:", budget)
    print()

# TODO 13: Rate adjustments using dictionary comprehension
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
active_customers = {cid: customers[cid] for cid in customers if cid in projects}

print("\n\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Project summaries using dictionary comprehension
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    for field in required:
        if field not in customer_dict:
            return False
    return True

print("\n\nCustomer Validation:")
print("-" * 60)

for cid, info in customers.items():
    print(cid, validate_customer(info))

# TODO 18: Project status tracking
statuses = ["active", "completed", "pending"]
status_counts = {"active": 0, "completed": 0, "pending": 0}

i = 0
for plist in projects.values():
    for p in plist:
        p["status"] = statuses[i % 3]
        status_counts[p["status"]] += 1
        i += 1

print("\n\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function
def analyze_customer_budgets(projects_dict):
    results = {}

    for cid, plist in projects_dict.items():
        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count > 0 else 0

        results[cid] = {
            "total": total,
            "average": avg,
            "count": count
        }

    return results


print("\n\nDetailed Budget Analysis:")
print("-" * 60)

budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):

    used_services = set()

    if customer_id in projects:
        for p in projects[customer_id]:
            used_services.add(p["service"])

    unused_services = [s for s in services if s not in used_services]

    budgets = [p["budget"] for p in projects.get(customer_id, [])]
    avg_budget = sum(budgets) / len(budgets) if budgets else 0

    recommendations = []

    for service in unused_services:
        if services[service] * 50 <= avg_budget or avg_budget == 0:
            recommendations.append(service)

    return recommendations


print("\n\nService Recommendations:")
print("-" * 60)

for cid in customers:
    recs = recommend_services(cid, customers, projects, services)
    print(cid, "Recommended Services:", recs)
