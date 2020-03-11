import requests
import json
import uuid
from time import sleep
def uID():
    # generate randomrandomrandomrandomrandomrandomrandomrandom numbers for unique user
    randomid = str(uuid.uuid1()).split('-')[4]
    file = open("unique_id.txt", "w")
    file.write(randomid)
    file.close()
    print("Your model's unique ID is --- ", randomid)
    print('Use the ID to verify the model via Nightwalker app.')

def api(json_dump):

    '''
     Function for collection of the provided variables and strings and sending them combined as a 'GET' request
     to be distributed by Flask server later on.
        Takes one argument - 'json_dump', that basically is a stringified combination of dictionaries.
    '''

    # declare endpoint_url for GET request
    endpoint_url = "http://157.230.107.88/sendModelData"
    
    # send GET request, followed by json_dump argument
    requests.post(endpoint_url, json=json_dump)


def walker(iteration='default', itercount='default', maxiter='default', epoch='default', maxepoch='default', trainloss='default', testloss='default',acc='default'):

    '''
        $iteration argument is for counting iterations. type = int.
 
       $itercount argument is basically a divider, for every how many iterations do you need to update information in the app. type = int.
 
       $maxiter is a maximum of iterations, after which the model finishes training. Make sure to send +1, as long as
       python takes the 'y' from range(x , y) and finishes the loop when technically y = (y - 1). type = int.
 
       $maxepoch is amount of epochs you're shooting for
 
       $epoch counts epochs. type = int.
 
       $trainloss takes train loss as an information. type = float.
 
       $testloss takes test loss as an information. type = float.
       
       $acc takes accuracy as an information. type=float
    '''
    try:
        f = open("unique_id.txt", "r")
        random = f.read()

    except FileNotFoundError:
        uID()
        f = open("unique_id.txt", "r")
        random = f.read()

    if iteration % itercount == 0 or (iteration == maxiter and epoch == maxepoch):
        json_dump = {'Iteration':iteration, 'Maxiter':maxiter, 'Epoch':epoch, 'MaxEpoch':maxepoch, 'Train Loss':trainloss, 'Test Loss':testloss, 'Accuracy':acc, 'ID':random}
        api(json_dump)
    else:
        print("You're not passing Iteration, Distribution and Maxiter variables correctly. Requests won't be sent.")

