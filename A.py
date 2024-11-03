import random

running = True

while running:
    command = input()

    # flush=True ensures data is sent immediatelly:
    if command == 'Hi':
        print('Hi', flush=True)
    elif command == 'GetRandom':
        print(random.randint(0, 1000), flush=True)
    elif command == 'Shutdown':
        running = False
