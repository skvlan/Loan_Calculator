import math
import argparse


def calculate_differentiated_payments(principal, months, interest_rate):
    i = interest_rate / 12
    payments = []
    for m in range(1, months + 1):
        payment = principal / months + i * (principal - (principal * (m - 1)) / months)
        payments.append(math.ceil(payment))
    return payments


def calculate_number_of_months(principal, monthly_payment, interest_rate):
    i = interest_rate / 12
    n = math.log(monthly_payment / (monthly_payment - i * principal), 1 + i)
    return math.ceil(n)


def calculate_loan_principal(monthly_payment, months, interest_rate):
    i = interest_rate / 12
    principal = monthly_payment / ((i * math.pow(1 + i, months)) / (math.pow(1 + i, months) - 1))
    return math.ceil(principal)


def calculate_annuity_payment(principal, months, interest_rate):
    i = interest_rate / 12
    monthly_payment = principal * ((i * math.pow(1 + i, months)) / (math.pow(1 + i, months) - 1))
    return math.ceil(monthly_payment)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Loan Calculator")
    parser.add_argument("--type", choices=["diff", "annuity"], help="Type of payment: diff or annuity")
    parser.add_argument("--principal", type=float, help="Loan principal amount")
    parser.add_argument("--payment", type=float, help="Monthly payment amount")
    parser.add_argument("--periods", type=int, help="Number of months")
    parser.add_argument("--interest", type=float, help="Annual interest rate")
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.type == "diff" and args.principal is not None and args.periods is not None and args.interest is not None:
        payments = calculate_differentiated_payments(args.principal, args.periods, args.interest / 100)
        total_payment = sum(payments)
        print("\n".join(f"Month {i}: payment is {math.ceil(p)}" for i, p in enumerate(payments, start=1)))
        print(f"\nOverpayment = {math.ceil(total_payment - args.principal)}")
    elif args.type == "annuity":
        if args.principal is not None and args.periods is not None and args.interest is not None:
            monthly_payment = calculate_annuity_payment(args.principal, args.periods, args.interest / 100)
            total_payment = monthly_payment * args.periods
            print(f"\nYour annuity payment = {monthly_payment}!")
            print(f"Overpayment = {math.ceil(total_payment - args.principal)}")
        elif args.payment is not None and args.periods is not None and args.interest is not None:
            principal = calculate_loan_principal(args.payment, args.periods, args.interest / 100)
            total_payment = args.payment * args.periods
            print(f"\nYour loan principal = {principal}!")
            print(f"Overpayment = {math.ceil(total_payment - principal)}")
        elif args.principal is not None and args.payment is not None and args.interest is not None:
            months = calculate_number_of_months(args.principal, args.payment, args.interest / 100)
            total_payment = args.payment * months
            if months < 12:
                print(f"\nIt will take {months} months to repay the loan!")
            elif months == 12:
                print("\nIt will take 1 year to repay the loan!")
            else:
                years = months // 12
                remaining_months = months % 12
                if remaining_months == 0:
                    print(f"\nIt will take {years} years to repay the loan!")
                else:
                    print(f"\nIt will take {years} years and {remaining_months} months to repay the loan!")
            print(f"Overpayment = {math.ceil(total_payment - args.principal)}")
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")

if __name__ == "__main__":
    main()



