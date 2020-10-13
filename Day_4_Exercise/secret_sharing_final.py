from sympy import nextprime
import random
privkey = 0x1062f7a3410b4a29fa7435c57c14d521eb8169875f280e1bf2bc39f172514059
nextPrime = nextprime(privkey,ith=1)

#Private Key.
print("Private key: {}\n".format(hex(privkey)))

# General Equation for creating points.
key = []
rand = []
def calculate_point(k): 
    for i in range(k-1):
        rand.append(random.randrange(0,nextPrime))

    for j in range(k):
        x = privkey
        for i in range(k-1):
            r1 = rand[i]
            x += r1 * pow(j+1,i+1)
        x = x % nextPrime
        key.append(x)



#Input number of points.
point = input("Input K: ")
calculate_point(point)

#print points.
print("Points:")
for i in range(point):
    x = key[i]
    print("({0},{1})\n".format(i+1,hex(x)))

#Reconstruction.
def verify_points(key):
    verify = 0
    for i in range(len(key)):
        l = 1
        for j in range(len(key)):
            if j != i:
                l = (l * ((j+1)/float((j+1)-(i+1))))
        verify += key[i]*int(l)
    verify = verify % nextPrime
    return verify

#Verify.
print("Verify: {}".format(hex(verify_points(key))))




