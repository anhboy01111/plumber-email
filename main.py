import os

def generate_entry():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = (
        "Subject: No more receipts on your dashboard\n\n"
        "Hi Dave,\n\n"
        "Between 6am emergency callouts, merchants, and fitting boilers, "
        "the last thing you need after a 12-hour day is sorting receipts at the kitchen table.\n\n"
        "I provide simple bookkeeping tailored for local plumbing firms:\n"
        "- Snap photos of parts and fuel receipts right from your cab.\n"
        "- We match invoices to jobs and keep your accounts audit-ready.\n"
        "- Flat £30 per week for both vans. No contracts.\n\n"
        "First two weeks are completely on us to test.\n\n"
        "Reply yes if you want your evenings back, and I will drop by Monday.\n\n"
        "Best,\nSam Miller"
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    generate_entry()
