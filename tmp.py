from retrival_web.logic import AND, OR, AND_NOT

a = [1, 2, 3, 4]
b = [1, 2]
print(AND(a, b))
print(OR(a, b))
print(AND_NOT(a, b))