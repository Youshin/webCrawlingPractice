# infile = open('FirstPresidents.txt', 'r')

# for line in infile:
#     print(line, end='')
# infile.close()

# infile2 = open('FirstPresidents.txt', 'r')
# print([line.rstrip() for line in infile2])
# infile2.close()

infile1 = open('USPres.txt','r')
infile2 = open('Vpres.txt', 'r')

pset = { name for name in infile1 }
vset = { name for name in infile2 }

data = pset.intersection(vset)
outfile = open('PV.txt', 'w')
outfile.writelines(data)

infile1.close()
infile2.close()
outfile.close()