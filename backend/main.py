from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal 
from schemas import ProjectCreate, ProjectUpdate, ProjectResponse
from typing import List
from models import Base, Projects
from fastapi.middleware.cors import CORSMiddleware


#Create app FIRST
app = FastAPI(
    title="My FastAPI Backend",
    description="Simple FastAPI + MySQL Project CRUD",
    version="1.0.0"
)

#THEN add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Create database tables
Base.metadata.create_all(bind=engine)


#Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}


#Health Check
@app.get("/health")
def health_check():
    return {"status": "API is running"}



#CRUD OPERATIONS FOR PROJECTS


#CREATE Project
@app.post("/projects/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Projects(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


#READ All Projects
@app.get("/projects/", response_model=List[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Projects).all()
    return projects


#READ Single Project
@app.get("/projects/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Projects).filter(Projects.project_id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project


#UPDATE Project
@app.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, updated_data: ProjectUpdate, db: Session = Depends(get_db)):
    project = db.query(Projects).filter(Projects.project_id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)
    return project


#DELETE Project
@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Projects).filter(Projects.project_id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()
    return None