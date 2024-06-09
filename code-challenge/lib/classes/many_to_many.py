class Band:
    def __init__(self, name, hometown):
        self._name = None
        self.name = name
        self.hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            print("Name must be a string.")
    
    
    
    def concerts(self):
        return self._concerts

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all_concerts = []

    def __init__(self, date, band, venue):
        self._date = None
        self.date = date
        self.band = band
        self.venue = venue
        self.venue._concerts.append(self)
        Concert.all_concerts.append(self)


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            print("Date must be a string.")


    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            print("Venue must be of type Venue.")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            print("Band must be of type Band.")

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    @classmethod
    def test_get_all_concerts(cls):
        return cls.all_concerts


class Venue:
    def __init__(self, name, city):
        self._name = None
        self.name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            print("Name must be a string.")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            print("City must be a string.")

    def concerts(self):
        return self._concerts
    def bands(self):
        return list(set(concert.band for concert in self._concerts))
