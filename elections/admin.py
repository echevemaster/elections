# Admin functions go here (i.e. add/delete elections)

import turbogears
from turbogears import controllers, expose, flash, redirect
from elections import model
from elections.model import *

import sqlalchemy

from turbogears.database import session

# All instances of CHANGEME need to be changed to ensure that a user is in an admin group when we start authing against FAS
CHANGEME=1

class Admin(controllers.Controller):
    #@expose(template='elections.templates.adminlist')
    @expose()
    def index(self, **kw):
        return "Hi"

    @expose(template="elections.templates.admedit")
    def edit(self,eid=None):
        try:
            eid = int(eid)
        except ValueError:
            eid = Elections.query.filter_by(shortname=eid).all()[0].id
        candidates = Candidates.query.filter_by(election_id=eid).all()
        return dict(eid=eid, candidates=candidates)

    @expose()
    def save(self, **kw):
        return "Hi"
