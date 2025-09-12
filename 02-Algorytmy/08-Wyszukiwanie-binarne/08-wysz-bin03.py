# Zdefiniuj listę z duplikatami oraz zwróć pierwszy i ostatni indeks szukanego elementu w liście z duplikatami.

def find_first_and_last(arr, x):
    def find_first():
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                result = mid
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def find_last():
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                result = mid
                left = mid + 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return find_first(), find_last()


print(find_first_and_last([1, 2, 2, 2, 3, 4, 5, 6, 7, 8], 2))
