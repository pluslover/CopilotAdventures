# Ask the user to input a string from the console to insert an entry into the dictionary.
# Each string is delimited by commas. The key is the combination of the first two strings with '_' as the separator, and the value is the third string.
# Repeat the process until the user inputs an empty string.
# After the user inputs all the strings, print out the dictionary.

dance = {}

while True:
    entry = input('Enter a string to insert into the dictionary (key1,key2,value): ')
    if entry == '':
        break
    key1, key2, value = entry.split(',')
    dance[key1 + '_' + key2] = value

dance1_sequence = input('Enter the first dance sequence: ').split(',')
dance2_sequence = input('Enter the second dance sequence: ').split(',')

# Calculate the forest status based on dance1_sequence and dance2_sequence.
# Each dance will affect the forest status.

forest_status_changes = [dance[d1 + '_' + d2] for d1, d2 in zip(dance1_sequence, dance2_sequence)]

# Print out the forest status changes.

for d1, d2, status in zip(dance1_sequence, dance2_sequence, forest_status_changes):
    print(f'Dance 1: {d1}, Dance 2: {d2}, Forest Status: {status}')



