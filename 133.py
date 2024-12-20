smaller_list2 = [1, 3, 5]
smaller_list3 = []
smaller_list4 = [1,2,3,4,5,6]


def check_sublist(larger, smaller):
    if not smaller:
        return True
    return any(larger[i:i+len(smaller)] == smaller for i in range(len(larger) - len(smaller) + 1))


print(f"Является ли {smaller_list1} подсписком {larger_list}? {check_sublist(larger_list, smaller_list1)}")
print(f"Является ли {smaller_list2} подсписком {larger_list}? {check_sublist(larger_list, smaller_list2)}")
print(f"Является ли {smaller_list3} подсписком {larger_list}? {check_sublist(larger_list, smaller_list3)}")
print(f"Является ли {smaller_list4} подсписком {larger_list}? {check_sublist(larger_list, smaller_list4)}")