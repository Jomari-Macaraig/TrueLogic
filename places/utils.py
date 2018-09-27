import googlemaps

client = googlemaps.Client('AIzaSyCn3YGIibVn_wFzfhaFwsi759fEsvNuwUM')

def find_place_ids(query):
    places = client.places(query=query)
    place_ids = [place['place_id'] for place in places['results']]
    return place_ids

def get_place_details(place_id):
    fields = ['name', 'formatted_address', 'website', 'formatted_phone_number']
    place = client.place(place_id=place_id, fields=fields)
    result = place['result']
    return {
        'name': result['name'],
        'address': result['formatted_address'],
        'website': result['website'],
        'contact_number': result['formatted_phone_number'],
    }
