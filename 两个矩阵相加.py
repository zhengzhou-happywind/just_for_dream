# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵.
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]


def matrix_plus():
    """
    两个矩阵相加，得到新的矩阵
    :return: 
    """
    new_li = []
    # 循环遍历X矩阵最外层的一个个列表，以及每个列表的索引
    for outer_index, each_inner_li in enumerate(X):
        # 在第一层循环内，创建空列表，用于存储矩阵最内层每个元素相加的值
        new_inner_li = []
        # 循环X矩阵每个外出列表里面的元素，以及其索引
        for inner_index, x_num in enumerate(each_inner_li):
            # 利用外层以及内层的索引，拿到Y矩阵对应的值
            y_num = Y[outer_index][inner_index]
            x_num += y_num
            # 把两个矩阵的值相加之后，存入本层循环外创建的空列表
            new_inner_li.append(x_num)
        # 这里把内层的列表，依次存入最外层的空列表中
        new_li.append(new_inner_li)
    return new_li


ret_li = matrix_plus()
print(X)
print(Y)
print(ret_li)
