from fastapi import FastAPI
from grab_from_libgen import LibgenSearch

# To run the app : python3 -m uvicorn main:app --reload

app = FastAPI()

@app.get("/title")
def getfromtitles(title = None):

    if title is None:
        resultats = 'Enter a title!'

    else:
        res = LibgenSearch('fiction', q=title)
        resultats = res.get_results()

    return resultats

@app.get("/author")
def getfromtauthor(author = None):

    if author is None:
        resultats = 'Enter an author!'

    else:
        res = LibgenSearch('authors', q=author)
        resultats = res.get_results()

    return resultats