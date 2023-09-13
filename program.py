from di_builder import di
from app import Application

app = di.resolve(Application)
