from utils import drawLine

tpl = ( 1, "TEST", True, 42)
print ("Tuple: {}".format(tpl))

lst = list(tpl)
lst.append("DALADNO")
tpl = tuple(lst)
print ("Tuple: {}".format(tpl))

drawLine()
OSes = ( "GNU/Linux", "FreeBSD", "Unix", "Solaris", "MacOS")
(linux, bsd, nix, sun, apple) = OSes
print ("Linux OS: " + linux)