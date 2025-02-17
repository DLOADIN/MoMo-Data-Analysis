from datetime import datetime
import xml.etree.ElementTree as ET
from datetime import datetime


def convert_to_date(date_str: str) -> datetime:
    """Converts a string in eg: '10 May 2024 4:30:58 PM' format to a datetime object."""
    return datetime.strptime(date_str, "%d %b %Y %I:%M:%S %p")


def parse_amount_recieved(root):
    for element in root:
        if element.get("body").startswith("You have received"):
            msg_parts = element.get("body").split(".")
            amount = msg_parts[0].split(" ")[3]
            sender_firstname, senders_second_name = msg_parts[0].split()[6:8]
            id = int(element.get("date"))
            date = convert_to_date(element.get("readable_date"))
    return [id, sender_firstname, senders_second_name, amount, date]


def main():
    mytree = ET.parse("modified_sms_v2.xml")
    root = mytree.getroot()

    # test..
    def print_(*args):
        for arg in args:
            print(arg)

    print_(*parse_amount_recieved(root))


if __name__ == "__main__":
    main()
