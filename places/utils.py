import googlemaps

client = googlemaps.Client('AIzaSyCn3YGIibVn_wFzfhaFwsi759fEsvNuwUM')

def find_place_ids(query, page_token=None):
    places = client.places(query=query, page_token=page_token)
    results = places['results']
    place_ids = [place['place_id'] for place in results]
    return place_ids, places['next_page_token']

def get_place_details(place_id):
    fields = ['name', 'formatted_address', 'website', 'formatted_phone_number']
    place = client.place(place_id=place_id, fields=fields)
    result = place['result']
    return {
        'name': result['name'],
        'address': result['formatted_address'],
        'website': result.get('website'),
        'contact_number': result['formatted_phone_number'],
    }

def get_places(query, token=None, results=None):
    results = results or []
    place_ids, page_token = find_place_ids(query, page_token=token)
    places = []
    for place_id in place_ids:
        place = get_place_details(place_id)
        if place['website']:
            places.append(place)
    results.extend(places)
    if not len(results) == 30:
        return get_places(query=query, token=page_token, results=results)
    return results

