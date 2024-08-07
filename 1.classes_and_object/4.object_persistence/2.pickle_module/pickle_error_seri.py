import pickle


def f1():
    print('Hello from the jar!')


with open('function.pckl', 'wb') as file_out:
    pickle.dump(f1, file_out)
