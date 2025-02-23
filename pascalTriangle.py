



'''
 assumes numRows >= 1
'''
def generateTriangleRows(numRows: int):
    rows = [[1]]

    if numRows == 1:
        return rows

    for i in range(1, numRows):
        prevRow = rows[i - 1]
        row = [1]

        for j in range(len(prevRow) - 1):
            row.append(prevRow[j] + prevRow[j+1])

        row.append(1)
        rows.append(row)

    return rows


def main():
    rows = generateTriangleRows(10)

    for row in rows:
        for val in row:
            print(str(val) + " ", end="")
        print()


main()