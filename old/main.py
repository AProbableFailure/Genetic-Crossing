from worm import *


def main():
    dad = Worm(3, True)
    dad.add_genes(0, ["dlg-1"]).add_genes(2, ["him-5", "him-5"])
    mom = Worm(3)
    mom.add_genes(1, ["cdc-42", "cdc-42"])

    print(cross(mom, dad))


if __name__ == "__main__":
    main()