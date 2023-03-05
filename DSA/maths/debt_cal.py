def emi_calculator(loan_amount, no_of_years, roi):
    # emi formula [P.r.(1+r)^n/ (1+r)^n-1]
    p = loan_amount
    n = no_of_years * 12  # no of months
    r = (roi / 12) / 100  # monthly basis interest
    emi = ((p * r) * (1 + r) ** n) / (((1 + r) ** n) - 1)
    interest = emi * n - p
    total = emi * n
    print(f"for {no_of_years=} {interest=} {total=}")
    return emi


if __name__ == '__main__':
    print(f"{emi_calculator(1000000, 10, 10.5)=}")
