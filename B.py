import subprocess
import sys


def send_command(receiver, command):
    receiver.stdin.write(command)
    receiver.stdin.flush()  # ensure data is sent immediately


def close_gracefully(process, exit_code):
    process.stdin.close()
    process.stdout.close()
    process.terminate()
    process.wait()  # ensure process is terminated
    sys.exit(exit_code)


if len(sys.argv) < 2:
    print('Expected the path to program A as an argument')
    sys.exit(1)

# Start A which path is passed as a B arg:
A = subprocess.Popen(
    ["python3", sys.argv[1]],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

send_command(A, 'Hi\n')

hi_response = A.stdout.readline().strip()

if hi_response != 'Hi':
    print('A responded with', hi_response, 'instead of Hi')
    close_gracefully(A, 1)

random_nums = []

for i in range(100):
    send_command(A, 'GetRandom\n')
    int_response = A.stdout.readline().strip()

    try:
        random_nums.append(int(int_response))
    except ValueError:
        print('A responsed with', int_response, ' when asked for a random int')
        close_gracefully(A, 1)
        

send_command(A, 'Shutdown\n')

sorted_nums = sorted(random_nums)
print(sorted_nums)
print((sorted_nums[49] + sorted_nums[50]) / 2)  # median
print(sum(sorted_nums) / 100)  # average

close_gracefully(A, 0)
