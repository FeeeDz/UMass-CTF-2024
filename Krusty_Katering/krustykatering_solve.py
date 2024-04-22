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
