

# Function to rotate string left and right by d length

def rotate(list1):
	list2 = list1[len(list1) - 1:] + list1[:len(list1) - 1]
	print(list2)



list_test = [1,2,3,4,5]
rotate(list_test)