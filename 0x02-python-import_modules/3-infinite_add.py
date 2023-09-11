#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    num_args = len(sys.argv)
    total = 0
    for i in range(1, num_args):
        total += int(sys.argv[i])
    print("{:d}".format(total))
