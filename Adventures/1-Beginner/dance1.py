#ask user to input a string from console to insert a entry into dictionary, each string are , delimtered. key is the combination of the two strings with _ as separator, value is the third string
#repeat the process until user input a empty string
#after user input all the strings, print out the dictionary

dance = {}
while True:
    entry = input('Enter a string to insert into the dictionary (key1,key2,value): ')
    if entry == '':
        break
    key1, key2, value = entry.split(',')
    dance[key1 + '_' + key2] = value

dance1_sequence = [];
dance2_sequence = [];
while True:
    dance1 = input('Enter the first dance sequence: ')
    if dance1 == '':
        break
    dance1_sequence.append(dance1)

# ask user to input the second dance sequence
while True:
    dance2 = input('Enter the second dance sequence: ')
    if dance2 == '':
        break
    dance2_sequence.append(dance2)

# calculate the forest status based on dance1_sequence and dance2_sequence, each dance will affect the forest status
forest_status_changes = [dance[d1 + '_' + d2] for d1, d2 in zip(dance1_sequence, dance2_sequence)]
# print out the forest status changes
for d1, d2, status in zip(dance1_sequence, dance2_sequence, forest_status_changes):
    print(f'Dance 1: {d1}, Dance 2: {d2}, Forest Status: {status}')




