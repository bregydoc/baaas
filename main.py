from raw import retrieve_data_by_code, search_by_code
from api.service import app
from settings import HOST, PORT
import uvicorn

# data = search_by_code("12509324")

# print(data)

# data = retrieve_data_by_code("", "5212")

# print(data)


if __name__ == "__main__":
    # app.run(host=HOST, port=PORT, debug=False)
    uvicorn.run(app, host=HOST, port=PORT)
