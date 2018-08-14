a = 1
b = 3.14
c = 22/7
d = 'Anil Kumar A'
e = "Anil A Kumar"
f = (1, a, b, c, d, 'abcd', "dcba")
g = [a, b, c, d, e, f, 'a']
h = {'a', 'b', 'c', 'd'}
i = {'raja':'Manager', 'anil':'Test Engineer 3', 'anil kumar a':'QA Engineer'}

print("\n\n================>Data Types")
print("\tdata type of \"a\" is:", type(a), 'Value is', a)
print("\tdata type of 'b' is:", type(b), 'Value is', b)
print("\tdata type of 'c' is:", type(c), 'Value is', c)
print("\tdata type of 'd' is:", type(d), 'Value is', d)
print("\tdata type of \"e\" is:", type(e), 'Value is', e)
print("\tdata type of \"f\" is:", type(f), 'Value is', f)
print("\tdata type of \"g\" is:", type(g), 'Value is', g)
print("\tdata type of 'h' is:", type(h), 'Value is', h)
print('\tdata type of "i" is:', type(i), 'Value is', i)

print("\n\n================>Some operations")
print("\ta+b = ", a+b)
print("\ta/b = ", a/b)
print("\t3rd characted of string 'd' is: ", d[2])
print("\tYou can check for a substring, check 'mar' in string 'e'", e.find('mar'))

print("\n\n================>Immutable Variables")

i_a = 20
i_b = 'Hello'
i_c = (1, 2, 3, 4)

print("\tdata type of 'i_a' is:", type(i_a), 'Value is', i_a, 'And it\'s current id is: ', id(i_a))
print("\tdata type of 'i_b' is:", type(i_b), 'Value is', i_b, 'And it\'s current id is: ', id(i_b))
print("\tdata type of 'i_c' is:", type(i_c), 'Value is', i_c, 'And it\'s current id is: ', id(i_c))

print("\tNow I am trying to modify above variables")
i_a = i_a + 10
print("\tdata type of 'i_a' is:", type(i_a), 'Value is', i_a, 'And it\'s current id is: ', id(i_a))
i_b = i_b + ' is a good guy'
print("\tdata type of 'i_b' is:", type(i_b), 'Value is', i_b, 'And it\'s current id is: ', id(i_b))

print("\n\n================>Mutable Variables")
m_a = [1, 2, 3, 4]
m_b = {'water':'bottle', 'rice':'plate', 'mobile':'pocket'}

print("\tdata type of 'm_a' is:", type(m_a), 'Value is', m_a, 'And it\'s current id is: ', id(m_a))
print("\tdata type of 'm_b' is:", type(m_b), 'Value is', m_b, 'And it\'s current id is: ', id(m_b))

m_a.append('ajajajaja')
m_b.pop('rice')

print("\tdata type of 'm_a' is:", type(m_a), 'Value is', m_a, 'And it\'s current id is: ', id(m_a))
print("\tdata type of 'm_b' is:", type(m_b), 'Value is', m_b, 'And it\'s current id is: ', id(m_b))


print("\t=======> SETs")
s_a = {'a', 'b', 'c', 'd'}
s_b = {'c', 'd', 'e', 'f'}
print("\t set 's_a' is: ", s_a)
print("\t set 's_b' is: ", s_b)
print("\tUNION = ", s_a.union(s_b))
print("\tINTERSECTION = ", s_a.intersection(s_b))

print("\t=======> Dictionaries")
dict_a = {'one':'ek', 'two':'dho', 'three':'theen', 'tmp_list':[1, 2, 3, 4], 'tmp_tuple':(1, 2, 3, 4), 'tmp_set':{1, 2, 3, 4}, 'tmp_dict':{1:'one', 2:'two', 3:'three'}}
print('\tDictionary: "dict_a" is:', dict_a)
print('\t dict_a["three"]',dict_a["three"])
print('\t if you want ti find a key value of a key of a dictionary "dict_a[\'tmp_dict\'][1]"', dict_a['tmp_dict'][1])

