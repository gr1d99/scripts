from collections import defaultdict

"""
defaultdict is a dictionary like object which provides all methods provided by dictionary.
Using list as the default_factory, it is easy to group a sequence of key-value pairs 
into a dictionary of lists.
"""

some_list = [('lenovo', 1), ('hp', 2), ('mac', 3), ('lenovo', 4), ('mac', 10)]
d = defaultdict(list)
for k, v in some_list:
    d[k].append(v)

print(d.items())

"""
When each key is encountered for the first time, it is not already in the mapping; 
so an entry is automatically created using the default_factory function which returns an empty list. 
The list.append() operation then attaches the value to the new list. 
When keys are encountered again, the look-up proceeds normally (returning the list for that key) 
and the list.append() operation adds another value to the list. 
This technique is simpler and faster than an equivalent technique using dict.setdefault()
"""
