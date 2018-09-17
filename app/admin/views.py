# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import DepartmentForm, EmployeeAssignForm, RoleForm, LoreForm, HunterForm
from .. import db
from ..models import Department, Employee, Role, Lore, Hunter, NewsModel

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

def check_lore():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_lore:
        abort(403)

def check_chart():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_chart:
        abort(403)

# Lore Views

@admin.route('/lore', methods=['GET', 'POST'])
@login_required
def list_lores():
    """
    List all lore entrys
    """
    check_lore()

    lores = Lore.query.all()

    return render_template('admin/lores/lores.html',
                           lores=lores, title="Lore")

@admin.route('/lores/add', methods=['GET', 'POST'])
@login_required
def add_lore():
    """
    Add a lore
    """
    check_lore()

    add_lore = True

    form = LoreForm()
    if form.validate_on_submit():
        lore = Lore(title=form.title.data,
                                loreBody=form.loreBody.data, imageUrl=form.imageUrl.data)
        try:
            # add lore to the database
            db.session.add(lore)
            db.session.commit()
            flash('You have successfully added a new lore entry.')
        except:
            # in case lore name already exists
            flash('Error: lore title already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_lores'))

    # load department template
    return render_template('admin/lores/lore.html', action="Add",
                           add_lore=add_lore, form=form,
                           title="Add Lore")

@admin.route('/lores/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_lore(id):
    """
    Edit a lore entry
    """
    check_lore()

    add_lore = False

    lore = Lore.query.get_or_404(id)
    form = LoreForm(obj=lore)
    if form.validate_on_submit():
        lore.title = form.title.data
        lore.loreBody = form.loreBody.data
        lore.imageUrl = form.imageUrl.data
        db.session.commit()
        flash('You have successfully edited the lore entry.')

        # redirect to the departments page
        return redirect(url_for('admin.list_lores'))

    form.title.data = lore.title
    form.loreBody.data = lore.loreBody
    form.imageUrl.data = lore.imageUrl
    return render_template('admin/lores/lore.html', action="Edit",
                           add_lore=add_lore, form=form,
                           lore=lore, title="Edit lore entry")

@admin.route('/lores/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_lore(id):
    """
    Delete a lore entry from the database
    """
    check_lore()

    lore = Lore.query.get_or_404(id)
    db.session.delete(lore)
    db.session.commit()
    flash('You have successfully deleted the lore entry.')

    # redirect to the departments page
    return redirect(url_for('admin.list_lores'))

    return render_template(title="Delete lore")

# News Views

@admin.route('/nius', methods=['GET', 'POST'])
@login_required
def list_nius():
    """
    List all nius entrys
    """
    check_lore()

    niuss = NewsModel.query.all()

    return render_template('admin/newses/niuses.html',
                           niuss=niuss, title="News")

@admin.route('/nius/add', methods=['GET', 'POST'])
@login_required
def add_nius():
    """
    Add a News
    """
    check_lore()

    add_news = True

    form = NiusForm()
    if form.validate_on_submit():
        nius = NewsModel(title=form.title.data,
                                newsBody=form.newsBody.data, imageUrl=form.imageUrl.data)
        try:
            # add news to the database
            db.session.add(nius)
            db.session.commit()
            flash('You have successfully added a new News entry.')
        except:
            # in case lore name already exists
            flash('Error: News title already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_nius'))

    # load department template
    return render_template('admin/newses/nius.html', action="Add",
                           add_news=add_news, form=form,
                           title="Add News")

@admin.route('/nius/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_nius(id):
    """
    Edit a news entry
    """
    check_news()

    add_news = False

    nius = NewsModel.query.get_or_404(id)
    form = NiusForm(obj=nius)
    if form.validate_on_submit():
        nius.title = form.title.data
        nius.loreBody = form.newsBody.data
        nius.imageUrl = form.imageUrl.data
        db.session.commit()
        flash('You have successfully edited the news entry.')

        # redirect to the departments page
        return redirect(url_for('admin.list_nius'))

    form.title.data = nius.title
    form.newsBody.data = nius.newsBody
    form.imageUrl.data = nius.imageUrl
    return render_template('admin/newses/nius.html', action="Edit",
                           add_news=add_news, form=form,
                           nius=nius, title="Edit news entry")

@admin.route('/nius/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_nius(id):
    """
    Delete a news entry from the database
    """
    check_news()

    nius = Lore.query.get_or_404(id)
    db.session.delete(nius)
    db.session.commit()
    flash('You have successfully deleted the news entry.')

    # redirect to the departments page
    return redirect(url_for('admin.list_nius'))

    return render_template(title="Delete news")

# Chart Views

@admin.route('/chart', methods=['GET', 'POST'])
@login_required
def list_chart():
    """
    List all hunters entrys
    """
    check_chart()

    hunters = Hunter.query.order_by(Hunter.position.asc())

    return render_template('admin/charts/chart.html',
                           hunters=hunters, title="Chart")

@admin.route('/chart/add', methods=['GET', 'POST'])
@login_required
def add_hunter():
    """
    Add a lore
    """
    check_chart()

    add_chart = True

    form = HunterForm()
    if form.validate_on_submit():
        hunter = Hunter(name=form.name.data,
                                position=form.position.data, lastPosition=form.lastPosition.data)
        try:
            # add lore to the database
            db.session.add(hunter)
            db.session.commit()
            flash('You have successfully added a new hunter.')
        except:
            # in case lore name already exists
            flash('Error: hunter name or position already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_chart'))

    # load department template
    return render_template('admin/charts/hunter.html', action="Add",
                           add_hunter=add_hunter, form=form,
                           title="Add Hunter")

@admin.route('/chart/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_hunter(id):
    """
    Edit a hunter
    """
    check_chart()

    add_hunter = False

    hunter = Hunter.query.get_or_404(id)
    form = HunterForm(obj=hunter)
    if form.validate_on_submit():
        hunter.name = form.name.data
        hunter.position = form.position.data
        hunter.lastPosition = form.lastPosition.data
        db.session.commit()
        flash('You have successfully edited the hutner data.')

        # redirect to the departments page
        return redirect(url_for('admin.list_chart'))

    form.name.data = hunter.name
    form.position.data = hunter.position
    form.lastPosition.data = hunter.lastPosition
    return render_template('admin/charts/hunter.html', action="Edit",
                           add_hunter=add_hunter, form=form,
                           hunter=hunter, title="Edit hunter data")

@admin.route('/chart/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_hunter(id):
    """
    Delete a hunter from the database
    """
    check_chart()

    hunter = Hunter.query.get_or_404(id)
    db.session.delete(hunter)
    db.session.commit()
    flash('You have successfully killed the hunter.')

    # redirect to the departments page
    return redirect(url_for('admin.list_chart'))

    return render_template(title="Kill hunter")

# Department Views

@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")

@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")

@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")

@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")

@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')

@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')

@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")

@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")

@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')

@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a department and a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    #if employee.is_admin:
     #   abort(403)

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.is_admin = form.is_admin.data
        employee.is_lore = form.is_lore.data
        employee.is_chart = form.is_chart.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')