# This module access the manager module

from manager import greeting as gt
from manager import emp_id as id
from manager import emp_name as name
from manager import emp_pass

print('Current module is:', __name__)
print(emp_pass)

n=0
for i in name :
    gt(i) 
    print('Your id is:', id[n])
    n += 1