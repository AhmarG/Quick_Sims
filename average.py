__author__ = 'Ahmar Gordon'

print('\n       Welcome to TEST AVERAGE SIMULATOR')
averages = []
print('\nEnter your test grades (0-100)\n\t\t~negative numbers quit input stream~')
while True:
    score = input('> ')
    try:
        score = int(score)
    except ValueError:
        print('\nGive me a number. Try again.')
        continue
    if score in range(0, 101):
        averages.append(score)
    else:
        break

if not averages:
    print('No average to compute')
else:
    print(averages)
    print("The test average is " + str(sum(averages)/len(averages)))
