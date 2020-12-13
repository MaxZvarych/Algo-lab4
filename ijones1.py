def read_info_from_file(filename):
    width = 0
    height=0
    corridor = []
    with open(filename, 'r') as input_file:
        i = 0
        for row in input_file:
            if (i != 0):
                for letter in row.strip().split():
                    letters=[symbol for symbol in letter]
                    corridor.append(letters)
            elif (i == 0):
                info = row.split()
                height= info[0]
                width=info[1]
                i += 1
    return corridor, height, width

def write_result_to_file(result):
    number_of_exists=str(result)
    with open('ijones.out.txt','w') as  result_file:
        result_file.write(number_of_exists)


def ijones(corridor,height,width):
    ways_to_get_to_tile = [[1 for _ in range(width)] for _ in range(height)]
    letters = {}
    for j in range(width):
        letters_in_column={}
        if j==0:
            for i in range(height):
                letters_in_column.update({corridor[i][j]: ways_to_get_to_tile[i][j]})
            letters.update(letters_in_column)
            continue
        for i in range(height):
            unique_tile = letters.get(corridor[i][j])
            number_of_ways=letters_in_column.get(corridor[i][j],0)
            if unique_tile == None:
                ways_to_get_to_tile[i][j] = ways_to_get_to_tile[i][j - 1]
                number_of_ways+=ways_to_get_to_tile[i][j]
                letters_in_column.update({corridor[i][j]: number_of_ways})
            else:
                ways_to_get_to_tile[i][j]=ways_to_get_to_tile[i][j-1]+unique_tile
                letters_in_column.update({corridor[i][j]: ways_to_get_to_tile[i][j]})
        letters.update(letters_in_column)

    print(ways_to_get_to_tile)
    print(letters)


if __name__ == "__main__":
    INPUT_FILE_NAME = "ijones.in.txt"
    res=read_info_from_file(INPUT_FILE_NAME)
    corridor=res[0]
    print(corridor)
    ijones(corridor,int(res[1]),int(res[2]))