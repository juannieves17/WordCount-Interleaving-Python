'''
Created on Mar 11, 2013

@author: juanito
'''
def parallel_int(A,B):
    #If the lengths of A and B are not equal
    if not len(A) == len(B):
        if len(A) > len(B):
            biggest = len(A)
        if len(A) < len(B):
            biggest = len(B)
            
        result = []
        for i in range(0,biggest):
            #If you finish the A list, add the remaning in the B list
            if i > len(A)-1:
                for k in range(i,len(B)):
                    result.append(B[k])
                break
            #If you finish the B list, add the remaning in the A list
            elif i > len(B)-1:
                for k in range(i,len(A)):
                    result.append(A[k])
                break
            else:
                result.append(A[i])
                result.append(B[i])
    #if the lengths are equal
    else:
        biggest = len(A)
        result = []
        for i in range(0,biggest):
            result.append(A[i])
            result.append(B[i])
    return result

# A and B are the list
# temp is the string that will be printed
# m is the length of A
# n is the length of B
# i is the index for the next available in the result
# x and y are just counter to make the substrings.
#list if the final list with all the interleavings and is declared globally
filename = "interleaving.txt"
def all_intRecur(A,B,temp, m, n, i, x, y,out):
    
    if m == 0 and n == 0:
        global filename
        out.write("["+str(temp))
        
    if m != 0:
        temp[i] = A[0]
        all_intRecur(A[x+ 1:],B, temp, m -1, n, i+1,x,y,out)
        
    if n != 0:
        temp[i] = B[0]
        all_intRecur(A, B[y+ 1:], temp, m, n-1, i+1,x,y,out)

def main():    
    a = [1,2]
    b = [3,4]
    l = len(a) + len(b)
    temp = [0]* l
    output = open(filename,"r+b")
    output.write("list 1 = "+ str(a)+"\n")
    output.write("list 2 = "+ str(b)+"\n")
    output.write("Parallel Interleaving\n")
    output.write("Result = "+ str(parallel_int(a, b))+"\n")
    
    output.write("\nAll Interleaving\n")
    all_intRecur(a,b,temp, len(a), len(b), 0,0,0,output)
    output.write("]")
    output.close()
    print "Done"


if __name__ == '__main__':
    main()