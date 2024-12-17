
# Online Python - IDE, Editor, Compiler, Interpreter

class LogSystem:
    def __init__(self):
        # Initialize logs list to hold all the log entries as tuples (id, timestamp)
        self.logs = []
      
        # Dictionary to map the granularity level to the index of timestamp string
        self.granularity_to_index = {
            "Year": 4,    # Index where the Year value ends in the timestamp
            "Month": 7,   # Index where the Month value ends in the timestamp
            "Day": 10,    # Index where the Day value ends in the timestamp
            "Hour": 13,   # Index where the Hour value ends in the timestamp
            "Minute": 16, # Index where the Minute value ends in the timestamp
            "Second": 19, # Index where the Second value ends in the timestamp
        }

    def put(self, log_id: int, timestamp: str) -> None:
        # Store the log with its id and timestamp
        self.logs.append((log_id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list:
        # Find the index up to which we will compare timestamps based on the granularity
        index = self.granularity_to_index[granularity]
      
        # Retrieve log_ids of logs where timestamp is within the start and end range,
        # sliced according to the granularity level
        return [log_id for log_id, ts in self.logs if start[:index] <= ts[:index] <= end[:index]]

# Example of how to use the LogSystem class
obj = LogSystem()
print(obj.put(1, "2017:01:01:23:59:59"))
print(obj.put(2, "2017:01:01:22:59:59"))
print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))
# results = obj.retrieve(start, end, granularity)
