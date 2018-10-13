import time
from datetime import datetime as dt

# hosts path for mac & linux
hosts_path = "hosts"
hosts_path = '/etc/hosts'
redirect = '127.0.0.1'
blocked_websites = ["www.facebook.com", "www.idnes.cz", "www.9gag.com"]

while True:
    # compare current computer time to hours specified by user
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 20):
        print('Working hours...')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                #check if website is already writen in host file
                if website in content:
                    pass
                #if not write it in specified format
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            #file.seek(0) puts pointer 0 characters from absolute document start
            file.seek(0)
            #iterate through every line of read content
            for line in content:
                # if line doesn't have any value from blocked_websites write that line
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            #file.truncate() deletes remaining content of the file
            file.truncate() 

        print('Fun hours...')
    #time.sleep(seconds) pauses python program for specified durations in seconds
    time.sleep(2)