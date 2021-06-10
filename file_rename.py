import os

file_path  = """C:/Users/rnwld/Desktop/교회서식150가지"""
file_names = os.listdir(file_path)
print(file_names)

d = dict()
f = open("""C:/Users/rnwld/Desktop/교회서식150가지/1-0list자료목록표.txt""")

lines = f.readlines()
print(lines)

for line in lines:
    no = line.split()
    title = " ".join(no[1:])
    d[no[0]+".HWP"] = title


print(d.keys())

for name in file_names:
    src = os.path.join(file_path, name)
    if name in d.keys():
        dst = name[:-4] + " - " + d[name] + ".HWP"
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)


#
# for name in file_names:
#     src = os.path.join(file_path, name)
#     dst = str(i) + '.jpg'
#     dst = os.path.join(file_path, dst)
#     os.rename(src, dst)