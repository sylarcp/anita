from sqlalchemy.orm import relationship
from app.database import Base, engine0
# from app import db
from sqlalchemy import Table, Integer, Column, PrimaryKeyConstraint
# Base.metadata.reflect(db.engine)
# Base.metadata.bind=engine

class Hd(Base):
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
                        'l3trigpath': self.l3trigpath,
                        'phimask': self.phimask,
                        'phimaskh': self.phimaskh
                        }
        return json_comment
class Rf(Base):
    __tablename__ = 'rf'
    __table_args__ = (Column('nbuf', Integer, primary_key=True), {'autoload':True})
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
                        'l3trigpath': self.l3trigpath,
                        'phimask': self.phimask,
                        'phimaskh': self.phimaskh
                        }
        return json_comment    
class Hk(Base):
    __tablename__ = 'hk'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'us': self.us,
                        'code': self.code,
                        'cal': self.cal,
                        'avz': self.avz,
                        'bd1': self.bd1,
                        'bd2': self.bd2,
                        'bd3': self.bd3,
                        'calb1': self.calb1,
                        'calb2': self.calb2,
                        'calb3': self.calb3,
                        'accx': self.accx,
                        'accy': self.accy,
                        'accz': self.accz,
                        'acct': self.acct,
                        'ssx': self.ssx,
                        'ssy': self.ssy,
                        'ssi': self.ssi,
                        'ssflag': self.ssflag,
                        'ssel': self.ssel,
                        'ssaz': self.ssaz,
                        'sst': self.sst,
                        'pressh': self.pressh,
                        'pressl': self.pressl,
                        'p1_5v': self.p1_5v,
                        'p3_3v': self.p3_3v,
                        'p5v': self.p5v,
                        'p5sbv': self.p5sbv,
                        'p12v': self.p12v,
                        'p24v': self.p24v,
                        'ppvv': self.ppvv,
                        'n5v': self.n5v,
                        'n12v': self.n12v,
                        'iprf1v': self.iprf1v,
                        'iprf2v': self.iprf2v,
                        'p1_5i': self.p1_5i,
                        'p3_3i': self.p3_3i,
                        'p5i': self.p5i,
                        'p5sbi': self.p5sbi,
                        'p12i': self.p12i,
                        'p24i': self.p24i,
                        'ppvi': self.ppvi,
                        'n5i': self.n5i,
                        'n12i': self.n12i,
                        'iprf1i': self.iprf1i,
                        'iprf2i': self.iprf2i,
                        'bati': self.bati,
                        'p5vip': self.p5vip,
                        'it': self.it,
                        'et': self.et,
                        'sbst1': self.sbst1,
                        'sbst2': self.sbst2,
                        'core1': self.core1,
                        'core2': self.core2,
                        'sbst5': self.sbst5,
                        'sbst6': self.sbst6,
                        'magx': self.magx,
                        'magy': self.magy,
                        'magz': self.magz

                        }
        return json_comment

class Wv(Base):
    # __table__ = Table('wv', Base.metadata, PrimaryKeyConstraint("evnum", "id"),extend_existing=True)
    __tablename__ = 'wv'
    __table_args__ = ( PrimaryKeyConstraint("evnum","id"), {'autoload':True})
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf, 
                        # 'crc': self.crc,
                        'now': self.now,
                        'evnum': self.evnum,
                        'id': self.id,
                        # 'chip': self.chip,
                        # 'rcobit': self.rcobit,
                        # 'hbwrap': self.hbwrap,
                        # 'hbstart': self.hbstart,
                        # 'hbend': self.hbend,
                        # 'peds': self.peds,
                        # 'raw': self.raw,
                        # 'cal': [int(cal*100) for cal in self.cal]
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

class Sshk(Base):
    __tablename__ = 'sshk'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'time': self.time,
                        'us': self.us,
                        'now': self.now,
                        'code': self.code,
                        'cal': self.cal,
                        'avz': self.avz,
                        # 'bdl': self.bdl,
                        # 'calb1': self.calb1,
                        'ssx': self.ssx,
                        'ssy': self.ssy,
                        'ssi': self.ssi,
                        'ssflag': self.ssflag,
                        'ssel': self.ssel,
                        'ssaz': self.ssaz,
                        'sst': self.sst
            }
        return json_comment

class Hk_surf(Base):
    __tablename__ = 'hk_surf'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'us': self.us,
                        #'global': self.global,
                        'error': self.error,
                        'scalergoals': self.scalergoals,
                        #'nadirgoals': self.nadirgoals,
                        'upper': self.upper,
                        'scaler': self.scaler,
                        'thresh': self.thresh,
                        'thershset': self.threshset,
                        'rfpow': self.rfpow,
                        'l1scaler': self.l1scaler,
                        'surfask': self.surfmask
            }
        return json_comment

class Turf(Base):
    __tablename__ = 'turf'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'deadtime': self.deadtime,
                        'l2trigmask': self.l2trigmask,
                        # 'l1trigmaskh': self.l1trigmaskh,
                        'phitrigmask': self.phitrigmask,
                        # 'phitrigmaskh': self.phitrigmaskh,
                        'l2': self.l2,
                        # 'l1h': self.l1h,
                        'l3': self.l3,
                        'l3gated': self.l3gated,
                        # 'l3h': self.l3h
            }
        return json_comment

class Mon(Base):
    __tablename__ = 'mon'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'disk': self.disk,
                        'blade': self.blade,
                        'usbint': self.usbint,
                        'usbext': self.usbext,
                        'linkev': self.linkev,
                        'linkcmdlos': self.linkcmdlos,
                        'linkcmdsip': self.linkcmdsip,
                        'linkgps': self.linkgps,
                        'linkhk': self.linkhk,
                        'linkmon': self.linkmon,
                        'linkhd': self.linkhd,
                        'linksurf': self.linksurf,
                        'linkturf': self.linkturf,
                        'linkped': self.linkped
            }
        return json_comment

class Adu5_pat(Base):
    __tablename__ = 'adu5_pat'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'gpstype': self.gpstype,
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'code': self.code,
                        'time': self.time,
                        'us': self.us,
                        'tod': self.tod,
                        'heading': self.heading,
                        'pitch': self.pitch,
                        'roll': self.roll,
                        'mrms': self.mrms,
                        'brms': self.brms,
                        'flag': self.flag,
                        'latitude': self.latitude,
                        'longitude': self.longitude,
                        'altitude': self.altitude
            }
        return json_comment
    def to_czml(self):
        czml_comment = {
          'id': 'myObject',
          'availability': '2014-01-15T00:00Z/2014-01-01T24:00Z',
          'point': {
            'color': {
              'rgba': [255, 255, 0, 255]
            },
            'outlineWidth': 2.0,
            'pixelSize': 3.0,
            'show': True
          },
          "position" : {
            "epoch" : "2012-08-04T10:00:00Z",
            "cartographicDegrees" : [0,self.latitude,self.longitude,self.altitude]
          }
        }
        return czml_comment
class Adu5_vtg(Base):
    __tablename__ = 'adu5_vtg'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'gpstype': self.gpstype,
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'code': self.code,
                        'time': self.time,
                        'us': self.us,
                        'course': self.course,
                        'mcourse': self.mcourse,
                        'vkt': self.vkt,
                        'vkph': self.vkph
            }
        return json_comment

class Adu5_sat(Base):
    __tablename__ = 'adu5_sat'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'gpstype': self.gpstype,
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'code': self.code,
                        'time': self.time,
                        'numsats': self.numsats,
                        'prn': self.prn,
                        'elevation': self.elevation,
                        'snr': self.snr,
                        'flag': self.flag,
                        'azimuth': self.azimuth
            }
        return json_comment

class G12_pos(Base):
    __tablename__ = 'g12_pos'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf,
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'us': self.us,
                        'tod': self.tod,
                        'numsats': self.numsats,
                        'latitude': self.latitude,
                        'longitude': self.longitude,
                        'altitude': self.altitude,
                        'course': self.course,
                        'upv': self.upv,
                        'vkt': self.vkt,
                        'pdop': self.pdop,
                        'hdop': self.hdop,
                        'vdop': self.vdop,
                        'tdop': self.tdop,
                        'unit': self.unit
            }
        return json_comment

class G12_sat(Base):
    # __table__ = Table('wv', Base.metadata, PrimaryKeyConstraint("evnum", "id"),extend_existing=True)
    __tablename__ = 'g12_sat'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf, 
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'numsats': self.numsats,
                        'prn': self.prn,
                        'elevation': self.elevation,
                        'snr': self.snr,
                        'flag': self.flag,
                        'azimuth': self.azimuth
                        
                        }
        return json_comment

class Cmd(Base):
    # __table__ = Table('wv', Base.metadata, PrimaryKeyConstraint("evnum", "id"),extend_existing=True)
    __tablename__ = 'cmd'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf, 
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'flag': self.flag,
                        'bytes': self.bytes,
                        'cmd': self.cmd
                        
                        }
        return json_comment


class Wakeup(Base):
    # __table__ = Table('wv', Base.metadata, PrimaryKeyConstraint("evnum", "id"),extend_existing=True)
    __tablename__ = 'wakeup'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf, 
                        'crc': self.crc,
                        'now': self.now,
                        'type': self.type
                        
                        }
        return json_comment



class File(Base):
    # __table__ = Table('wv', Base.metadata, PrimaryKeyConstraint("evnum", "id"),extend_existing=True)
    __tablename__ = 'file'
    __table_args__ = {'autoload':True}
    def to_json(self):
        json_comment = {
                        'nbuf': self.nbuf, 
                        'crc': self.crc,
                        'now': self.now,
                        'time': self.time,
                        'filename': self.filename,
                        'length': self.length,
                        'content': self.content,
                        'hbwrap': self.hbwrap,
                        'hbstart': self.hbstart
                        
                        }
        return json_comment