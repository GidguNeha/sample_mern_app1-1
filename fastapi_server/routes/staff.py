from fastapi import APIRouter
stu_router=APIRouter(prefix="/staff")
@stu_router.get("/getStaffs")
def getStaffs():
    return "get staff method called"
@stu_router.post("/addstaff")
def addstaff():
    return "add staff method called"
