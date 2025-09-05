def AND(set1: list[int], set2: list[int]) -> list[int]:
    """
    Trả về giao của hai danh sách số nguyên.
    Hai danh sách đầu vào được giả định là không có phần tử trùng lặp.

    Parameters:
        set1 (list[int]): Danh sách số nguyên thứ nhất.
        set2 (list[int]): Danh sách số nguyên thứ hai.

    Returns:
        list[int]: Danh sách các phần tử xuất hiện ở cả hai danh sách.
    """
    _set1 = sorted(set1)
    _set2 = sorted(set2)
    result = []
    i, j = 0, 0

    while (i < len(_set1)) and (j< len(set2)):
        if _set1[i] == _set2[j]:
            result.append(_set1[i])
            i += 1
            j += 1
        elif _set1[i] < _set2[j]:
            i += 1
        else:
            j += 1
    
    return result.copy()

def OR(set1: list[int], set2: list[int]) -> list[int]:
    """
    Trả về hợp của hai danh sách số nguyên.
    Hai danh sách đầu vào được giả định là không có phần tử trùng lặp.

    Parameters:
        set1 (list[int]): Danh sách số nguyên thứ nhất.
        set2 (list[int]): Danh sách số nguyên thứ hai.

    Returns:
        list[int]: Danh sách các phần tử xuất hiện trong ít nhất một trong hai danh sách.
    """
    _set1 = sorted(set1)
    _set2 = sorted(set2)
    result = []
    i, j = 0, 0

    while (i < len(_set1)) and (j < len(_set2)):
        if (_set1[i] == _set2[j]):
            result.append(_set1[i])
            i += 1
            j += 1
        elif _set1[i] < _set2[j]:
            result.append(_set1[i])
            i += 1
        else:
            result.append(_set2[j])
            j += 1

    while (i < len(_set1)):
        result.append(_set1[i])
        i += 1

    while (j < len(_set2)):
        result.append(_set2[j])
        j +=1

    return result.copy()

def AND_NOT(set1: list[int], set2: list[int]) -> list[int]:
    """
    Trả về hiệu của hai danh sách số nguyên (các phần tử trong set1 nhưng không có trong set2).
    Hai danh sách đầu vào được giả định là không có phần tử trùng lặp.

    Parameters:
        set1 (list[int]): Danh sách số nguyên thứ nhất.
        set2 (list[int]): Danh sách số nguyên thứ hai.

    Returns:
        list[int]: Danh sách các phần tử xuất hiện trong set1 nhưng không có trong set2.
    """
    _set1 = sorted(set1)
    _set2 = sorted(set2)
    result = []
    i, j = 0, 0

    while (i < len(_set1)) and (j < len(_set2)):
        if (_set1[i] == _set2[j]):
            i += 1
            j += 1
        elif _set1[i] < _set2[j]:
            result.append(_set1[i])
            i += 1
        else:
            j += 1

    while (i < len(_set1)):
        result.append(_set1[i])
        i += 1

    return result.copy()