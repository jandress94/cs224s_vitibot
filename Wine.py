class Wine:
    def __init__(self, wineJson):
        self.id = wineJson['Id']
        self.name = wineJson['Name']
        self.url = wineJson['Url']
        self.varietal = wineJson['Varietal']['Name']
        self.vineyard = wineJson['Vineyard']['Name']
        self.vintage = wineJson['Vintage']
        self.price = wineJson['Retail']['Price']
        self.location = wineJson['Appellation']['Name']
        if 'Region' in wineJson['Appellation']:
            self.location += ' | ' + wineJson['Appellation']['Region']['Name']

    def __str__(self):
        resultString = 'Name: %s\nVarietal: %s\nVineyard: %s\nVintage: %s\nPrice: %s\nLocation: %s' % (self.name, self.varietal, self.vineyard, self.vintage, self.price, self.location)
        return resultString.encode('ascii', 'xmlcharrefreplace')


'''
{
   "Id":154614,
   "Name":"1000 Stories Bourbon Barrel Aged Zinfandel 2013",
   "Url":"http:\/\/www.wine.com\/v6\/1000-Stories-Bourbon-Barrel-Aged-Zinfandel-2013\/wine\/154614\/Detail.aspx",
   "Appellation":{
      "Id":2416,
      "Name":"North Coast",
      "Url":"http:\/\/www.wine.com\/v6\/North-Coast\/wine\/list.aspx?N=7155+101+2416",
      "Region":{
         "Id":101,
         "Name":"California",
         "Url":"http:\/\/www.wine.com\/v6\/California\/wine\/list.aspx?N=7155+101",
         "Area":null
      }
   },
   "Labels":[
      {
         "Id":"154614m",
         "Name":"thumbnail",
         "Url":"http:\/\/cache.wine.com\/labels\/154614m.jpg"
      }
   ],
   "Type":"Wine",
   "Varietal":{
      "Id":141,
      "Name":"Zinfandel",
      "Url":"http:\/\/www.wine.com\/v6\/Zinfandel\/wine\/list.aspx?N=7155+124+141",
      "WineType":{
         "Id":124,
         "Name":"Red Wines",
         "Url":"http:\/\/www.wine.com\/v6\/Red-Wines\/wine\/list.aspx?N=7155+124"
      }
   },
   "Vineyard":{
      "Id":999995404,
      "Name":"1000 Stories",
      "Url":"http:\/\/www.wine.com\/v6\/1000-Stories\/learnabout.aspx?winery=21821",
      "ImageUrl":"",
      "GeoLocation":{
         "Latitude":-360,
         "Longitude":-360,
         "Url":""
      }
   },
   "Vintage":"2013",
   "Community":{
      "Reviews":{
         "HighestScore":0,
         "List":[

         ],
         "Url":"http:\/\/www.wine.com\/v6\/1000-Stories-Bourbon-Barrel-Aged-Zinfandel-2013\/wine\/154614\/Detail.aspx?pageType=reviews"
      },
      "Url":"http:\/\/www.wine.com\/v6\/1000-Stories-Bourbon-Barrel-Aged-Zinfandel-2013\/wine\/154614\/Detail.aspx"
   },
   "Description":"",
   "GeoLocation":{
      "Latitude":-360,
      "Longitude":-360,
      "Url":""
   },
   "PriceMax":22.9900,
   "PriceMin":22.9900,
   "PriceRetail":22.9900,
   "ProductAttributes":[
      {
         "Id":613,
         "Name":"Big &amp; Bold",
         "Url":"http:\/\/www.wine.com\/v6\/Big-andamp-Bold\/wine\/list.aspx?N=7155+613",
         "ImageUrl":""
      }
   ],
   "Ratings":{
      "HighestScore":91,
      "List":[

      ]
   },
   "Retail":{
      "InStock":false,
      "Price":22.9900,
      "Sku":"YNG436526_2013",
      "State":"MA",
      "Url":""
   },
   "Vintages":{
      "List":[

      ]
   }
}
'''