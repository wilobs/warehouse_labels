from blabel import LabelWriter


def generate_positions() -> list:
    aisles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N']
    bayes = 16
    levels = 4
    positions = ['L', 'R']
    
    bins = []
    for aisle in aisles:
        for bi, _ in enumerate(range(bayes), 1):
            for li, _ in enumerate(range(levels), 1):
                for position in positions: 
                    bins.append(f"A{aisle}_B{str(bi).zfill(2)}_L{str(li).zfill(2)}_{position}")
                    # print(f"A{aisle}_B{str(bi).zfill(2)}_L{str(li).zfill(2)}_{position}")

    return bins

def write_to_file(filename: str, iter):
    with open(filename, 'w+') as f:
        for v in iter:
            f.write(v)
            f.write('\n')

def write_to_label(iter):
    label_writer = LabelWriter("./templates/item_template.html", default_stylesheets=("./templates/style.css",))
    records = [
        dict(main_label=x) for x in iter
    ]

    label_writer.write_labels(records, target="./output/labels_output.pdf")


bins = generate_positions()
write_to_file("./output/positions_output.txt", bins)
write_to_label(bins)