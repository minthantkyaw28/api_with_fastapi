#Entry point of FastAPI app
#is in the main.py

from imp import reload
import uvicorn

if __name__=="__main__":
    uvicorn.run( 
    "app.app:app",
    # host='127.0.0.1',
    port=9000,
    reload=True)

# chore: note 2025-06-25T13:43:59
