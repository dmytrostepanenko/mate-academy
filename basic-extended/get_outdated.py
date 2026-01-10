def get_outdated(robots: list, new_version: int) -> list:
    # write your code here
    outdated_list = []
    for index in range(len(robots)):
        if robots[index]["core_version"] < new_version:
            outdated_list.append(index)
    return outdated_list


if __name__ == "__main__":
    robots = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]

print(get_outdated(robots, 10)) # [0, 3]
print(get_outdated(robots, 14)) # [0, 1, 3]
print(get_outdated(robots, 8))# []
print(get_outdated(robots, 18)) # [0, 1, 2, 3, 4]
