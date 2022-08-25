import sys

if __name__ == '__main__' :

    L=sys.argv
    print(L)
    AlgoName = 'Linear regression' # -a
    FileName = 'Irish'             # -f
    FoldNum = '1'                  # -n
    classLevel = 'y'               # -c
    realval = '0.0001'             # -l
    for i in range(len(L)): 
        if L[i] == '-a':
            AlgoName = L[i+1]
        elif L[i]=='-f':
            FileName = L[i+1]
        elif L[i]=='-n':
            FoldNum = L[i+1]
        elif L[i]=='-c':
            classLevel = L[i+1]
        elif L[i]=='-l':
            realval = L[i+1]
    
    print("The modle is " +AlgoName+ " with dataset " +FileName+ " where number of folder " +FoldNum+ " with target attribute " +classLevel+ " and learning rate "+realval+".Thank you for inputing.")