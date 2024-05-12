from abc import ABC, abstractmethod

# Interface for output strategy
class OutputStrategy(ABC):
    @abstractmethod
    def output(self, data):
        pass

# Concrete strategy for console output
class ConsoleOutput(OutputStrategy):
    def output(self, data):
        print("Console Output:")
        for line in data:
            print(line)

# Concrete strategy for Kafka output
class KafkaOutput(OutputStrategy):
    def output(self, data):
        # Connect to Kafka and publish data
        print("Kafka Output:")
        for line in data:
            # Publish line to Kafka topic
            print(f"Published to Kafka: {line}")

# Context class that uses the strategy
class OutputContext:
    def __init__(self, output_strategy):
        self.output_strategy = output_strategy

    def set_output_strategy(self, output_strategy):
        self.output_strategy = output_strategy

    def output_data(self, data):
        self.output_strategy.output(data)

# Main code for reading data and outputting
def read_data(file_path):
    # Read data from file
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

if __name__ == "__main__":
    # Example usage
    
    # Read data from file
    data = read_data("example_data.txt")

    # Instantiate output strategies
    console_output = ConsoleOutput()
    kafka_output = KafkaOutput()

    # Set initial output strategy (console)
    output_context = OutputContext(console_output)

    # Output data using the current strategy
    output_context.output_data(data)

    # Switch to Kafka output strategy (without changing the main code)
    output_context.set_output_strategy(kafka_output)

    # Output data using the new strategy
    output_context.output_data(data)
