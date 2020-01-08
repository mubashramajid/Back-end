




team_namespace = api.namespace("team", description="endpoints for team module")

@api.route('/team/')
class TeamList(Resource):

    def get(self):
        get_data = db.session.query(Team).all()
        result = []
        for row in get_data:
            result.append({"team_name": row.teamName, "team_members": row.teamMembers})
        return {"data": result}
        pass


department_namespace = api.namespace("department", description="endpoints for team module")

@api.route('/department/')
class DepartmentList(Resource):

    def get(self):
        get_data = db.session.query(Department).all()
        result = []
        for row in get_data:
            result.append({"depart_name": row.departName, "no_of_employee": row.noOfEmployee})
        return {"data": result}
        pass



reviews_namespace = api.namespace("reviews", description="endpoints for team module")

@api.route('/reviews/')
class ReviewsList(Resource):

    def get(self):
        get_data = db.session.query(Reviews).all()
        result = []
        for row in get_data:
            result.append({"initiate_date": row.initiateDate, "completion_date": row.completionDate,"status": row.status})
        return {"data": result}
        pass



kpi_namespace = api.namespace("kpi", description="endpoints for team module")

@api.route('/kpi/')
class KPIList(Resource):

    def get(self):
        get_data = db.session.query(KPI).all()
        result = []
        for row in get_data:
            result.append({"kpi_attribute": row.kpiAttribute,"initiate_date": row.initiateDate, "completion_month": row.completionMonth,"completion_year": row.completionYear,"status": row.status})
        return {"data": result}
        pass



form_namespace = api.namespace("form", description="endpoints for team module")

@api.route('/form/')
class FormList(Resource):

    def get(self):
        get_data = db.session.query(Form).all()
        result = []
        for row in get_data:
            result.append({"issue_date": row.issueDate,"no_of_form_generate": row.noOfFormGenerate})
        return {"data": result}
        pass


comments_namespace = api.namespace("comments", description="endpoints for team module")

@api.route('/Comments/')
class CommentsList(Resource):

    def get(self):
        get_data = db.session.query(Comments).all()
        result = []
        for row in get_data:
            result.append({"issue_date": row.issueDate,"no_of_form_generate": row.noOfFormGenerate})
        return {"data": result}
        pass