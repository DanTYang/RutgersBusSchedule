import urllib.request
import json
import time
def timeFromNowDisplay(times):
    seconds = time.time()
    total = time.localtime(seconds+times)
    local_time = time.strftime(" %I:%M %p", total)
    return local_time

def secondConverter(seconds):
    minutes = 0
    hours = 0
    days = 0
    years = 0
    if seconds > 60:
        minutes = seconds // 60
        seconds = seconds - (minutes * 60)
        if minutes > 60:
            hours = minutes // 60
            minutes = minutes - (hours * 60)
            if hours > 24:
                days = hours // 24
                hours = hours - (days * 24)
                if days > 365:
                    years = days // 365
                    days = days - (years * 365)
                    print(str(years) + ' years, ' + str(days) + ' days, ' + str(hours) + ' hours, ' + str(minutes) + ' minutes, ' + str(seconds) + ' seconds.')
                else:
                    print(str(days) + ' days, ' + str(hours) + ' hours, ' + str(minutes) + ' minutes, ' + str(seconds) + ' seconds.')
            else:
                print(str(hours) + ' hours, ' + str(minutes) + ' minutes, ' + str(seconds) + ' seconds.')
        else:
            print(str(minutes) + ' minutes, ' + str(seconds) + ' seconds.')
    else:
        print(str(seconds) + ' seconds.')

def googleMapsTimeFind(origin, destination, mode):
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = 'AIzaSyBfKCT5x8kJRM8ovCvq5khtWtzWGUnWMh4'
    nav_request = 'origin={}&destination={}&mode={}&key={}'.format(origin, destination, mode, api_key)
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    seconds = int(directions['routes'][0]['legs'][0]['duration']['value'])
    return seconds

num_classes = input('Number of classes?: ')
storage = {'Classes':[], 'Locations':[]}
for i in range(int(num_classes)):
    ClassName = input('What is the name of class '+ str(i + 1) +'?: ')
    ClassLoc = input('Which building is it Located in?: ').replace(' ','+')
    storage['Classes'].append(ClassName)
    storage['Locations'].append(ClassLoc)
time_difference = 0
print('curent time:' +timeFromNowDisplay(0))
for i in range(int(num_classes) - 1):
    origin = storage['Locations'][i]
    destination = storage['Locations'][i+1]
    print('Arival time to ' + storage['Classes'][i+1] + ': ' +timeFromNowDisplay(googleMapsTimeFind(origin, destination, 'walking') + time_difference))
    time_difference = time_difference + googleMapsTimeFind(origin, destination, 'walking')