#!/usr/bin/env python3

import glob
import re
import os


def read_points(file):
    if os.path.isfile(file):
        with open(file, "r") as f:
            s = re.search(r"Total score: ?(\d+)", f.read(), re.IGNORECASE)
            return int(s.group(1)) if s else 0
    return 0


if __name__ == '__main__':
    results = glob.glob("**/*.out*", recursive=True)
    filename = re.compile("(.*)(\.out)_[12]+")
    tasks = map(lambda f: filename.search(f).group(1), filter(filename.match, results))
    points = map(lambda f: (read_points(f + ".out_1") + read_points(f + ".out_2")) / (2 if os.path.isfile(f + ".out_2")
                                                                                          else 1), tasks)

    print(str(sum(points)) + " / 500")
