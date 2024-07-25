from pydantic import BaseModel
class fraud(BaseModel):
    amt : float
    gender : int
    city_pop : int
    merch_lat : float
    merch_long : float