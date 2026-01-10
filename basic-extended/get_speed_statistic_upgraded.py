import math

def get_speed_statistic(test_results: list) -> list:
    # write your code here
    final = []
    final.append(min(test_results))
    final.append(max(test_results))
    final.append(math.floor(sum(test_results) / len(test_results)))

    return final