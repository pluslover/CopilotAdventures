def time_diff(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    return (h2 - h1) * 60 + m2 - m1

def main():
    central_time = '12:00'
    town_times = ['11:00', '12:00', '13:00', '14:00', '15:00']
    
    time_diffs = [time_diff(central_time, town_time) for town_time in town_times]

    for i in range(len(town_times)):
        print(f'Central Time: {central_time}, Town Time: {town_times[i]}, Time Difference: {time_diffs[i]}')

if __name__ == '__main__':
    main()