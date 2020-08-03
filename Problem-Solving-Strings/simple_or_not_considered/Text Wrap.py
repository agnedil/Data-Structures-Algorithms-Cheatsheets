import textwrap

l = input()
w = int(input())
print(*textwrap.wrap(l, w), sep="\n")
# OR
def wrap(string, max_width):
    return textwrap.fill(string, max_width)
