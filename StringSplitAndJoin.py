def split_and_join(line):
    result = ""
    for i in line:
        if i == " ":
            result += "-"
        else:
            result += i
    return result


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# https://www.hackerrank.com/challenges/python-string-split-and-join/problem