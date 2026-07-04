import subprocess


# uvicorn server:app --host 0.0.0.0 --port 8000
#creates "http://localhost:8000/chat"
def start_server():
    """
    Start the FastAPI server using uvicorn in a subprocess.
    """
    subprocess.Popen(
        [
            "uvicorn",
            "server:app",
            "--host", "0.0.0.0",
            "--port", "8000"
        ],
    creationflags=subprocess.CREATE_NO_WINDOW
    )

    # cloudflared tunnel --url http://localhost:8000
    # subprocess.Popen(
    #     [
    #         "cloudflared tunnel",
    #         "--url",
    #         "http://localhost:8000"
    #     ],
    # creationflags=subprocess.CREATE_NO_WINDOW
    # )

