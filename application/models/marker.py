import sqlalchemy as sa
import sqlalchemy.orm as orm

from sqlalchemy.dialects.postgresql import INTEGER
from application import db
from datetime import datetime, timezone

class AnalysisMarker(db.Model):
    __tablename__ = 'analysis_markers'