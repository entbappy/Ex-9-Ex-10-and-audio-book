#Ex - 10 pickling iris
# use pickle and requests module
import pickle

f = open("iris.data","r")
lis = f.read().split("\n")
# a = len(lis)
# print(a)
print(type(lis))
lis2 = [item.split(",") for item in lis if len(item)!=0]
# print(lis2)
f.close()

# file_name = "iris.pkl"
# file = open(file_name,"wb")
# store = pickle.dump(lis2,file)
# file.close()

#Depickling
file_name = "iris.pkl"
file = open(file_name,"rb")
retrieve = pickle.load(file)
print(retrieve)
file.close()






