import pandas as pd
import matplotlib.pyplot as plt
import ast
import os

data = {
    'id': [1290, 82894, 56042, 12345, 67890, 54321],
    'name': ['Mathews', 'Anas', 'Arsh', 'Sara', 'John', 'Emma'],
    'class': [12, 12, 12, 11, 11, 10],
    'div': ['M', 'M', 'M', 'N', 'N', 'O'],
    'progress': [
        [76, 65, 99, 54, 100],
        [90, 78, 55, 89, 98],
        [67, 85, 47, 99, 73],
        [88, 92, 71, 66, 95],
        [77, 45, 80, 79, 85],
        [85, 93, 62, 48, 88]
    ]
}

df = pd.DataFrame(data)
if os.path.exists('./data.csv'):
    print('exists')
else:
    df.to_csv('data.csv', index = False)
    print('loaded')

read_data = pd.read_csv('data.csv')
read_df = pd.DataFrame(read_data)

read_df['progress'] = read_df['progress'].apply(ast.literal_eval)


def add(reg, name, grade, div, progress):
    try:
        read_df.loc[len(read_df['class'])] = [reg, name, grade, div, progress]
        print('student added \n', read_df, '\n___________________')
    except ValueError:
        print('there was something wrong')

def remove(id):
    try:
        for i in range(0, len(read_df['class']), 1):
            output = read_df.loc[i]

            if output[0] == id:
                read_df.drop(i, inplace= True)
                read_df.reset_index(inplace = True)
                print('deleted \n', read_df)
                break
    except ValueError:
        print("that's not a valid registration number")

def progress():
    plt.clf()
    exams = ['FA1', 'SA1', 'FA2', 'SA2', 'Models']
    for i in range(0, len(read_df['class'])):
        li = read_df.loc[i]
        plt.plot(li[4], label = li[1])
    plt.legend()  
    plt.xticks(ticks = [0,1,2,3,4], labels=exams)
    plt.title('Examination Progress')
    plt.xlabel('Examination')
    plt.ylabel('Marks')
    plt.savefig('./plotted.png')
    plt.show()

def topper(achievers):
    marks = {'name': [], 'marks': []}
    rank = []
    for i in range(len(read_df['class'])):
        progress = read_df.loc[i, 'progress']
        total = 0
        for item in progress:
            total += item
        average = total/5
        marks['name'].append(read_df.loc[i, 'name'])
        marks['marks'].append(average)
        
    toppers_df = pd.DataFrame(marks)
    top = toppers_df.sort_values(by='marks', ascending = False)
    
    if achievers == 'high':
        if len(read_df['class']) > 3:
            print(top.head(3))
        else:
            print(top.head(len(read_df['class'])))
    else:
        if len(read_df['class']) > 3:
            print(top.tail(3))
        else:
            print(top.tail(len(read_df['class'])))
                   

#add(2398, 'John', 11, 'M', [23,45,64,23,64])
#remove(56042)
#progress()
#topper('high')

while True:
    menu = "Choose an option from the given menu by entering a digit corresponding to the function you want to use: \n\n1. Get the Student's Data\n2. Get an analysis of the marks scored\n3. Get data on the lowest or top achievers\n4. Add a student to the database\n5. Remove a student from the database\n6. Save the database to csv\n\n\nEnter(1-6): "
    user_input = int(input(menu))
    if user_input == 1:
        print(read_df)
    elif user_input == 2:
        progress()
    elif user_input == 3:
        achiever_input = int(input("For high achievers, press 1\nFor low achievers, press 2\n\nEnter: "))
        if achiever_input == 1:
            topper('high')
        elif achiever_input == 2:
            topper('low')
        else:
            print('incorrect input')
    elif user_input == 4:
        reg_id = int(input("Enter the student's registration id: "))
        name = str(input("Enter the student's name: "))
        grade = int(input("Enter the student's present class: "))
        div = str(input("Enter the student's class division: "))
        print("\nmarks(out of 100): \n\n")
        fa1 = int(input("Enter the student's FA1 Marks: "))
        sa1 = int(input("Enter the student's SA1 Marks: "))
        fa2 = int(input("Enter the student's FA2 Marks: "))
        sa2 = int(input("Enter the student's SA2 Marks: "))
        models = int(input("Enter the student's MODELS Marks: "))
        progress = [fa1, sa1, fa2, sa2, models]
        add(reg_id, name, grade, div, progress)
    elif user_input == 5:
        print(read_df)
        reg_id = int(input("Enter the registration id of the student to be removed: "))
        remove(reg_id)
    elif user_input == 6:
        read_df.to_csv('data.csv', index=False)
    else:
        print('Invalid Choice! Try Again.')
        
    
































    
    
