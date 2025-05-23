from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

# Check if templates directory exists
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
if os.path.exists(templates_dir):
    templates = Jinja2Templates(directory=templates_dir)
else:
    templates = None

@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Root endpoint that redirects to the NiceGUI application.
    This is a fallback for when the application is accessed via FastAPI.
    """
    if templates:
        return templates.TemplateResponse("redirect.html", {"request": request, "url": "/"})
    else:
        # If templates are not available, return a simple HTML response
        html_content = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Redirecting...</title>
                <meta http-equiv="refresh" content="0;url=/" />
            </head>
            <body>
                <p>Redirecting to the AI Engineer Portfolio...</p>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)