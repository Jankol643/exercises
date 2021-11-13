#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-2d-arrays
# Difficulty: Easy

def max_hour_glasses(matrix) :
    def get_hourglass_sum(matrix,row,col):
        hg_sum = 0
        hg_sum = hg_sum + matrix[row-1][col-1]  #current sum + top left element
        hg_sum = hg_sum + matrix[row-1][col]    #current sum + element above the matrix[i,j]
        hg_sum = hg_sum + matrix[row-1][col+1]  #current sum + top right element
        hg_sum = hg_sum + matrix[row][col]      #current sum + middle element of hg/matrix[i,j]
        hg_sum = hg_sum + matrix[row+1][col-1]  #current sum + bottom left element of hg
        hg_sum = hg_sum + matrix[row+1][col]    #current sum + element below the matrix[i,j]
        hg_sum = hg_sum + matrix[row+1][col+1]  #current sum + bottom right element
        return hg_sum

    max_hourglass_sum = -63 # minimum value of an element a
    #looping through the 2d matrix
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            current_hourglass_sum = get_hourglass_sum(matrix, i, j)
            #find highest hourglass sum
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    return max_hourglass_sum

if __name__ == '__main__':
    matrix = list()

    for _ in range(6):
        row = input().strip().split(' ')
        row = list(map(int, row))
        matrix.append(row)
    res = max_hour_glasses(matrix)
    print(res)
