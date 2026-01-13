"""
У цьому завданні тобі потрібно показати юзерам хто з їх друзів онлайн і готовий чатитись 🖥

Створи функцію who_is_online(), яка:

Приймає список словників friends.
Визначає хто з них online, offline чи away.
Якщо юзер має статус online, але його не було в мережі більш ніж 10 хвилин 
(lastActivity > 10), то можна вважати, що фактично його статус вже away.
"""

def who_is_online(friends: list) -> dict:
    result_dict = {
        "online": [],
        "offline": [],
        "away": []
    }
    if len(friends) == 0:
        return result_dict
    
    for inner_dict in friends:
        if inner_dict["status"] == "online" and inner_dict["lastActivity"] <= 10:
            result_dict["online"].append(inner_dict["username"])
        elif inner_dict["status"] == "online" and inner_dict["lastActivity"] > 10:
            result_dict["away"].append(inner_dict["username"])
        else:
            result_dict["offline"].append(inner_dict["username"])

    result_dict_copy = result_dict.copy()
    for key, value in result_dict_copy.items():
        if len(value) == 0:
            result_dict.pop(key)

    return result_dict


if __name__ == "__main__":
    test = [{
  "username": "Alice",
  "status": "online",
  "lastActivity": 10
}, {
  "username": "Lucy",
  "status": "offline",
  "lastActivity": 22
}, {
  "username": "Bob",
  "status": "online",
  "lastActivity": 10
}]

print(who_is_online(test))