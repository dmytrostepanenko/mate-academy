"""
Реалізуй функцію sum_dicts(), яка:

Приймає необмежену кількість словників.
Повертає один словник, який об'єднує усі вхідні словники.
Примітки:

усі значення у словнику є числами;
якщо ключі об'єктів збігаються, значення для відповідних ключів сумуються;
функція завжди повертає словник;
числа в словнику можуть бути додатними та від'ємними.
"""

def sum_dicts(*args: dict) -> dict:
    result_dict = {}

    for inner_dict in args:
        for key, value in inner_dict.items():
            if result_dict.get(key) != None:
                result_dict[key] += value
            else:
                result_dict[key] = value

    return result_dict


if __name__ == "__main__":
    first = {"a": 2, "b": 4};
    second = {"a": 2, "b": 10};
    third = {"d": -5};

    print(sum_dicts(first) == {"a": 2, "b": 4})
    print(sum_dicts(first, third) == {"a": 2, "b": 4, "d": -5})
    print(sum_dicts(first, second, third) == {"a": 4, "b": 14, "d": -5})
