from flask import render_template, request, redirect, url_for, flash
import mysql.connector

from database import conectar
from autenticacao import login_obrigatorio


def registrar_rotas_produtos(app):

    @app.route('/produtos')
    @login_obrigatorio
    def produtos():
        try:
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)

            cursor.execute("SELECT * FROM produto")
            produtos = cursor.fetchall()

            cursor.close()
            conexao.close()

            return render_template('index2.html', produtos=produtos)

        except mysql.connector.Error as err:
            return f"Erro ao buscar produtos: {err}"


    @app.route('/produtos/cadastrar', methods=['POST'])
    @login_obrigatorio
    def cadastrar_produto():
        nome_produto = request.form.get('nome_produto')
        categoria = request.form.get('categoria')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')

        try:
            conexao = conectar()
            cursor = conexao.cursor()

            comando = """
            INSERT INTO produto
            (NOME_PRODUTO, CATEGORIA, PRECO, QUANTIDADE)
            VALUES (%s, %s, %s, %s)
            """

            valores = (nome_produto, categoria, preco, quantidade)

            cursor.execute(comando, valores)
            conexao.commit()

            cursor.close()
            conexao.close()

            flash('Produto cadastrado com sucesso!')
            return redirect(url_for('produtos'))

        except mysql.connector.Error as err:
            return f"Erro ao cadastrar produto: {err}"


    @app.route('/produtos/deletar/<int:id_produto>', methods=['POST'])
    @login_obrigatorio
    def deletar_produto(id_produto):
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            comando = "DELETE FROM produto WHERE ID_PRODUTO = %s"
            valores = (id_produto,)

            cursor.execute(comando, valores)
            conexao.commit()

            cursor.close()
            conexao.close()

            flash('Produto excluído com sucesso!')
            return redirect(url_for('produtos'))

        except mysql.connector.Error as err:
            return f"Erro ao deletar produto: {err}"
