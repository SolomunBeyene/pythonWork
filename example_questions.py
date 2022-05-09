# 1) Given an array of integers, convert them to a single int made up of the digits
example1 = [1, 2, 3, 3,5]
for i in example1:
    print(i, end="")

# 2. Take a string and return it with all the vowels removed in uppercase
def anti_vowel(string):
    if string == 'x':
        exit();
    else:
        newstr = string;
        print("\nRemoving vowels from the given string");
        vowels = ('a', 'e', 'i', 'o', 'u');
        for x in string.lower():
            if x in vowels:
                newstr = newstr.replace(x,"");
        print("New string after successfully removed all the vowels:");
        print(newstr);

anti_vowel("solumon")

# 4. For an array of ints[] find the missing number in the array. The array might not be in order
def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    print(total - sum_of_A)

getMissingNo([1,2,3,4,5,6,7,9])

# 5. For an int[] array, find a pair of numbers who's sum is closest to zero
def minAbsSumPair(arr,arr_size):
	inv_count = 0
	if arr_size < 2:
		print("Invalid Input")
		return
	min_l = 0
	min_r = 1
	min_sum = arr[0] + arr[1]
	for l in range (0, arr_size - 1):
		for r in range (l + 1, arr_size):
			sum = arr[l] + arr[r]				
			if abs(min_sum) > abs(sum):		
				min_sum = sum
				min_l = l
				min_r = r
	print("The two elements whose sum is minimum are",
			arr[min_l], "and ", arr[min_r])
arr = [1, 2, 4, 7, 6, 3]
minAbsSumPair(arr, 6)

# 6. Shopping list: 2 items of the same price = 20% of their total and any item over £10 has 30% off. Find the total price


# 7. For a String, create an array of all the duplicate letters
string = "ssollomunbeteyenee"
duplicates = []
for char in string:
   if string.count(char) > 1:
    if char not in duplicates:
        duplicates.append(char)
print(duplicates)

 

# 8. Find the second highest number in an array
numbers = [10, 33, 4, 20, 100]
numbers.sort()
print("Second largest element is:", numbers[-2])

# 9. Create a 2 value array which counts all the consonants and vowels in a string
def isConsonant(ch):	
	ch = ch.upper()
	return not (ch == 'A' or ch == 'E' or
				ch == 'I' or ch == 'O' or
				ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
def totalConsonants(string):	
	count = 0	
	for i in range(len(string)):
		if (isConsonant(string[i])):
			count += 1		
	return count
string = "solomunbeyene"
print(totalConsonants(string))