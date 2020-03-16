# don't use an unicode string
localeID = 'it_IT'
dateSep = ['/']
timeSep = [':', '.']
meridian= ['del mattino', 'di pomeriggio']
usesMeridian = True
uses24 = True

Weekdays = [
    'lunedì', 'martedì', 'mercoledì',
    'giovedì', 'venerdì', 'sabato', 'domenica',
]
shortWeekdays = [
    'lun', 'mar', 'mer',
    'gio', 'ven', 'sab', 'dom',
]
Months = [
    'gennaio', 'febbraio', 'marzo',
    'aprile', 'maggio', 'giugno',
    'luglio', 'agosto', 'settembre',
    'ottobre', 'novembre', 'dicembre',
]
shortMonths = [
    'gen', 'feb', 'mar',
    'apr', 'mag', 'giu',
    'lug', 'ago', 'set',
    'ott', 'nov', 'dic',
]
# use the same formats as ICU by default
dateFormats = {
    'full': 'EEEE d MMMM yyyy',
    'long': 'd MMMM yyyy',
    'medium': 'd MMM yyyy',
    'short': 'd/M/yy'
}

timeFormats = {
    'full': 'h:mm:ss a z',
    'long': 'h:mm:ss a z',
    'medium': 'h:mm:ss a',
    'short': 'h:mm a',
}

dp_order = ['d', 'm', 'y']

# Used to parse expressions like "in 5 hours"
numbers = {
    'zero': 0,
    'una': 1,
    'uno': 1,
    'un\'ora': 1,
    'due': 2,
    'tre': 3,
    'quattro': 4,
    'cinque': 5,
    'sei': 6,
    'sette': 7,
    'otto': 8,
    'nove': 9,
    'dieci': 10,
    'undici': 11,
    'dodici'
    'tredici': 13,
    'quattordici': 14,
    'quindici': 15,
    'sedici': 16,
    'diciassette': 17,
    'diciotto': 18,
    'diciannove': 19,
    'venti': 20,
    'ventuno': 21,
    'ventidue': 22,
    'ventre': 23,
    'ventiquattro': 24
}

decimal_mark = ','

# this will be added to re_values later
units = {
    'seconds': ['seconda', 'secondo', 'secondi', 'sec', 'seci', 's'],
    'minutes': ['minuta', 'minuto', 'minuti','min', 'mini', 'm'],
    'hours': ['ora', 'ore', 'o'],
    'days': ['giorno', 'giorni', 'g'],
    'weeks': ['settimana', 'settimane', 's'],
    'months': ['mese', 'mesi', 'm'],
    'years': ['anno', 'anni', 'a'],
}

# text constants to be used by later regular expressions
re_values = {
    'daysuffix': '°',
    'qunits': 'h|m|s|d|w|y',
    'now': ['adesso', 'proprio adesso'],
}

# Used to adjust the returned date before/after the source
Modifiers = {
    'prima': -1,
    'dopo': 1,
    'fa': -1,
    'lo scorso': -1,
    'scorsa': -1,
    'precedente': -1,
    'questa': 0
}

dayOffsets = {
    'domani': 1,
    'oggi': 0,
    'ieri': -1,
}

