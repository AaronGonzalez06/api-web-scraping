import bs4
import requests

class ScrapingSerivce:
    url_use = 'http://books.toscrape.com/catalogue/page-{}.html'
    
    def filterRating(self,min,max):        
        minAux = "Cero"
        maxAux = "Cero"
        if min == 1:
            minAux = "One"
        elif min == 2:
            minAux = "Two"
        elif min == 3:
            minAux = "Three"
        elif min == 4:
            minAux = "Four"
        elif min == 5:
            minAux = "Five"
        
        if max == 1:
            maxAux = "One"
        elif max == 2:
            maxAux = "Two"
        elif max == 3:
            maxAux = "Three"
        elif max == 4:
            maxAux = "Four"
        elif max == 5:
            maxAux = "Five"
            
        search = []
        for x in range(1,20):
            result = requests.get(self.url_use.format(x))
            data = bs4.BeautifulSoup(result.text, 'lxml')
            products = data.select('.product_pod')
            for product in products:
                if product.find(class_=minAux) or product.find(class_=maxAux):
                    title = product.find('h3').find('a')['title']
                    price = product.find(class_="price_color").getText()
                    product_data = {
                        'title': title,
                        'price': price
                    }
                    search.append(product_data)        
        return search
    
    
    def filterPrice(self,min,max):
        search = []
        for x in range(1,20):            
            result = requests.get(self.url_use.format(x))
            data = bs4.BeautifulSoup(result.text, 'lxml')
            products = data.select('.product_pod')
            for product in products:
                title = product.find('h3').find('a')['title']
                price = product.find(class_="price_color").getText()
                price_filter = float(price.replace("Â£", ""))                     
                if price_filter>= min and price_filter<=max:
                    product_data = {
                        'title': title,
                        'price': price_filter
                    }
                    search.append(product_data)   
        return search        
    
    def filterPriceGender(self,min,max,gender):
        if gender.lower() == "mystery":
            url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-{}.html'
        elif gender.lower() == "romance":
            url = 'http://books.toscrape.com/catalogue/category/books/romance_8/page-{}.html'
        elif gender.lower() == "fiction":
            url = 'http://books.toscrape.com/catalogue/category/books/fiction_10/page-{}.html'
        elif gender.lower() == "fantasy":
            url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-{}.html'
 
        result = requests.get(url.format(1))
        data = bs4.BeautifulSoup(result.text, 'lxml')
        totalBooks= data.select('form')[0].find('strong').getText()
        book=0
        x=1
        search = []
        while(book != int(totalBooks)):
            result = requests.get(url.format(x))
            data = bs4.BeautifulSoup(result.text, 'lxml')
            products = data.select('.product_pod')
            for product in products:
                title = product.find('h3').find('a')['title']
                price = product.find(class_="price_color").getText()
                price_filter = float(price.replace("Â£", ""))                     
                if price_filter>= min and price_filter<=max:
                    product_data = {
                        'title': title,
                        'price': price_filter
                    }                    
                    search.append(product_data)
                book+=1
            x+=1                            
        return search
    
    def filterRatingGender(self,min,max,gender):
        if gender.lower() == "mystery":
            url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-{}.html'
        elif gender.lower() == "romance":
            url = 'http://books.toscrape.com/catalogue/category/books/romance_8/page-{}.html'
        elif gender.lower() == "fiction":
            url = 'http://books.toscrape.com/catalogue/category/books/fiction_10/page-{}.html'
        elif gender.lower() == "fantasy":
            url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-{}.html'
                    
        minAux = "Cero"
        maxAux = "Cero"
        if min == 1:
            minAux = "One"
        elif min == 2:
            minAux = "Two"
        elif min == 3:
            minAux = "Three"
        elif min == 4:
            minAux = "Four"
        elif min == 5:
            minAux = "Five"
        
        if max == 1:
            maxAux = "One"
        elif max == 2:
            maxAux = "Two"
        elif max == 3:
            maxAux = "Three"
        elif max == 4:
            maxAux = "Four"
        elif max == 5:
            maxAux = "Five"
            
        result = requests.get(url.format(1))
        data = bs4.BeautifulSoup(result.text, 'lxml')
        totalBooks= data.select('form')[0].find('strong').getText()
        book=0
        x=1
        search = []
        while(book != int(totalBooks)):
            result = requests.get(url.format(x))
            data = bs4.BeautifulSoup(result.text, 'lxml')
            products = data.select('.product_pod')
            for product in products:
                if product.find(class_=minAux) or product.find(class_=maxAux):
                    title = product.find('h3').find('a')['title']
                    price = product.find(class_="price_color").getText()
                    product_data = {
                        'title': title,
                        'price': price
                    }
                    search.append(product_data)   
                book+=1
            x+=1      
        return search