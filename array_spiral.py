https://www.codingninjas.com/studio/problems/print-spiral_547
from sys import stdin

def spiralPrint(mat, nRows, mCols):
    r=nRows
    c=mCols
    i,j=0,0
    count=0
    x,y=0,1
    if len(mat)==0:
        return
    else:    
        while True:
            while j < mCols-1:
                print(mat[i][j],end=' ')
                j += 1
                count += 1
            while i < nRows-1:
                print(mat[i][j],end=' ')
                i += 1
                count += 1

            if count == (r*c)-1:
                print(mat[i][j],end=' ')
                break

            nRows -= 1
            mCols -= 1
            
            while j > x:
                print(mat[i][j],end=' ')
                j -= 1
                count += 1
            x += 1

            while i > y:
                print(mat[i][j],end=' ')
                i -= 1
                count += 1
            y += 1