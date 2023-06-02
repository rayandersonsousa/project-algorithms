def is_anagram(first_string, second_string):
    first_string_lower = first_string.lower()
    second_string_lower = second_string.lower()

    sort_first_string = string_sort(first_string_lower)
    sort_second_string = string_sort(second_string_lower)

    true_or_false = sort_first_string == sort_second_string

    return (sort_first_string, sort_second_string, true_or_false)


def string_sort(string):
    if len(string) <= 1:
        return string

    pivot = string[0]

    smaller = "".join([char for char in string  if char < pivot])
    same = "".join([char for char in string  if char == pivot])
    higher = "".join([char for char in string  if char > pivot])

    return string_sort(smaller) + same + string_sort(higher)