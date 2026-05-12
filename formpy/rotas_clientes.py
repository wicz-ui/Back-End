from flask import render_template, request, redirect, url_for, flash
import mysql.connector

from database import conectar
from autenticacao import login_obrigatorio


def registrar_rotas_clientes(app):

    @app.route('/clientes')
    @login_obrigatorio
    def clientes():
        try:
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)

            cursor.execute("SELECT * FROM cliente")
            clientes = cursor.fetchall()

            cursor.close()
            conexao.close()

            return render_template('index.html', clientes=clientes)

        except mysql.connector.Error as err:
            return f"Erro ao buscar clientes: {err}"


    @app.route('/clientes/cadastrar', methods=['POST'])
    @login_obrigatorio
    def cadastrar_cliente():
        cpf = request.form.get('cpf')
        nome = request.form.get('primeiro_nome')
        sobrenome = request.form.get('sobrenome')
        idade = request.form.get('idade')

        try:
            conexao = conectar()
            cursor = conexao.cursor()

            comando = """
            INSERT INTO cliente
            (CPF, PRIMEIRO_NOME, SOBRENOME, IDADE)
            VALUES (%s, %s, %s, %s)
            """

            valores = (cpf, nome, sobrenome, idade)

            cursor.execute(comando, valores)
            conexao.commit()

            cursor.close()
            conexao.close()

            flash('Cliente cadastrado com sucesso!')
            return redirect(url_for('clientes'))

        except mysql.connector.Error as err:
            return f"Erro ao cadastrar cliente: {err}"


    @app.route('/clientes/deletar/<cpf>', methods=['POST'])
    @login_obrigatorio
    def deletar_cliente(cpf):
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            comando = "DELETE FROM cliente WHERE CPF = %s"
            valores = (cpf,)

            cursor.execute(comando, valores)
            conexao.commit()

            cursor.close()
            conexao.close()

            flash('Cliente excluído com sucesso!')
            return redirect(url_for('clientes'))

        except mysql.connector.Error as err:
            return f"Erro ao deletar cliente: {err}"
