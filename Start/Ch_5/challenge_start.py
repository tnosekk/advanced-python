# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True],
    ],
    [["dress", "M", False, True], ["whites", 5.25], ["darks", 12.5]],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True],
    ],
]

# TODO: process each order

for order in test_orders:
    total_price = 0.0

    print("===================")
    for item in order:
        match item:
            case "shirt" | "pants" | "jacket" | "dress" as garmet, size, starch, sameday:
                total_price += 12.95
                if starch:
                    total_price += 2.00
                if sameday:
                    total_price += 10.00
                print(
                    f"Dry Clean:({size}) {garmet}",
                    "Starched" if starch else "",
                    "same-day" if sameday else "",
                )

            case str() as desc, weight:
                if weight >= 15.0:
                    total_price += (weight * 4.95) * 0.9
                else:
                    total_price += weight * 4.95

                print(f"Wash/Fold: {desc}, weight {weight:.1f}")

            case "comforter" | "cover" as blanket, dry_clean, size:
                total_price += 25.00
                print(f"Blanket: ({size}) {blanket}", "Dry clean" if dry_clean else "")
            case _:
                print("Invalid item format")
    print(f"Order total: {total_price:.2f}")
    print("===================")
