Info:
This is a python script integrates with Trello API to pull out the exact status of the trello boards, lists and tickets.

Libraries used:
1. Requests
2. JSON
3. Pandas

Process:
1. Find the API url from trello and add the required aspects that needs to be pulled out. For eg., if board details is needed use API specified for Board else if list details is needed use API specified for list and so on..
2. Once the url is finalized, use requests module to send requests to the destined url and get the response. Response needs to be '200' if there is no error.
3. When the received response is 200, use json module to unpack the json object from the return response.
4. Once json object is returned, use data structures to unpack and load the data from json objects based on the requirements.
5. Finally using pandas convert the created data structure to a data frame and load the dataframe in an excel or csv depending on the feasibility.
