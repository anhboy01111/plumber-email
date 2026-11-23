import os

def generate_entry():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = (
        "Subject: Bookkeeping for your two vans\n\n"
        "Hi Dave,\n\n"
        "Between emergency callouts, merchants, and fitting boilers, "
        "the last thing you need after a long shift is doing invoices at home.\n\n"
        "I provide simple bookkeeping tailored for trade firms:\n"
        "- Snap photos of parts and fuel receipts right from your cab.\n"
        "- We match invoices to jobs and keep your accounts audit-ready.\n"
        "- Flat 30 pounds per week for both vans. No contracts.\n\n"
        "First two weeks are free to test.\n\n"
        "Reply yes if you want your evenings back, and I will drop by Monday.\n\n"
        "Best,\nSam Miller"
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    generate_entry()