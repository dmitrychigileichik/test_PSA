import sys


#  Function for changing lines with 'case' function
def my_script(direction):
    # List for accumulation lines to rewrite the original file
    out = []
    # Opening original file in reading mode
    with open(direction, 'r', encoding='utf-8') as file:
        for line in file:
            # Checking if necessary lane
            if 'cast(' in line:
                # Splitting to right and left parts
                right_side = line.split(' = ')[1]
                left_side = line.split(' = ')[0]
                # Separation if necessary
                casting_part = [x.strip() for x in right_side.strip().split('cast') if x]
                adding = (')', ']', '}', '"')
                removing = ('(', '[', '{', '"')
                result = []
                # Handling information in brackets
                for elem in casting_part:
                    buffer = []
                    l_item = -1
                    while elem[l_item] != ')':
                        l_item -= 1
                    f_item = l_item
                    while elem[f_item] != ',' or buffer:
                        f_item -= 1
                        if elem[f_item] in adding and '"' not in buffer:
                            buffer.append(elem[f_item])
                        elif elem[f_item] in removing:
                            buffer.pop()
                    # Adding right information to temporary result
                    result.append(elem[f_item+1:l_item].strip())
                # Adding temporary result into list to accumulate right lines
                out.append(left_side + ' = ' + ', '.join(result) + '\n')
            else:
                # Adding line if there no function 'cast'
                out.append(line)
    # Rewriting the original file with necessary information
    with open(direction, 'w', encoding='utf-8') as output:
        output.writelines(''.join(out))


if __name__ == '__main__':
    path = sys.argv[1]
    my_script(path)
