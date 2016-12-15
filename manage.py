#!/usr/bin/env python
import os
# from app import create_app, db
# from app import app, db
from app import create_app
from app.models import Hd, Rf, Wv, Slow, Hk, Sshk, Hk_surf, Turf, Mon, Adu5_pat, Adu5_vtg, Adu5_sat,\
G12_pos, G12_sat, Cmd, Wakeup, File
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

app=create_app()
manager = Manager(app)
# migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app,Hd=Hd,Wv=Wv,Hk=Hk,Slow=Slow,Sshk=Sshk,Hk_surf=Hk_surf,Turf=Turf,Mon=Mon,\
    	Adu5_pat=Adu5_pat,Adu5_vtg=Adu5_vtg, Adu5_sat=Adu5_sat,G12_pos=G12_pos,G12_sat=G12_sat,\
    	Cmd=Cmd,Wakeup=Wakeup,File=File)
# manager.add_command("runserver", Server(host='128.175.112.125'))
# thread share info, while processes does not.
manager.add_command("runserver", Server(threaded=True, processes=1))

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)



@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
