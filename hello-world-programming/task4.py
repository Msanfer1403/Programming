# Task4 Data Types .py

from config import IVA
from config import DISCOUNT
from config import CURRENCY

total = 100 * IVA
final  = total - total * DISCOUNT
print (final, "CURRENCY:", CURRENCY)