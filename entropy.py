import re
import sys
readStream = open("/home/jung/ransomware/png_entropy.txt")
writeStream = open("/home/jung/ransomware/NVMalloc.pdf")

#readStream = open(sys.argv[1])
r = readStream.read()
w = writeStream.read()

r = re.split("['\n']",r)
w = re.split("['\n']",w)

r_len = len(r)
w_len = len(w)
def preprocess(data):
    leng = len(data)
    for i in range(leng-1):
        data[i] = int(float(data[i].split()[2]))
    return data
	
r = preprocess(r)
w = preprocess(w)

def calEntropy(data):
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(x))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

	
for c in r :
    print(chr(c))

print(calEntropy(r),calEntropy(w))


