from utils import drawLine

kek = { "apple", "apple", "apple", "banana", "notebook", 42, 42, 1, True, False, False}
print (kek)

kek.remove("apple")
print (kek)
# Will break up the code, because apple isn't in this set
#kek.remove("apple")

kek.discard("banana")
kek.discard("banana")
kek.discard("banana")
kek.discard("banana")
kek.discard("banana")
kek.discard("banana")
print (kek)