from datetime import datetime, timezone


def discount_price(price, discount=0, is_back_friday=False, is_boxing_day=False):
    utc_today = datetime.now(timezone.utc).date()

    def calculate_discount(local_discount=0):
        return round(price - ((price / 100) * local_discount))

    def check_deal_day(month, day):
        return utc_today.month == month and utc_today.day == day

    if check_deal_day(11, 27) or is_back_friday:  # Back Friday
        return calculate_discount(40)
    elif check_deal_day(12, 25) or is_boxing_day:  # boxing day
        return calculate_discount(20)
    else:
        return calculate_discount()


discount_price_back_friday = discount_price(919, is_back_friday=True)
discount_price_boxing_day = discount_price(919, is_boxing_day=True)

print(f"Back friday Price :: {discount_price_back_friday}, Boxing day Price :: {discount_price_boxing_day}", sep=", ")
