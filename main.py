import fileinput


def convert(element: str) -> str:
    conversions = {
        "1": "chr1",
        "2": "chr2",
        "3": "chr3",
        "4": "chr4",
        "5": "chr5",
        "6": "chr6",
        "7": "chr7",
        "8": "chr8",
        "9": "chr9",
        "10": "chr10",
        "11": "chr11",
        "12": "chr12",
        "13": "chr13",
        "14": "chr14",
        "15": "chr15",
        "16": "chr16",
        "17": "chr17",
        "18": "chr18",
        "19": "chr19",
        "20": "chr20",
        "21": "chr21",
        "22": "chr22",
        "X": "chrX",
        "Y": "chrY"
    }
    return conversions[element]


if __name__ == '__main__':
    for line in fileinput.input():
        line = line.rstrip('\n')
        if line.startswith("#"):
            print(line)
            continue
        elements = line.split("\t")
        elements[0] = convert(elements[0])
        print("\t".join(elements))
