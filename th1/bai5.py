import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrival_web.logic import AND, OR

if __name__ == "__main__":
    arr1 = [1, 6, 8, 9, 14, 20]
    arr2 = [2, 3, 6, 8, 11, 14, 18]
    print("Tập hợp 1:", arr1)
    print("Tập hợp 2:", arr2)
    print("Giao của 2 tập hợp:", AND(arr1, arr2))
    print("Hợp của 2 tập hợp:", OR(arr1, arr2))