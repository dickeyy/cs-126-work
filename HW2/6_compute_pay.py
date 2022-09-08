total_hours = 4 + 5 + 8 + 4
salary = 8.75
tax = 0.20

total_pay = total_hours * salary
tax_owed = total_hours * salary * tax

def main():
    # Calculate pay at work based on hours worked each day
    print("My total hours worked:")
    print(total_hours)

    print("My hourly salary:")
    print(salary)

    print("My total pay:")
    print(total_pay)

    print("My taxes owed:")  # 20% tax
    print(tax_owed)

main()