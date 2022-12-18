import argparse

parser = argparse.ArgumentParser(
    prog="Sr Barriga Payment Workflow",
    description="Execute payment Workflow"
)

parser.add_argument(
    "-u", "--user", "--user to create a payment", type=str)

parser.add_argument(
    "-v", "--value", "--value to create a payment", type=float)

parser.add_argument(
    "-d", "--description", "--payment description", type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
