import sys
categories=["table", "chair", "cupboard"]

category_to_index = {category: index for index, category in enumerate(categories)}

one_hot_matrix = []

for category in categories:
    one_hot_row = [0] * len (categories)
    one_hot_row[category_to_index[category]] = 1
    one_hot_matrix.append(one_hot_row)

for row in range(len(one_hot_matrix)):
    print(categories[row], one_hot_matrix[row])
