def read_info_from_file(filename):
    width = 0
    height = 0
    corridor = []
    with open(filename, 'r') as input_file:
        i = 0
        for row in input_file:
            if (i != 0):
                for letter in row.strip().split():
                    letters = [symbol for symbol in letter]
                    corridor.append(letters)
            elif (i == 0):
                info = row.split()
                height = info[0]
                width = info[1]
                i += 1
    return corridor, height, width


def write_result_to_file(result):
    number_of_exists = str(result)
    with open('ijones.out.txt', 'w') as  result_file:
        result_file.write(number_of_exists)


def ijones(corridor, height, width):
    ways_to_get_to_tile = [[1 for _ in range(width)] for _ in range(height)]
    letters = {}
    for j in range(width):
        letters_in_column = {}
        if j == 0:
            for i in range(height):
                if corridor[i][j] not in letters_in_column:
                    letters_in_column.update({corridor[i][j]: ways_to_get_to_tile[i][j]})
                else:
                    new_value = letters_in_column.get(corridor[i][j]) + ways_to_get_to_tile[i][j]
                    letters_in_column[corridor[i][j]] = new_value
            letters.update(letters_in_column)
            continue
        for i in range(height):
            unique_tile = letters.get(corridor[i][j])
            number_of_ways = letters_in_column.get(corridor[i][j], 0)
            if unique_tile == None:
                ways_to_get_to_tile[i][j] = ways_to_get_to_tile[i][j - 1]
                number_of_ways += ways_to_get_to_tile[i][j]
                letters_in_column.update({corridor[i][j]: number_of_ways})
            else:
                if corridor[i][j] == corridor[i][j - 1]:
                    ways_to_get_to_tile[i][j] = unique_tile
                else:
                    ways_to_get_to_tile[i][j] = ways_to_get_to_tile[i][j - 1] + unique_tile
                number_of_ways += ways_to_get_to_tile[i][j]
                letters_in_column.update({corridor[i][j]: number_of_ways})

        for key in letters_in_column:
            if key in letters:
                new_value = letters_in_column.get(key) + letters.get(key)
                letters[key] = new_value
            else:
                letters[key] = letters_in_column.get(key)

    print(ways_to_get_to_tile)
    print(letters)

    number_of_ways_to_exit = ways_to_get_to_tile[0][-1]
    if height > 1:
        number_of_ways_to_exit += ways_to_get_to_tile[-1][-1]
    return number_of_ways_to_exit


if __name__ == "__main__":
    INPUT_FILE_NAME = "ijones.in.txt"
    res = read_info_from_file(INPUT_FILE_NAME)
    corridor = res[0]
    print(corridor)
    result = ijones(corridor, int(res[1]), int(res[2]))
    print(result)
    write_result_to_file(result)
