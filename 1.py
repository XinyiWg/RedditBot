"""
class province:
    def __init__(self, city, country=''):
        
        if country == '':
            self.country = country
            
          
        self.city = city
    
    def __str__(self):
        return self.country + self.city
    
     
province1=  province('Canada', 'montreal')
province2 = province('China', 'montreal')
print(province1)
print(province2)
"""
info = '{"id": "260745567", "name": "Larry"}'
a=info.split(',')
index = a[1].find('{')
print(a,index,a)


