import sys
import urllib.parse

def main():
    if len(sys.argv) < 2:
        print("Usage: python encode_tool.py '<string>'")
        sys.exit(1)

    string = sys.argv[1]
    encoded_string = urllib.parse.quote(string, safe='')
    decoded_string = urllib.parse.unquote(string)

    print("Encoded string:", encoded_string)
    print("Decoded string:", decoded_string)

if __name__ == "__main__":
    main()
