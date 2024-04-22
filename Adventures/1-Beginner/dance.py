'''define a lookup function that takes two strings as input and returns a string as output'''
'''each string must be one of `Twirl`, `Leap`, or `Spin` '''
'''the two strings need to be combined to form a new string uses _ as separator'''
'''use the new string as an key to lookup a value from a dictionary'''
'''the dictionary contains all the combinations of the two strings and their corresponding values and defines as below'''

'''return the value from the dictionary'''




def lookup(s1, s2):
    lookupTable = {
        'Twirl_Leap': 'Dance',
        'Twirl_Spin': 'Jump',
        'Twirl_Twirl': 'Skip',
        'Leap_Twirl': 'Skip',
        'Leap_Spin': 'Walk',
        'Leap_Leap': 'Run',
        'Spin_Twirl': 'Run',
        'Spin_Leap': 'Hop',
        'Spin_Spin': 'Walk'
    }
    return lookupTable[s1 + '_' + s2]

def main():
    lox_dance = ['Twirl', 'Leap', 'Spin', 'Twirl', 'Leap']
    faelis_dance = ['Spin', 'Twirl', 'Leap', 'Leap', 'Spin']
    forest_status_changes = []

    # calculate the forest status based on lox_dance and faelis_dance, each dance will affect the forest status
    forest_status_changes = [lookup(lox, faelis) for lox, faelis in zip(lox_dance, faelis_dance)]

    # print out the forest status changes
    for lox, faelis, status in zip(lox_dance, faelis_dance, forest_status_changes):
        print(f'Lox Dance: {lox}, Faelis Dance: {faelis}, Forest Status: {status}')

if __name__ == '__main__':  
    main()

        
        