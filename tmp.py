from retrival_web.logic import AND, OR, AND_NOT

a = [1, 2, 9, 14, 16]
b = [14, 9, 1]
print(AND(a, b))
print(OR(a, b))
print(AND_NOT(a, b))