import re

def parse_price(price_text: str) -> float:
    return float(re.sub(r"[^\d.]", "", price_text))