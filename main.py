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

