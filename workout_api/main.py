from fastapi import FastAPI

app = FastAPI(
    title='WorkoutAPI',
    version='0.1.0',
    description='API para uma academia, desenvolvida no bootcamp de Python da DIO'
)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à WorkoutAPI!"}