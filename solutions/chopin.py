import sys

doubles = {"A#": "Bb", "C#": "Db", "D#": "Eb",
           "F#": "Gb", "G#": "Ab"}
reverse = dict((v, k) for k, v in doubles.items())
i = 0

for line in sys.stdin:
    note, tone = str(line).split()
    if note in doubles:
        print("Case {0}:".format(i + 1), doubles[note], tone)
    elif note in reverse:
        print("Case {0}:".format(i + 1), reverse[note], tone)
    else:
        print("Case {0}: UNIQUE".format(i + 1))
    i += 1
