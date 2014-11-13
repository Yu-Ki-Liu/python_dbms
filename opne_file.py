__author__ = 'chaucer'

def open_file():
    #open a file
    fo = open("user.txt","wb")
    print "Name of the file: ", fo.name
    print "Closed or not : ", fo.closed
    print "Opening mode : ", fo.mode
    print "Softspace flag : ", fo.softspace