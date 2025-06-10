import sys
import re

# Usage: python remove_base64_from_md.py <input_file> <output_file>
def remove_base64_lines(input_path, output_path):
    base64_pattern = re.compile(r'data:image/[^\"]+')
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if not base64_pattern.search(line):
                outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_base64_from_md.py <input_file> <output_file>")
        sys.exit(1)
    remove_base64_lines(sys.argv[1], sys.argv[2])
