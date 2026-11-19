try:
    log_handle = open("log.txt", "r")
    line_cnt = 0
    word_cnt = 0
    char_cnt = 0
    warn_cnt = 0
    err_cnt = 0

    print("Log File Contents:\n")
    for entry in log_handle:
        print(entry, end="")
        line_cnt += 1
        word_cnt += len(entry.split())
        char_cnt += len(entry.strip("\n"))
        if "WARNING" in entry.upper() or "WARN" in entry.upper():
            warn_cnt += 1
        if "ERROR" in entry.upper() or "CRITICAL" in entry.upper():
            err_cnt += 1

    log_handle.close()

    print("\n\nLog Summary:")
    print("Total Lines:", line_cnt)
    print("Total Words:", word_cnt)
    print("Total Characters:", char_cnt)
    print("Total Warnings:", warn_cnt)
    print("Total Errors:", err_cnt)
except FileNotFoundError:
    print("Error: log.txt file does not exist.")
