from fastapi import APIRouter, Depends

from app.main import router as scrapeRoutes

from app.auth import authMiddleware

router = APIRouter(dependencies=[Depends(authMiddleware)])
# router = APIRouter()


router.include_router(scrapeRoutes, tags=["Scrape Routes"])

