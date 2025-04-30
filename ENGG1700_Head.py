import ENGG1700_DataActions as DataActions
"""'/Users/nakiajunior/Downloads/CollatedData.csv'"""

def main():
    steel = DataActions.Array(0)
    aluminium = DataActions.Array(1)
    acrylic = DataActions.Array(2)


    DataActions.data('/Users/nakiajunior/Downloads/CollatedData.csv', steel, aluminium, acrylic)
    steel.remove_blanks()
    aluminium.remove_blanks()
    acrylic.remove_blanks()
    print(steel.return_values()[0])


main()