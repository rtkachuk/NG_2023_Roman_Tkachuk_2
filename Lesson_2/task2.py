from utils import drawLine

str = "Hello world"
lst = [ "Friend", 1, False, "KEK", 42, True, "pomidorchiki", -256, True ]

for element in lst:
    print (element)

drawLine()
print ("First element: {}".format(lst[0]))
print ("Last element: {}".format(lst[-1]))
print ("Couple elements: {}".format(lst[2:4]))
print ("Up to 4th element: {}".format(lst[:4]))
drawLine()
lst[1] = "Jack"
print (lst)
lst.insert(2, "LOL")
print ("Altered list: {}".format(lst))
lst.append("CAT")
print ("List with added cat: {}".format(lst))
lst2 = [ 7, 9, -44343434, "PYTHON", "Mustdie 11"]
lst.extend(lst2)
print ("Extended list: {}".format(lst))
drawLine()
lst.remove(True)
print ("List without one True: {}".format(lst))
lst.pop(0)
print ("List without first index: {}".format(lst))
lst2.clear()
print ("Clear list: {}".format(lst2))
drawLine()

print ("Show only odd indexes: ")
index = 0
while index < len(lst):
    if index % 2 == 0:
        print (lst[index])
    index = index + 1

drawLine()
if "CAT" in lst:
    print ("There is CAT in list!")

drawLine()
nmbrs = [ 1, 9, 2, 6, 7,3, 0, -256, 13 ]
nmbrs.sort()
print ("Sorted list: {}".format(nmbrs))
nmbrs.sort(reverse=True)
print ("Sorted list: {}".format(nmbrs))
drawLine()
testList1 = [ 1, 2, 3, 4, 5 ]
testList2 = testList1.copy()
testList2[0] = "KEK"
print (testList1)