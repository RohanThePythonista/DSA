from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Train the chatbot with some data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Define the sources of data
data_sources = {
    'dlz': ['column1', 'column2', 'column3'],
    'edl': ['column4', 'column5', 'column6'],
    'hub': ['column7', 'column8', 'column9']
}


# Define a function to prompt the user for input
def get_user_input(data_source):
    inputs = {}
    for column in data_sources[data_source]:
        inputs[column] = input(f'Please enter a value for {column}: ')
    return inputs


# Define a function to insert the user's input into a SQL database
def insert_into_database(inputs):
    # Generate the SQL insert query here
    # ...
    print(f"{inputs} at insert_into_database")
    print('Data inserted into database')


# Define a function to process a new row in the database
def process_new_row(row):
    # Process the new row here
    # ...
    print(f"{row} at process_new_row")
    print('New row processed')


# Start the chatbot
while True:
    # Prompt the user to select a data source
    data_source = input('Please select a data source (dlz, edl, hub): ')
    if data_source not in data_sources:
        print('Invalid data source')
        continue

    # Prompt the user for input based on the selected data source
    inputs = get_user_input(data_source)

    # Insert the user's input into the SQL database
    insert_into_database(inputs)

    # Process the new row in the database
    process_new_row(inputs)

    # Respond to the user
    response = chatbot.get_response('Thanks, your input has been saved.')
    print(response)
