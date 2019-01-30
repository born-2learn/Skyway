
def read():

    try:
        f1 =open('resort_details.txt' ,'r+')
        f=f1.read( )

    except IOError:
        f='Loading  Text...'
    return f
