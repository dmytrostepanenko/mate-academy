def count_matching_socks(colors: list) -> int:
    # write your code here
    if len(colors) == 0:
        return 0
        
    all_collors = {}
    unic_colors = set(colors)
    for color in unic_colors:
        all_collors[color] = colors.count(color) // 2
    
    max_color = max(all_collors.values())
    counter = 0
    for value in all_collors.values():
        if max_color == value:
            counter += 1

    return max_color * counter
    
    


print(count_matching_socks([10, 10]))  # одна пара шкарпеток кольору 10
print(count_matching_socks([2, 2, 2, 2, 2]))  # дві пари шкарпеток кольору 2
print(count_matching_socks([10, 20, 30, 40, 50, 60]))  # усі шкарпетки різних кольорів — 0 пар
print(count_matching_socks([10, 20, 30, 10, 20, 60]))  # 2 пари, одна кольору 10 і одна кольору 20
