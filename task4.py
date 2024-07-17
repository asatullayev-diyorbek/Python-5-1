import time


def this_date():
    this_time = time.localtime()
    line1 = time.strftime("%A %d %B %Y %H:%M:%S", this_time)
    line2 = time.strftime("%d.%m.%Y", this_time)
    return f"Today:\n{line1}\n{line2}"


if __name__ == "__main__":
    print(this_date())
