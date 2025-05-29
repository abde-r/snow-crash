import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <string>")
        sys.exit(1)

    s = sys.argv[1]
    decoded = ''.join(
        chr((ord(c) - i) & 0xFF)
        for i, c in enumerate(s)
    )
    print(decoded)

if __name__ == "__main__":
    main()
