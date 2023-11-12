def describe_city(city, country='spain'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('madrid')
describe_city('mumbai', 'india')
describe_city('barcelona')