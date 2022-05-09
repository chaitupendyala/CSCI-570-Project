#Imports
from re import S
import time
import psutil


#Declarations
Gap_Penalty   = 30

def mis_alignment_cost( str1, str2 ):
    str = 'ACGT'
    str1_index = str.index(str1)
    str2_index = str.index(str2)
    Mis_Aligmnent_Cost = [[0  ,  110, 48 , 94 ],
                          [110,  0  , 118, 48 ],
                          [48 ,  118, 0  , 110],
                          [94 ,  48 , 110, 0  ]]
    return Mis_Aligmnent_Cost[str1_index][str2_index]


# Functions required to compute the algnment
def Alignment( A, B ):
    Length_of_A = len(A)
    Length_of_B = len(B)
    Alignment_Costs = [[0 for column in range(Length_of_B + 1)] for row in range(Length_of_A + 1)]
    
    for i in range(Length_of_A+1):
        Alignment_Costs[i][0] = Gap_Penalty*i
        
    for j in range(Length_of_B+1):
        Alignment_Costs[0][j] = Gap_Penalty*j
    
    for i in range(1,Length_of_A+1):
        for j in range(1,Length_of_B+1):
            if A[i-1] == B[j-1]:
                Alignment_Costs[i][j] = min( Alignment_Costs[i-1][j-1],
                                             Alignment_Costs[i-1][j] + Gap_Penalty,
                                             Alignment_Costs[i][j-1] + Gap_Penalty)
                #Alignment_Costs[i][j] = Alignment_Costs[i-1][j-1]
            else:
                Alignment_Costs[i][j] = min( Alignment_Costs[i-1][j-1] + mis_alignment_cost( A[i-1], B[j-1] ),
                                             Alignment_Costs[i-1][j] + Gap_Penalty,
                                             Alignment_Costs[i][j-1] + Gap_Penalty)
    
    return Alignment_Costs


# Finding the alignment between the two strings
def Find_Alignment(Alignment_Costs, A, B):
    Length_of_A = len(A)
    Length_of_B = len(B)
    
    path = [ [0 for column in range( Length_of_B+1 )] for row in range( Length_of_A + 1 ) ]
    path[Length_of_A][Length_of_B] = 1
    path[0][0] = 1
    
    i = Length_of_A
    j = Length_of_B
    while i != 0 or j != 0:
        if Alignment_Costs[i][j] == Alignment_Costs[i-1][j] + Gap_Penalty:
            path[i-1][j] = 1
            i -= 1
        elif Alignment_Costs[i][j] == Alignment_Costs[i][j-1] + Gap_Penalty:
            path[i][j-1] = 1
            j -= 1
        else:
            path[i-1][j-1] = 1
            i -= 1
            j -= 1
    
    A_Final_String = B_Final_String = ''
    i = j = 0
    
    while i != Length_of_A or j != Length_of_B:
        if i != Length_of_A and path[i+1][j] == 1:
            A_Final_String += A[i]
            B_Final_String += '-'
            i += 1
        elif j != Length_of_B and path[i][j+1] == 1:
            A_Final_String += '-'
            B_Final_String += B[j]
            j += 1
        else:
            A_Final_String += A[i]
            B_Final_String += B[j]
            i += 1
            j += 1
    print( A_Final_String )
    print( B_Final_String )
    wf = [str(Alignment_Costs[Length_of_A][Length_of_B]), A_Final_String, B_Final_String]
    return wf

# Checking the running time and memory usage
def call_inefficient_sequence_alignment( s1, s2, output_file ):
    start = time.time()
    process = psutil.Process()
    memory_info = process.memory_info()

    Alignment_Costs = Alignment(s1, s2)
    wf = Find_Alignment(Alignment_Costs, s1, s2)
    end = time.time()
    run_time = end - start
    memory_consumed = int(memory_info.rss/1024)

    wf.append(str(run_time*1000))
    wf.append(str(memory_consumed))
    print("M+N: " + str( len(s1) + len(s2) ))
    f = open("./outputs/inefficient/" + output_file, 'w')
    f.write('\n'.join(wf))
    f.close()