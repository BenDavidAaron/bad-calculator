'''
This is a script that generates N number of test cases.
each case consists of three comma-delimited values on a line.
the first value is the sum (result) of the two following 
randomly generated integers (features) on each line.
Format:
sum,int_1,int_2\n
'''

from random import randint
from tqdm import tqdm

def add_two_random_ints():
	int_1 = randint(1,9)
	int_2 = randint(1,9)
	return "%s,%s,%s\n" % (int_1 + int_2, int_1, int_2)

number_cases = int(input("How many cases do you want to generate?\n"))

with open("%1.1E cases.csv" % number_cases, "w") as f:
	f.writelines('A,Q1,Q2')
	for _ in tqdm(range(number_cases)):
		f.writelines(add_two_random_ints())