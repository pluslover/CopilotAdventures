''' write a util function to calulate two times difference in minutes, the time is in format of HH:MM '''
''' example: time_diff('12:30', '13:30') = -60 '''
''' example: time_diff('12:30', '12:15') = 15 '''
def time_diff(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    return (h2 - h1) * 60 + m2 - m1

''' compose a main function to test the util function '''
def main():
    centralTime = '12:00';

    timeDiffs = [];
    townTimes = ['11:00', '12:00', '13:00', '14:00', '15:00'];
    
    for townTime in townTimes:
        timeDiffs.append(time_diff(centralTime, townTime));

    ''' print out the time differences includes both central time and town time '''
    for i in range(len(townTimes)):
        print('Central Time: ' + centralTime + ', Town Time: ' + townTimes[i] + ', Time Difference: ' + str(timeDiffs[i]));

''' run main function '''
if __name__ == '__main__':
    main();