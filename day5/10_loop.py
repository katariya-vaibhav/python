import time

max_retries = 5
attempts = 0
wait_time = 1

while attempts < max_retries:
    print(f"attempts : {attempts + 1} , max_retries : {max_retries} , wait_time : {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
