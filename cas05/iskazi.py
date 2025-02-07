a = (3==4) and (5>7) and (9>8) # (False) i (False) i (True) --> False
b = (3==8) or (3==3) # (False) ili (True) --> True
c = (4<5) or (7==7) or (3+3 == 6) # (True) ili (True) ili (True) --> True
d = not (3==3) # not (True) ---> False
e = not (4==5) # not (False) --> True

# a netacno, b,c tacni, d netacno, e tacno
"""print(a)
print(b)
print(c)
print(d)
print(e)
"""

# najveci prioritet ima not, pa and, pa or
# prioritet nam govori sta se prvo racuna
# prvo se racuna not, pa and pa or

f = (8==6) and (7==5) or (2==2) and (9!=9)
# (8==6) and (7==5) ---> False and False = False
# (2==2) and (9!=9) ---> True and False = False
# False or False ---> False
# f = FALSE

"""
f = (8==6) and ((7==5) or (2==2)) and (9!=9) or ima veci prioritet od and?
f = ((8==6) and (7==5)) or ((2==2) and (9!=9)) and ima veci prioritet od or?
f = (((8==6) and (7==5)) or (2==2)) and (9!=9) da li and i or imaju isti prioritet?
"""
g = not (3==4) or (5==7)
"""
prvo se racuna not 
not (3==4) = not (False) = True
g = True or (5==7) = True or False = True
"""
h = not (2==4) and (3!=4) and not (5==6)
"""
not (2==4) = not (False) = True
not (5==6) = not (False) = True
h = True and (3!=4) and True = True and True and True = True
"""
i = (7<8) and not (4==5) or (8==9) or not (4==5) and (8!=10)
"""
not (4==5) = not (False) = True
i = (7<8) and True or (8==9) or True and (8!=10)
sledece racunamo and
(7<8) and True  = True and True = True
True and (8!=10) = True and True = True
i = True or (8==9) or True = True
"""
# false, true, true, true
print(f)
print(g)
print(h)
print(i)
