import sqlalchemy as sa
import sqlalchemy.orm as orm

from sqlalchemy.dialects.postgresql import INTEGER
from application import db
from datetime import datetime, timezone
from .marker import AnalysisMarker


class User(db.Model):
    __tablename__ = 'users'

    id: orm.Mapped[int] = orm.mapped_column(INTEGER(), primary_key=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String(255), unique=True, nullable=False)
    hashed_password: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False)
    created_at: orm.Mapped[datetime] = orm.mapped_column(sa.TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)

    analyses: orm.WriteOnlyMapped['Analysis'] = orm.relationship(backref='user', lazy=True)

    @classmethod
    def get_user_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()
    
    def __repr__(self):
        return '<User: {}>'.format(self.email)

class Analysis(db.Model):
    __tablename__ = 'analysis'

    id: orm.Mapped[int] = orm.mapped_column(INTEGER(), primary_key=True)
    user_id: orm.Mapped[int] = orm.mapped_column(INTEGER(), sa.ForeignKey('users.id'), nullable=False)
    status: orm.Mapped[str] = orm.mapped_column(sa.String(50), default='pending')
    document_path: orm.Mapped[str] = orm.mapped_column(sa.String(255))
    uploaded_at: orm.Mapped[datetime] = orm.mapped_column(sa.TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)

    markers: orm.WriteOnlyMapped['AnalysisMarker'] = orm.relationship(backref='analysis', lazy=True)

    @classmethod
    def get_analyse_by_id(cls, analyse_id):
        return cls.query.filter_by(id=analyse_id).first()
    
    def __repr__(self):
        return '<Analyse: {}>'.format(self.id)