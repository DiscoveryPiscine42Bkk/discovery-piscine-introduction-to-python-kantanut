import sys

def main():
    if len(sys.argv) != 3:
        print("RTFM (Read the F-ing manual)")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)
    if count == 0:
        print("RTFM (Read the F-ing manual)")
    else:
        print(count)
main()