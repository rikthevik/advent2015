

import re

def main(inputpath):
    total_diff = 0
    for l in ( _l.strip() for _l in open(inputpath, "r") ):
        code_count = len(l)
        content = l[1:-1]
        content, _ = re.subn(r'\\x[a-f0-9][a-f0-9]', '!', content)
        content = content.replace(r'\\', '@')
        content = content.replace(r'\"', '#')
        mem_count = len(content)
        print l, code_count, mem_count, (code_count - mem_count)
        total_diff += (code_count - mem_count)
    print total_diff

main("input07.test.txt")
main("input07.real.txt")