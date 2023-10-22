from services.scrapingService import ScrapingSerivce
from fastapi import FastAPI, HTTPException

scrping = ScrapingSerivce()
app = FastAPI()


@app.get('/')
def welcome():
    return {"message": "App API books web scraping"}

@app.get('/filterRating/{minRating}/{maxRating}')
def filterRating(minRating: int,maxRating: int):
    return scrping.filterRating(minRating,maxRating)

@app.get('/filterPrice/{minRating}/{maxRating}')
def filterPrice(minRating: int,maxRating: int):
    return scrping.filterPrice(minRating,maxRating)

@app.get('/filterPriceGender/{minRating}/{maxRating}/{category}')
def filterPriceGender(minRating: int,maxRating: int,category: str):
    return scrping.filterPriceGender(minRating,maxRating,category)

@app.get('/filterRatingGender/{minRating}/{maxRating}/{category}')
def filterRatingGender(minRating: int,maxRating: int,category: str):
    return scrping.filterRatingGender(minRating,maxRating,category)

