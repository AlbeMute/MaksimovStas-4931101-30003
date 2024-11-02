# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    participants_1 = group1.split(delimiter)
    participants_2 = group2.split(delimiter)
    common_participants = set(participants_1) & set(participants_2)
    sorted_common_participants = sorted(common_participants)
    return sorted_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(result)
