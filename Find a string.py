def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            counter += 1
    return counter
if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count