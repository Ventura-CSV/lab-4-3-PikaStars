def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0

    ########################################
    # Do not delete the return statement
    ########################################
    i = 0
    while i < 5:
        num = int(input("Enter your input:"))
        total += num
        i += 1
    print (total)
    return total


if __name__ == '__main__':
    main()
