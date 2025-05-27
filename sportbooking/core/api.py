from ninja import NinjaAPI
from typing import List
from pydantic import BaseModel
from .models import SportFacility, Reservation, Review

api = NinjaAPI()

# Schemas pro serializaci modelů

class FacilitySchema(BaseModel):
    id: int
    name: str
    location: str
    capacity: int

    model_config = {
        "from_attributes": True  # pro pydantic v2 je to místo orm_mode
    }

class ReservationSchema(BaseModel):
    id: int
    user_id: int
    facility_id: int
    date: str  # může být date nebo str
    start_time: str
    end_time: str

    model_config = {
        "from_attributes": True
    }
class ReviewSchema(BaseModel):
    id: int
    user_id: int
    facility_id: int
    text: str
    rating: int

    model_config = {
        "from_attributes": True
    }

# Endpoints

@api.get("/facilities", response=List[FacilitySchema])
def list_facilities(request):
    facilities = SportFacility.objects.all()
    return facilities

@api.get("/reservations", response=List[ReservationSchema])
def list_reservations(request):
    reservations = Reservation.objects.all()
    return reservations

@api.get("/reviews", response=List[ReviewSchema])
def list_reviews(request):
    reviews = Review.objects.all()
    return reviews
