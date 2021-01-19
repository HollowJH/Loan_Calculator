import math
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = vars(parser.parse_args())

i = args["interest"]
p = args["principal"]
n = args["periods"]
payment = args["payment"]


def time(i=args["interest"], p=args["principal"], payment=args["payment"]):
    i = i / 1200 if i is not None else 1
    n_months = int(math.ceil(math.log(payment / (payment - i * p), 1 + i)))
    month = "1 month" if n_months % 12 == 1 else f"{n_months % 12} months"
    if n_months % 12 == 0 and n_months >= 12:
        if n_months == 12:
            answer = "It will take 1 year to repay this loan!"
        else:
            answer = f"It will take {n_months // 12} years to repay this loan!"
    else:
        answer = f"It will take {n_months // 12} years and {month} to repay this loan!"
    overpay = f"Overpayment = {int(n_months * payment - p)}"
    return [answer, overpay]


if list(args.values()).count(None) < 2:
    values = list(args.values())
    values = [i for i in values[1:] if i is not None]
    if not all([True if i > 0 else False for i in values[1:]]):
        print("Incorrect parameters.")
    if args["type"] == "diff" and (len(args) == 4 and "payment" not in args.keys() or len(args) == 5):
        i = i / 1200 if i is not None else 1
        total = 0

        for m in range(1, n + 1):
            month = math.ceil(p / n + i * (p - ((p * (m - 1)) / n)))
            total += month
            print(f"Month {m}: payment is {month}")
        print(f"Overpayment = {total - p}")

    elif args["type"] == "annuity":
        if args["principal"] is not None:
            if args["payment"] and args["interest"]:
                result = time()
                print(result[0])
            else:
                i = args["interest"] / 1200 if args["interest"] is not None else 1
                p = args["principal"]
                n = args["periods"]
                payment = math.ceil(p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
                result = time(payment=payment)
                print(payment)
            print(result[1])
        else:
            i = i / 1200 if i is not None else 1
            p = math.floor(payment / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))

            print(f"Your loan principal = {p}!")
            print(f"Overpayment = {int(n * payment - p)}")

    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")
