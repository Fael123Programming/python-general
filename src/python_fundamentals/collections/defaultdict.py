from collections import defaultdict

"""
    A default dict does not complain of not
    having a key when it is accessed, i.e.,
    it avoids KeyError.
"""

if __name__ == "__main__":
    colors = [('1', 'blue'), ('2', 'yellow'), ('3', 'red'), ('1', 'white'), ('3', 'green'), ('2', 'purple')]
    mapped_colors = defaultdict(list)
    for key, value in colors:
        mapped_colors[key].append(value)
    print(mapped_colors)
    print(mapped_colors['1'])
