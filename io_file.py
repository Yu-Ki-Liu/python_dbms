__author__ = 'yuki'

def write_file():
    #open a file
    fo = open("user.txt","ab")
    fo.write("dddYuki main\n")
    # Close opend file
    fo.close()

def read_file():
     # Open a file
    fo = open("user.txt", "r")
    str = fo.readline();
    #print "Read String is : ", str
    # Close opend file
    fo.close()
    return str