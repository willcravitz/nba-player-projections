# NBA Player Projections

## Setup
Clone the repository, and in the root of the directory run the following:
       
       python3 -m venv venv
       source venv/bin/activate
       pip3 install pip --upgrade
       pip3 install -r requirements.txt

Create a `.env` file in the root of the directory and add the following line:

      DATABASE_URL=sqlite:///<database_name>.db

where `<database_name>` can be whatever you choose.

## Running the Server
From the root of the directory run:

      uvicorn app.main:app

If you're developing and want changes reflected as you edit the code, then use:

      uvicorn app.main:app --reload
