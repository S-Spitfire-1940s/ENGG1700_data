import ENGG1700_DataActions as DataActions
"""'/Users/nakiajunior/Downloads/CollatedData.csv'"""

def main():
    steel = DataActions.Array(0)
    aluminium = DataActions.Array(1)
    acrylic = DataActions.Array(2)


    DataActions.data('/Users/nakiajunior/Downloads/CollatedData.csv', steel, aluminium, acrylic)
    steel.remove_blanks()

    steel.scatter()
main()