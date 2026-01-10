def make_lemonade(sugar_grams: int, water_liters: int) -> int:
    sugar_portion = sugar_grams // 100
    water_portion = water_liters * 1000 // 500
    if water_liters:
        if water_portion > sugar_portion:
            return sugar_portion
        else:
            return water_portion
    else:
        return "Nan"
    

if __name__ == "__main__":
    print(make_lemonade(500, 2)) # 4
    print(make_lemonade(600, 6)) # 6
    print(make_lemonade(300, 0)) # "NaN"
