import csv
import statistics
import random

def load_from_csv(filename):
    '''Returns a matrix from a csv file. Put the file name in speechmarks'''
    with open(filename, 'r') as p:
        my_list = [list(map(int,rec)) for rec in csv.reader(p, delimiter=',')]
        return my_list

def get_distance(list1, list2):
    """returns euclidian distance between 2 lists"""
    return sum((p-q)**2 for p, q in zip(list1, list2)) ** .5

def get_mean(matrix, column):
    '''Returns the mean of the column numbers in matrix'''
    x = [item[column] for item in matrix]
    return statistics.mean(x)

def get_standard_deviation(matrix, column):
    '''Retutns the standard deviation of the column numbers in matrix '''
    try:
        x = [item[column] for item in matrix]
        return statistics.stdev(x)
    except:
        print(" Please enter an integer between 0 and 8 for the column number")


def get_standardised_matrix(matrix):
    '''Returns the standardised version of the matrix'''
    alist =[[(matrix[x][y] - get_mean(matrix, y)) / get_standard_deviation(matrix, y) for y in range(len((matrix[x])))] for x in range(len(matrix))]
    return alist

def get_k_nearest_labels(lista, learningdata, learningdatalabels, k):
    '''Returns the k labels corresponding with the learning data'''
    distances = list()
    for a in learningdata:
        dist = get_distance(lista, a)
        distances.append((learningdata.index(a), dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(k):
        neighbors.append(distances[i][0])
    labels = list()
    for i in neighbors:
        labels.append(learningdatalabels[i])
    return labels

def get_mode(numbers):
    '''Returns the randomised mode from a matrix'''
    flat_list = [item for sublist in numbers for item in sublist]
    modes = (statistics.multimode(flat_list))
    return random.choice(modes)

def classify(data, learning_data, learning_data_labels, k):
    '''Returns the predicted labels made by the algorithm'''
    alist = []
    for item in data:
        a = get_k_nearest_labels(item, learning_data, learning_data_labels, k)
        alist.append(a)
    data_labels_mode = []
    for item in range(len(alist)):
        data_labels_mode.append(get_mode(alist[item]))
    data_labels = [[b] for b in data_labels_mode]
    return data_labels

def get_accuracy(list1, list2):
    '''Returns the accuracy between two matrices'''
    return (sum([sum([1 if x == list2[inx1][inx2] else 0 for inx2, x in enumerate(i)]) for inx1, i in enumerate(list1)]) / sum([len(i) for i in list1]) * 100)

def run_test():
    data = load_from_csv("C:/Users/Mayowa/Downloads/Data.csv")
    learning_data = load_from_csv("C:/Users/Mayowa/Downloads/Learning_Data.csv")
    learning_data_labels = load_from_csv("C:/Users/Mayowa/Downloads/Learning_Data_Labels.csv")
    correct_data_labels = load_from_csv("C:/Users/Mayowa/Downloads/Correct_Data_Labels.csv")    
    matrix_d = get_standardised_matrix(data)
    matrix_ld = get_standardised_matrix(learning_data)
    for i in range(3, 16):
        k = i
        a = classify(matrix_d, matrix_ld, learning_data_labels, k)
        accuracy = get_accuracy(a, correct_data_labels)
        print("k = %d, Accuracy = %d%%" % (k, accuracy))
    


