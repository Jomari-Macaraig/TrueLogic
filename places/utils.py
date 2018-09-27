import googlemaps

client = googlemaps.Client('AIzaSyCn3YGIibVn_wFzfhaFwsi759fEsvNuwUM')

def find_place_ids(query, page_token):
    places = client.places(query=query, page_token=page_token)
    results = places['results']
    place_ids = [place['place_id'] for place in results]
    return place_ids, results['next_page_token']

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
