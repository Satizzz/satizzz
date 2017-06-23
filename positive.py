#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      test108
#
# Created:     20-06-2017
# Copyright:   (c) test108 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(n):
    num=n
    if(num<0):
        print("The number is negative")
    elif(num==0):
        print("The number is zero")
    else:
        print("The number is Positive")

if __name__ == '__main__':
    main(-20)
