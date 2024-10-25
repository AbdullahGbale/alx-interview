#!/usr/bin/python3
'''
A script that reads inputs line by line and computes the stats.
'''
import sys


def main():
    """
    The main
    """
    total_file_size = 0
    status_code_count = ["200", "301", "400", "401", "403", "404", "405", "500"]
    line_count = 0
    stats = {k: 0 for k in status_code_count}

    def print_stats():
        """
        Print the aggregated statistics
        """
        print("File size: {:d}".format(total_file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
             line_count += 1
             data = line.split()
             try:
                # Assuming the status code is the second-to-last element
                sc = data[-2]
                if sc in stats:
                    stats[sc] += 1
            except (IndexError, KeyError):
                pass
            try:
                # Assuming the file size is the last element
                total_file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stats()

        print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise


if __name__ == "__main__":
    main()
