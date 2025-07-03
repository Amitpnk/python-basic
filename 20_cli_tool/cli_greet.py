# cli_greet.py
# A simple CLI tool using argparse

import argparse

def main():
    # 🧰 Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Greet a user with name and age.")

    # ➕ Define expected arguments
    parser.add_argument("name", help="Name of the user")
    parser.add_argument("--age", type=int, help="Age of the user", default=0)

    # 🧾 Parse arguments from command line
    args = parser.parse_args()

    # 🧑 Output
    print(f"👋 Hello, {args.name}!")
    if args.age > 0:
        print(f"🎂 You are {args.age} years old.")
    else:
        print("📅 Age not provided.")

if __name__ == "__main__":
    main()
