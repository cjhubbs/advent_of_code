metadata_sum = 0

def p1_process_node(data):
    global metadata_sum
    num_of_children = int(data.pop(0))
    num_of_metadata = int(data.pop(0))
    for c in range(num_of_children):
        p1_process_node(data)
    for m in range(num_of_metadata):
        metadata_sum += int(data.pop(0))

def p2_process_node(data):
    value = 0
    num_of_children = int(data.pop(0))
    num_of_metadata = int(data.pop(0))
    children = []
    for c in range(num_of_children):
        children.append(p2_process_node(data))
    for m in range(num_of_metadata):
        if num_of_children == 0:
            value += int(data.pop(0))
        else:
            idx = int(data.pop(0))
            if 0 < idx <= len(children):
                value += children[idx-1]
    return value


#p1
f = open("8-input.txt", "r")
items = f.read().split(" ")
p1_process_node(items)
print(metadata_sum)

#p2
f = open("8-input.txt", "r")
items = f.read().split(" ")
print(p2_process_node(items))
