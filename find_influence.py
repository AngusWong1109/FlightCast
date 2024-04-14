def find_max_and_min(filePath):
    max = -100000
    min = 100000
    file = open(filePath, 'r')
    for line in file:
        influence_score = line.split(",")[-1]
        if(float(influence_score) > max):
            max = float(influence_score)
        if(float(influence_score) < min):
            min = float(influence_score)
    file.close()
    return max, min

max, min = find_max_and_min('./influence_data/arr_LOO_influence.txt')
print("Arr Max: ", max)
print("Arr Min: ", min)

max, min = find_max_and_min('./influence_data/dep_LOO_influence.txt')
print("Dep Max: ", max)
print("Dep Min: ", min)