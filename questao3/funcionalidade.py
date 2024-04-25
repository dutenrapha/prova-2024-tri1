#rotas do site (links)
from flask import render_template, url_for, redirect
from flask_login import  login_required, login_user, logout_user, current_user
from FtoB import app, database, bcrypt
from FtoB.forms import FormLogin, FormCriarConta
from FtoB.models import Usuario, Foto

@app.route("/", methods=['GET', 'POST'])
def homepage():
    form_Login = FormLogin()
    if form_Login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_Login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_Login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", usuario=usuario.username))
    return render_template("homepage.html", form=form_Login)


#TESTE
@app.route("/criarconta", methods=["GET","POST"])
def  criar_conta():
     form_CriarConta = FormCriarConta()
     if form_CriarConta.validate_on_submit():
         SenhaCrypt = bcrypt.generate_password_hash(form_CriarConta.senha.data)
         usuario = Usuario(username=form_CriarConta.username.data,
                           email=form_CriarConta.email.data,
                           senha=SenhaCrypt)
         database.session.add(usuario)
         database.session.commit()
         login_user(usuario, remember=True)
         return redirect(url_for("perfil", usuario=usuario.username))
     return render_template("criar-conta.html", form=form_CriarConta)


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)


@app.route("/logout")
@login_required
def logout():
    logout_user() #current_user
    return redirect(url_for("homepage"))