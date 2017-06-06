
category_dict = {
    'type': {
        'red': 124,
        'white': 125,
        'rose': 126
    },
    'varietal': {
        'cabernet sauvignon': 139,
        'chardonnay': 140,
        'sauvignon blanc': 151,
        'pinot gris': 194,
        'pinot grigio': 194,
        'bordeaux blends': 144,
        'pinot noir': 143,
        'other red blends': 145,
        'sangiovese': 163,
        'shiraz': 146,
        'syrah': 146,
        'rhone blends': 10082,
        'albarino': 136,
        'barbera': 172,
        'cabernet franc': 197,
        'carmenere': 10081,
        'chenin blanc': 165,
        'dolcetto': 183,
        'gamay': 150,
        'gewurztraminer': 166,
        'grenache': 10080,
        'gruner veltliner': 10087,
        'junmai': 198,
        'junmai-daiginjo': 127,
        'junmai-ginjo': 199,
        'madeira': 154,
        'malbec': 10079,
        'merlot': 138,
        'mourvedre': 10083,
        'muscat': 173,
        'nebbiolo': 170,
        'nero d\'avola': 10086,
        'non-vintage': 182,
        'other dessert': 160,
        'other red wine': 195,
        'other white blends': 148,
        'other white wine': 196,
        'petite sirah': 176,
        'pinot blanc': 168,
        'pinotage': 10085,
        'primitivo': 10084,
        'port': 155,
        'riesling': 153,
        'rose': 147,
        'sherry': 157,
        'semillon': 177,
        'tempranillo': 169,
        'torrontes': 209,
        'vermouth': 156,
        'vintage': 181,
        'viognier': 162,
        'white zinfandel': 175,
        'zinfandel': 141,
        'bordeaux white blends': 221,
        'rhone white blends': 10113,
    },
    'style': {
        'red - light & fruity': 610,
        'red - smooth & supple': 611,
        'red - earthy & spicy': 612,
        'red - big & bold': 613,
        'white - light & crisp': 614,
        'white - fruity & smooth': 615,
        'white - rich & creamy': 616,
        'sweet': 617,
    },
    'region': {
        'california': 101,
        'washington': 104,
        'oregon': 103,
        'other us': 111,
        'australia': 108,
        'new zealand': 114,
        'france - bordeaux': 10038,
        'france - rhone': 10039,
        'france - other regions': 102,
        'italy': 105,
        'spain': 109,
        'portugal': 107,
        'israel': 119,
        'germany': 106,
        'greece': 115,
        'other european': 118,
        'south america': 112,
        'south africa': 113,
        'japan': 122,
        'mexico': 15427,
        'canada': 121,
    },
    'appellation': {
        'champagne': 2331,
        'chile': 2428,
        'coonawarra': 9060,
        'austria': 607,
        'barossa': 9058,
        'burgundy': 2457,
        'napa valley': 2398,
        'canada': 1781,
        'beaujolais': 2397,
        'carneros': 2454,
        'russian river': 1863,
        'alsace': 2148,
        'argentina': 2089,
        'clare valley': 9059,
        'columbia valley': 2414,
        'mclaren vale': 9063,
        'tuscany': 2452,
        'yarra valley': 9064,
        'greece': 1455,
        'chablis': 10063,
        'hungary': 1726,
        'slovenia': 1727,
        'victoria': 10077,
        'margaret river': 9062,
        'israel': 2097,
        'rheingau': 1837,
        'hokkaido': 2475,
        'sonoma county': 2371,
        'gisborne': 10074,
        'provence': 10064,
        'languedoc-roussillon': 2374,
        'santa maria valley': 2124,
        'loire': 2333,
        'mosel-saar-ruwer': 2268,
        'new york': 1867,
        'piedmont': 2431,
        'rioja': 2370,
        'none': 2346,
        'yakima valley': 2052,
        'trentino-alto adige': 2279,
        'ribera del duero': 9067,
        'other german': 1650,
        'cote rotie': 10053,
        'priorat': 9066,
        'navarra': 10075,
        'santa cruz mountains': 965,
        'central coast': 2462,
        'north coast': 2416,
        'sierra foothills': 2288,
        'other california': 2388,
        'portugal': 2377,
        'friuli-venezia giulia': 2310,
        'rias baixas': 10065,
        'veneto': 2352,
        'southern italy': 2143,
        'sardinia': 10068,
        'walla walla valley': 1956,
        'south australia': 10078,
        'south africa': 2283,
        'switzerland': 943,
        'willamette valley': 2474,
        'umpqua valley': 2195,
        'rogue river valley': 2157,
        'other french': 2312,
        'sicily': 10066,
        'other italian': 2309,
        'condrieu': 10054,
        'hermitage': 10055,
        'cornas': 10056,
        'chateauneuf-du-pape': 10057,
        'tavel': 10058,
        'gigondas': 10059,
        'vacqueyras': 10062,
        'cotes du rhone': 10061,
        'rasteau': 10060,
        'other rhone': 2375,
        'hunter valley': 9061,
        'other australia': 2405,
        'hawkes bay': 10069,
        'martinborough': 10070,
        'marlborough': 10071,
        'waipara valley': 10072,
        'central otago': 10073,
        'other new zealand': 2273,
        'akita': 2476,
        'tochigi': 2490,
        'niigata': 2492,
        'hiroshima': 2493,
        'tottori': 2495,
        'ibaraki': 2496,
        'iwate': 2491,
        'osaka': 2498,
        'shizuoka': 2497,
        'shimane': 2494,
        'st. estephe': 10044,
        'margaux': 10040,
        'pauillac': 10049,
        'medoc': 10041,
        'pessac-leognan': 10051,
        'sauternes and barsac': 10046,
        'graves': 10045,
        'st-emilion': 10042,
        'pomerol': 10043,
        'fronsac': 10047,
        'cotes de castillon': 10048,
        'other bordeaux': 10052,
        'rueda': 10076,
        'jumilla': 10067,
        'idaho': 2341,
        'mexico': 2337,
        'new mexico': 2338,
        'north carolina': 2344,
        'other': 2500,
        'other spain': 9065,
        'sardinia': 2315,
        'texas': 2339,
        'virginia': 2340,
    },
    'vintage': {
        'non-vintage': 37,
        '1875': 301,
        '1908': 302,
        '1910': 303,
        '1912': 305,
        '1921': 306,
        '1922': 307,
        '1933': 308,
        '1934': 309,
        '1937': 310,
        '1940': 311,
        '1941': 312,
        '1944': 314,
        '1945': 315,
        '1948': 317,
        '1950': 319,
        '1952': 320,
        '1953': 321,
        '1954': 322,
        '1955': 323,
        '1958': 324,
        '1959': 325,
        '1961': 327,
        '1962': 328,
        '1963': 329,
        '1964': 330,
        '1966': 331,
        '1967': 332,
        '1968': 333,
        '1969': 334,
        '1970': 335,
        '1971': 336,
        '1972': 337,
        '1973': 338,
        '1974': 339,
        '1975': 340,
        '1976': 341,
        '1977': 342,
        '1978': 343,
        '1979': 344,
        '1980': 345,
        '1981': 346,
        '1982': 347,
        '1983': 348,
        '1984': 349,
        '1985': 350,
        '1986': 351,
        '1987': 352,
        '1988': 353,
        '1989': 354,
        '1990': 355,
        '1991': 356,
        '1992': 357,
        '1993': 358,
        '1994': 359,
        '1995': 360,
        '1996': 361,
        '1997': 362,
        '1998': 363,
        '1999': 364,
        '2000': 365,
        '2001': 366,
        '2002': 367,
        '2003': 368,
        '2004': 369,
        '2005': 370,
        '2006': 371,
        '2007': 372,
        '2008': 373,
        '2009': 374,
        '2010': 375,
        '2011': 376,
        '2012': 377,
        '2013': 378,
        '2014': 379,
        '2015': 380,
        '2016': 381,
        '2017': 382,
    }
}