import math
import chardet
import pandas as pd


def queen_board_input():
    with open(r"H:\WPI\spring 20\AI\ASSIGNMENT 1\heavy queens board.csv", 'rb') as f:  # change path accordingly
        result = chardet.detect(f.read())  # to detect the encoding of csv file
    # change path accordingly
    df = pd.read_csv(r"H:\WPI\spring 20\AI\ASSIGNMENT 1\heavy queens board.csv", encoding=result['encoding'],error_bad_lines=False, sep=',', engine='python', header=None)
    n = len(df)
    a = [[0 for x in range(0,n)]for y in range(0,n)]
    #print(df)
    board = [[0 for x in range(0,n)] for y in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            if(math.isnan(df[i][j])==False):
                a[j][i] = int(df[i][j])


    #for x in a:
        #print(x)
    return a
