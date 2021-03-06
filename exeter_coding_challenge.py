import csv, sys, time
import os
import psutil

def initialize_french_dictionary():
  #store it in csv_file variable
    with open('french_dictionary.csv') as csv_file: 
       #creating another variable and call on the inbuilt method csv.reader
       #delimiter is used to separate datas from datasets
        csv_reader = csv.reader(csv_file, delimiter=',') 
        for row in csv_reader:
          #to iterate the elements one by one with respect to the english word
            french_dict[row[0]] =[row[1],0]


def translate(input_file): #calls on the english file
    print('Read the corresponding file.')
    #a new file is created to write the translated texts
    fp1 = open('t8.shakespeare.translated.txt', 'w') 
    #the key values from the dictionary is stored in check_list
    check_list = french_dict.keys() 
    with open(input_file, 'r') as input_text: #until the texts exist in the english file has been read
        while True:
            line = input_text.readline() #the line is read and stored in "line"
            if not line:
                break
            buffer = ''
            for word in line.split(): #invoking the line and splitting their words individually and storing it in "word"
                filtered = filter(str.isalpha,word)  #the function of alphabetical splitted word is stored in filtered
                #the function from filtered are checked and is joined to an empty string to make it a string
                query = "".join(filtered) 
                if query in check_list:
                    query_success = french_dict[query][0]  #after filtering compare it with the words given in dictionary
                    french_dict[query][1] += 1 #check the next elements sequentially
                    word = word.replace(query, query_success) #now the english(query) is replaced with frenchdict(query_success) and saved in word
                buffer += word + ' ' 
            buffer = buffer.strip() #removes spaces before and front
            fp1.write(buffer + '\n') #now we write the buffer sentence into that
    fp1.close()
    print(f'Given file {input_file} is Translated to French')
    return True

def generate_frequency_csv():
    print('Frequency is generated and added to frequency.csv file.')
    with open('frequency.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['English', 'French', 'Frequency'])
        for words in french_dict:
            writer.writerow([words, french_dict[words][0], french_dict[words][1]])
    print('Frequency Created.')
    return True

def generate_performance(process_time, memory_info):
    print('Perfomance is generated and added to perfomance.txt file')
    with open('performance.txt', 'w') as file:
        file.write(f"Time to process : {process_time} seconds\n") 
        file.write(f"Memory used : {memory_info} MB")
    print('Perfomance Measured.')

if __name__ == '__main__':
   #to find the perfomance of the task
   #time is a function which holds the time since the process starts
    process_start_time = time.time() 
    french_dict = {} #declaration of a dict
    input_file = 't8.shakespeare.txt' #receiving the input english file

    if len(sys.argv) == 2: 
        input_file = sys.argv[1] #Handling the exception here
        
    #Invoking the functions
    initialize_french_dictionary() 
    translate(input_file)
    generate_frequency_csv()
    process_complete_time = time.time()
    memory_used = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2 
    #RSS (resident set size), getpid - process value now returns integer 
    #value which gets convered to rss, returns in KB
    process_time = process_complete_time - process_start_time
    generate_performance(process_time, memory_used)
