import googlemaps

client = googlemaps.Client('AIzaSyDiUC9hvx9tYVmtgAvqYecdAK9wMkSY6xU')

def find_place_ids(query, page_token=None):
    places = client.places(query=query, page_token=page_token)
    results = places['results']
    place_ids = [place['place_id'] for place in results]
    return place_ids[:1], places['next_page_token']

def get_place_details(place_ids):
    fields = ['name', 'formatted_address', 'website', 'formatted_phone_number']
    for place_id in place_ids:
        place = client.place(place_id=place_id, fields=fields)
        result = place['result']
        yield {
            'name': result['name'],
            'address': result['formatted_address'],
            'website': result.get('website'),
            'contact_number': result['formatted_phone_number'],
        }

def get_places(query, token=None, results=None):
    results = results or []
    place_ids, page_token = find_place_ids(query, page_token=token)
    places = [
        place for place in get_place_details(place_ids=place_ids) if place['website']
    ]
    results.extend(places)
    return results
