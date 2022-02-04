# Project of Stefan Otto Novak
from csv import reader
List_Recordings = []
REQUESTS = {}



class Record:
    def __init__(self, id, timestamp, number_of_requests, number_of_errors, response_time, cpu_cores, memory_usage, cpu_usage):
        self.id = id
        self.timestamp = timestamp
        self.number_of_requests = number_of_requests
        self.number_of_errors = number_of_errors
        self.response_time = response_time
        self.cpu_cores = cpu_cores
        self.memory_usage = memory_usage
        self.cpu_usage = cpu_usage


# Load the data
with open('data/train.csv', 'r') as file:    # skip the first line(the header)
    file_csv = reader(file)
    head = next(file_csv)

    if head is not None:        # check if the file is empty or not
        for i in file_csv:      # Iterate over each row
            a_data = str(i).split(", ")

            id = a_data[0]
            timestamp = a_data[1]
            number_of_requests = a_data[2]
            number_of_errors = a_data[3]
            response_time = a_data[4]
            cpu_cores = a_data[5]
            memory_usage = a_data[6]
            cpu_usage = a_data[7]

            new_record = Record(id, timestamp, number_of_requests, number_of_errors, response_time, cpu_cores, memory_usage, cpu_usage)
            List_Recordings.append(new_record)



# At what time are most requests
for record in List_Recordings:
    hour = int(record.timestamp[12:14])
    #print(hour)
    if REQUESTS.__contains__(hour):
        REQUESTS[hour] += 1
    else:
        REQUESTS[hour] = 1

print(str(REQUESTS[13]) + " requets at hour 17")








