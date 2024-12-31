Fast Api:
step 1 :
create virtual environment  py -m venv  .venv
step 2 :
 pip install fastapi
upgrage pip
pip install -U pip

#some standard packages that require ,group of optional dependencies:
pip install "uvicorn[standard]"

step-3:
create a main.py file ,
from fastapi import FastApi 
FastApi-base object / Root object of FastApi
#create innstance
app=FastApi()

#define a get method
@app.get("/")
async def index():
  return {"hello":"world"}
@app.get("/about")
async def about():
 return "An Exceptional Company"

###->we can specify the return type also
where 1st function a dictnary object,and second function return string object 

async def index()->dict[str,str]:      #index()->list Error
  return {"hello":"world"}
async def about()->str:
 return "An Exceptional Company"

#run locally:
uvicorn main:app --reload


######### Path Parameter in FastApi ##############
@app.get("/users/{user_id}")
#->endpoint for returning list of data
#->returning for individual object

########### type-hints and limit the path parameter value using pre-define set python Enums for data validation #####
str_field : type-hint:    declare in handler function for spefic data type
next() ->python inbuilt method take a iterable obj ,defult parameter
HttpException(status_code,detail) of FastApi

#improve the efficencey of field search in database table apply validate path parameter with Enum Class
from enum import Enum
class GenereURLChoices(Enum):
    ROCK='rocks'
    ELECTRONIC='electronics'
    METAL='metal'
    HIP_HOP='hip_hop'

@app.get("/brands/genre/{genre}")
async def brands_for_genre(genre:GenereURLChoices)->list[dict]:
    return [b for b in BANDS if b['genre'].lower()==genre.value.lower()]

### pydantics
Pydantic: Is mostly use data validation in python
using the pandantic module use can use extra validate, pandantic takecare of json converttion

for more modularity approach ,lets create a scama.py and Brand class there
->from pandic module we have to import BaseModel,we creat a class inherite the BaseModal

schema.py
++++++++
@app.get("/bands/{band_id}")
async def band(band_id:int)->Band:
    band=next((Band(**b) for b in BANDS if b['id']==band_id),None)

using nested module wih pydantic:
from pydantic import BaseModel
class Album(BaseModel):
    title:str
    relese_date:date
    
class Band(BaseModel):
    #  {"id":1,"name":"The kins","genre":"Rocks"},
    id:int
    name:str
    genre:str
    album:list[Album]=[]

##########Query parameter Filtering################
all brands- filter with genere and has Album

@app.get("/bands")
async def bands(genre:GenereURLChoices| None=None,hasAlbum=False )->list[Band]:
    band_list=[Band(**b) for b in BANDS]
    if genre:
        return[b for b  in band_list if b.genre.lower()==genre.value]
    if hasAlbum:
        return[b for b  in band_list if len(b.album)>=1]
    return band_list

#### implement Post and send data with json Request body:
----band class restructure:
class BaseBand(BaseModel):
    name:str
    genre:str
    albums:list[Album]=[]
class BandCreate(BaseBand):
    pass
class BandWithId(BaseBand):
    id:int

@app.post("/bands")
async def create_band(band_data:BandCreate)->BandWithId:
    id=BANDS[-1]['id']+1
    band=BandWithId(id=id,**band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band
##### test with rest cllient 
app.http
======
POST http://127.0.0.1:8000/bands/
Content-Type: application/json

{
    "name":"Boards of Canada ",
    "genre":"Electronics",
    "albums":[
        {
            "title":"Tommorow's Harvest",
            "release_date":"2024-09-08"
        },
        {
            "title":"Music has the Right to Children",
            "release_date":"2024-09-08"
        }
      ]
}

###
GET http://127.0.0.1:8000/bands/


##### typing module- Annotated Parameter  ###
->typing module added in python 3.5
->this module provide run type support for type-hint

typing.Annotated:   specify context-specific metadata to an annotation
============
->Metadata added using annoted can be specifiy static analysics toll at run time
Annotated[int,(0,10)]
->if annotated has no logic for metedata it is ignored
from typing import Annoted
syntax Annotated[type,(validate_data)]
test.py
++++
for annoted example understand flow
--------------------------------------------
 def double(x:Annotated:[int,(0,10)])->int:
     return x*2
 print(double(11)) #as the validation logic is not defined 22 is comes as output

Apply to Quert string:
import Annoted from typing ,Query form fastApi
->by default a query parameter takes any no of character,by using annoted you can limit parameter  charcter
->use Query objet from fastapi for validate rules in querystring
->we can used Annotated not only in query parameter in FastApi but in path and header also

from fastapi import FastAPI,HTTPException,Path,Query
from typing import Annotated
@app.get("/bands")
async def bands(genre:GenereURLChoices| None=None,
                q:Annotated[str|None,Query(max_length=10)]=None
                )->list[BandWithId]:
    band_list=[BandWithId(**b) for b in BANDS]
    if genre:
        return[b for b  in band_list if b.genre.lower()==genre.value]
    if  q:
        return[b for b  in band_list if q.lower() in b.name.lower()]
    return band_list

@app.get("/bands/{band_id}")
async def band(band_id:Annotated[int,Path(title="THE BAND ID")])->BandWithId:
    band=next((BandWithId(**b) for b in BANDS if b['id']==band_id),None)
    # print(band)
    if band==None:
        raise HTTPException(status_code=404,detail="band not found")
    else:
        return band
----------------------------------------------------------------------------------
###test.py  using the decorator compress the logic
from typing import Annotated,get_type_hints,get_origin,get_args

from functools import wraps
#add decorator for bellow function double
def check_value_range(func):
    @wraps(func)
    def wrapped(x):
        tpye_hints=get_type_hints(double,include_extras=True)
        hint=tpye_hints['x']
        if get_origin(hint) is Annotated:
            tpye_hint,*hint_args=get_args(hint)
            low,high=hint_args[0]
            if not low <= x <=high:
                raise ValueError(f'{x} falls outside boundary {low}-{high}')
        #execute function once all checks passed
        return func(x)
    return wrapped
@check_value_range
def double(x:Annotated[int,(0,10)])->int:
    """ tpye_hints=get_type_hints(double,include_extras=True)
    hint=tpye_hints['x']
    # print(hint)
    #get_origin->return annotated type of unsusbripted type of X
    #get_argus->tpet type argument with all substitution perform
    if get_origin(hint) is Annotated:
        tpye_hint,*hint_args=get_args(hint)
        # print(tpye_hint)
        # print(hint_args)
        low,high=hint_args[0]

        if not low <= x <=high:
            # print( "not wintin range")
            # pass
            raise ValueError(f'{x} falls outside boundary {low}-{high}') """
    return x * 2

print(double(5))
# print(double(11))
