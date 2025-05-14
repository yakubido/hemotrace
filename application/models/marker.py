import sqlalchemy as sa
import sqlalchemy.orm as orm

from sqlalchemy.dialects.postgresql import INTEGER, FLOAT
from application import db
from typing import Optional


class Marker(db.Model):
    __tablename__ = 'markers'
    id: orm.Mapped[int] = orm.mapped_column(INTEGER(), primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(255), unique=True, nullable=False)
    unit: orm.Mapped[str] = orm.mapped_column(sa.String(50))
    normal_min: orm.Mapped[float] = orm.mapped_column(FLOAT(2))
    normal_max: orm.Mapped[float] = orm.mapped_column(FLOAT(2))
    description: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(4096), nullable=True)


class AnalysisMarker(db.Model):
    __tablename__ = 'analysis_markers'

    id: orm.Mapped[int] = orm.mapped_column(INTEGER(), primary_key=True)
    analysis_id: orm.Mapped[int] = orm.mapped_column(INTEGER(), sa.ForeignKey('analysis.id'), nullable=False)
    marker_id: orm.Mapped[int] = orm.mapped_column(INTEGER(), sa.ForeignKey('markers.id'), nullable=False)
    value: orm.Mapped[float] = orm.mapped_column(FLOAT(2), nullable=False)

    marker: orm.Mapped['Marker'] = orm.relationship(back_populates='markers')