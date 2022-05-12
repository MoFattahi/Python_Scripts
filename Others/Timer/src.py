# Create a countdown timer

import time


def cd_timer():
    # get the user input
    input_time = int(input("Enter the time in seconds: "))
    if input_time > 0:
        while input_time:
            mins, secs = divmod(input_time, 60)
            print(' Timer: {:02d}:{:02d}'.format(mins, secs), end="\r")
            time.sleep(1)  # Delay Execution
            input_time -= 1
        print("\nFinished!\nTimer Completed.")

    elif input_time == 0:
        print("\nFinished!\nTimer Completed.")
    else:
        print("Input is not valid.\nTry Again.")
        cd_timer()


# Call the function
cd_timer()
