import pickle

f = open('list.pickle', 'wb')
test = [1,2,3,4,5]
pickle.dump(test, f)
f.close()


f2 = open('list.pickle', 'rb')
for i in pickle.load(f2):
    print(i)