# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,redirect, url_for, session,flash
from myaccount.models import FinanceBook
from myaccount import db

finBook = Blueprint('financeBook',__name__)


@finBook.route('/bookList')
def bookList():
	#根据当前用户查找他的账本
	books = FinanceBook.query.filter_by(userId=session.get("userId")).all()

	return render_template("finBookList.html",books=books)


@finBook.route('/EditFinBook')
@finBook.route('/EditFinBook/<bookId>')
def editFinBook(bookId=None):
	book=None
	if(bookId):
		book = FinanceBook.query.filter_by(id=bookId).first()
		#if(book==None):
			#return "找不到"
	return render_template("EditFinBook.html",book=book)

@finBook.route('/saveFinBook',methods=['GET', 'POST'])
def saveFinBook():
	id = request.form.get("id")
	bookName = request.form['bookName']
	if(id):
		book = FinanceBook.query.get(id)
		book.bookName = bookName
	else:
		print("======")
		newBook = FinanceBook(bookName,session.get("userId"))
		db.session.add(newBook)
	db.session.commit()
	return redirect(url_for(".bookList"))

