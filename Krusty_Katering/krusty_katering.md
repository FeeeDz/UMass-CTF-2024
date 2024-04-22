# Krusty Katering
### Description
Krusty Katering is hemorrhaging money, and Mr. Krabs has brought you in to fix it. You have 10 line cooks, and while they're okay at making Krabby patties, they can't agree on who cooks what and when. To make matters worse, Squidward (trying to keep his job) refuses to give you the list of orders, and will only tell you them one by one. Each time Squidward tells you a job, you get to add it to a cook's schedule for the day. Cooks cannot trade jobs, once it's on the schedule, it stays there. You want to ensure the last order finishes as soon as possible so that Mr. Krabs can close and count his profits. The competing Plankton's Provisions assigns their jobs randomly. So long as your crew is 20% more efficient than Team Chum Bucket every day this week, you're hired. Can you save Mr. Krabs' business?

### Solution
The objective of this challenge is to manage a team of 10 line cooks in a restaurant setting to complete orders as efficiently as possible. The challenge is to assign each order to a cook in a way that minimizes the total time to complete all orders, with the goal of beating a competing restaurant's time by 10% each day.

```python
from pwn import *

def parse_time(time_str):
    minutes = seconds = 0
    if 'm' in time_str:
        parts = time_str.split('m')
        minutes = int(parts[0])
        if 's' in parts[1]:
            seconds = int(parts[1].split('s')[0])
    elif 's' in time_str:
        seconds = int(time_str.split('s')[0])
    return minutes * 60 + seconds

def find_min_cook(cooks):
    min_time = min(cooks)
    return cooks.index(min_time)

def main():
    io = remote("krusty-katering.ctf.umasscybersec.org", 1337)
    cooks = [0] * 10  # Initialize all cook times to 0

    while True:
        try:
            r = io.recv(2048).decode()
            print(r)
            print(cooks)

            if "Your Time" in r:
                cooks = [0] * 10  # Reset all cook times

            if "Estimated time to cook:" in r:
                time_str = r.split("Estimated time to cook: ")[1].split("\n")[0]
                secs = parse_time(time_str)
                min_id = find_min_cook(cooks)
                cooks[min_id] += secs
                io.sendline(str(min_id + 1).encode())  # Send only if we have a valid min_id

        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()

# UMASS{subst@nd@rd_c00k}
```
