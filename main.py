from fastapi import FastAPI
from grab_from_libgen import LibgenSearch

# To run the app : python3 -m uvicorn main:app --reload

app = FastAPI()

@app.get("/getresults")
def getresults(title = None):

    if title is None:
        resultats = 'Enter a title!'

    else:
        res = LibgenSearch('fiction', q=title)
        resultats = res.get_results()

    return resultats