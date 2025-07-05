import json
import os

DATA_FILE = "samples.json"

def load_samples():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_samples():
    with open(DATA_FILE, "w") as f:
        json.dump(samples, f, indent=4)

samples = load_samples()

def view_samples():
    print("\nCurrent Samples:")
    if not samples:
        print("No samples yet.")
        return
    for i, sample in enumerate(samples, start=1):
        print(f"{i}. Sample ID: {sample['Sample ID']}")
        print(f"   Date: {sample['Date']}")
        print(f"   Method: {sample['Method']}")
        print(f"   Notes: {sample['Notes']}\n")

def add_sample():
    print("\nEnter new sample details:")
    sample_id = input("Sample ID: ")
    date = input("Date (YYYY-MM-DD): ")
    method = input("Method: ")
    notes = input("Notes: ")

    sample = {
        "Sample ID": sample_id,
        "Date": date,
        "Method": method,
        "Notes": notes
    }
    samples.append(sample)
    save_samples()
    print(f"Sample {sample_id} added.")

def edit_sample():
    view_samples()
    if not samples:
        return
    try:
        index = int(input("Enter the number of the sample to edit: ")) - 1
        if 0 <= index < len(samples):
            sample = samples[index]
            print("\nLeave blank to keep current value.")
            sample['Sample ID'] = input(f"Sample ID [{sample['Sample ID']}]: ") or sample['Sample ID']
            sample['Date'] = input(f"Date [{sample['Date']}]: ") or sample['Date']
            sample['Method'] = input(f"Method [{sample['Method']}]: ") or sample['Method']
            sample['Notes'] = input(f"Notes [{sample['Notes']}]: ") or sample['Notes']
            save_samples()
            print("Sample updated.")
        else:
            print("Invalid sample number.")
    except ValueError:
        print("Invalid input.")

def delete_sample():
    view_samples()
    if not samples:
        return
    try:
        index = int(input("Enter the number of the sample to delete: ")) - 1
        if 0 <= index < len(samples):
            deleted = samples.pop(index)
            save_samples()
            print(f"Sample {deleted['Sample ID']} deleted.")
        else:
            print("Invalid sample number.")
    except ValueError:
        print("Invalid input.")

def search_samples():
    query = input("Search by Sample ID, Method, or Date: ").strip().lower()
    results = [
        s for s in samples
        if query in s['Sample ID'].lower()
        or query in s['Method'].lower()
        or query in s['Date'].lower()
    ]

    if results:
        print("\nSearch Results:")
        for sample in results:
            print(f"- Sample ID: {sample['Sample ID']}")
            print(f"  Date: {sample['Date']}")
            print(f"  Method: {sample['Method']}")
            print(f"  Notes: {sample['Notes']}\n")
    else:
        print("No matching samples found.")

def main_menu():
    while True:
        print("\n📁 LIMS Sample Tracker")
        print("-" * 25)
        print("1. View all samples")
        print("2. Add a new sample")
        print("3. Edit a sample")
        print("4. Delete a sample")
        print("5. Search samples")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            view_samples()
        elif choice == '2':
            add_sample()
        elif choice == '3':
            edit_sample()
        elif choice == '4':
            delete_sample()
        elif choice == '5':
            search_samples()
        elif choice == '6':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please choose 1–6.")

# Run the menu
if __name__ == "__main__":
    main_menu()
