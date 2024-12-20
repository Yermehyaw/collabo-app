# Run the fastAPI app n debug mode
# NOTE: The dependencies listed in requirements.txt must be installed prior to running this script

# Activate a running mongoDB server
sudo systemctl start mongod
service mongod start

# Run the app
uvicorn main:app --reload
