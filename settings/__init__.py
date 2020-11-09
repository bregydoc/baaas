import os
import dotenv

dotenv.load_dotenv()

HOST: str = os.environ.get("HOST", "0.0.0.0")
PORT: int = os.environ.get("PORT", 5000)
