'''A module to train exceptions'''

def convert(s):
    '''Convert to integer'''
    try:
        x = int(s)
        print("conversion successful!")
    except ValueError:
        x=-1
        print("conversion failed!")
    finally:
        print("this is some final text")
    return x