from sqlalchemy.orm import relationship
from app.database import Base
# from app import db
from sqlalchemy import Table, Integer, Column, PrimaryKeyConstraint
# Base.metadata.reflect(db.engine)
# Base.metadata.bind=engine

class Hd(Base):
    # __table__ = Base.metadata.tables['hd']
    # __table__ = Table('hd', Base.metadata)
    __tablename__ = 'hd'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'us': self.us,
                        'ns': self.ns,
                        'evid': self.evid,
                        'evnum': self.evnum,
                        'surfmask': self.surfmask,
                        'calib': self.calib,
                        'priority': self.priority,
                        'turfword': self.turfword,
                        'l1mask': self.l1mask,
                        'l1maskh': self.l1maskh,
                        'peakthetabin': self.peakthetabin,
                        'imagepeak': self.imagepeak,
                        'coherentsumpeak': self.coherentsumpeak,
                        'prioritizerstuff': self.prioritizerstuff,
                        'trigtype': self.trigtype,
                        'trignum': self.trignum,
                        'l3cnt': self.l3cnt,
                        'pps': self.pps,
                        'trigtime': self.trigtime,
                        'c3po': self.c3po,
                        'deadtime': self.deadtime,
                        'l3trigpat': self.l3trigpat,
                        'l3trigpath': self.l3trigpath
                        }
        return json_comment
        
class Wv(Base):
    # __table__ = Table('wv', Base.metadata, PrimaryKeyConstraint("evnum", "id"),extend_existing=True)
    __tablename__ = 'wv'
    __table_args__ = ( PrimaryKeyConstraint("evnum","id"), {'autoload':True})
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf, 
                        'crc': self.crc,
                        'now': self.now,
                        'evnum': self.evnum,
                        'id': self.id,
                        'chip': self.chip,
                        'rcobit': self.rcobit,
                        'hbwrap': self.hbwrap,
                        'hbstart': self.hbstart,
                        'hbend': self.hbend,
                        'peds': self.peds,
                        'raw': self.raw,
                        'cal': self.cal
                        }
        return json_comment

class Slow(Base):
    # __table__ = Table('slow', Base.metadata, Column('time', Integer, primary_key=True), extend_existing=True)
    __tablename__ = 'slow'
    __table_args__ = (Column('time', Integer, primary_key=True), {'autoload':True})
    # time = Column(Integer, primary_key=True)
    def to_json(self):
        json_comment = {
                        #'nbuf': self.nbuf,  #nbuf is all 0s. useless
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'evnum': self.evnum,
                        'latitude': self.latitude,
                        'longitude': self.longitude,
                        'altitude': self.altitude,
                        'rate1': self.rate1,
                        'rate10': self.rate10,
                        'tempraw': self.tempraw,
                        'powerraw': self.powerraw,
                        'tempv': self.tempv,
                        'powerv': self.powerv,
                        'temp': self.temp,
                        'ppvv': self.ppvv,
                        'p24v': self.p24v,
                        'bati': self.bati,
                        'p24i': self.p24i,
                        'avgl3': self.avgl3,
                        'avgscaler': self.avgscaler,
                        'avgrfpow': self.avgrfpow
                        }
        return json_comment
