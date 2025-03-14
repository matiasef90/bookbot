from stats import get_report
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

get_report(sys.argv[1])

    