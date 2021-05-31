


def convertString(str1, str2, l1, l2):

	if l1 == 0:
		return l2

	if l2 == 0:
		return l1

	if str1[l1-1] == str2[l2-1]:
		return convertString(str1, str2, l1-1, l2-1)

	return 1 + min(convertString(str1, str2, l1, l2-1), # Insert
				convertString(str1, str2, l1-1, l2), # Remove
				convertString(str1, str2, l1-1, l2-1)) # Replace

str1 = "Anshuman"
str2 = "Antihuman"
res=convertString(str1, str2, len(str1), len(str2))
print(res)
