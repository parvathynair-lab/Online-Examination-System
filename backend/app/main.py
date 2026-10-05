from fastapi import FastAPI
app=FastAPI(title="Online Examination System",description="API for an online quiz and examination system",version="1.0.0")
@app.get("/")


def home():
    return{"message":"Online Examination System APIis running!"}

@app.get("/health")
def health_check():
    return {"status":"healthy"}