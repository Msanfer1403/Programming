# Task3 Data Types .py

values = [10, 3.14, "hi", True, None]
for v in values:
    print(f"{str(v):<8} -> {type(v)}")

print (3 + 3)

print (0.1 + 0.2 == 0.3)

# It says false because of floating point precision
# issues in Python. The sum of 0.1 and 0.2 does not exactly 
# equal 0.3 due to how floating point numbers are 
# represented in binary.