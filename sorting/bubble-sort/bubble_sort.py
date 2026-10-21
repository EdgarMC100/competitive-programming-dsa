"""Bubble sort: repeatedly swap neighboring elements until the list is sorted."""


def show(items):
    return "[ " + ", ".join(str(item) for item in items) + " ]"


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        print(f"i:{i}")
        swapped = False
        for j in range(n - i - 1):
            print(f"j{j} -> {numbers[j]}, j+1 -> {numbers[j + 1]} ", show(numbers))
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
                print("Swapped positions")
        if not swapped:
            break
    return numbers


if __name__ == "__main__":
    print(show(bubble_sort([5, 3, 7, 10, 1])))
