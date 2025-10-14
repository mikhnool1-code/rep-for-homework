import xml.etree.ElementTree as ET


def calculate_total_cost(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        total = 0

        for item in root.findall("item"):
            price = float(item.find("price").text)
            quantity = int(item.find("quantity").text)
            total += price * quantity

        return total
    except Exception:
        return "Wrong XML format or file error"
