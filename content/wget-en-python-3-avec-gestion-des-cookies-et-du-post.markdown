Title: wget en python 3 avec gestion des cookies et du post
Date: 2013-02-25 21:47
Category: Python
Tags: bash, cookie, post data, Python, urllib, wget
Slug: wget-en-python-3-avec-gestion-des-cookies-et-du-post

Un petit exemple avec le site ameli, qui permet d'illustrer la gestion des cookies et du post data.

### La commande Wget dans un petit script :

	#!bash
	#!/bin/bash
	login="xxxxx"
	pass="xxxxx"

	#Récupération des premiers cookies
	wget -dO /dev/null --cookies=on --keep-session-cookies --save-cookies=cookies.txt "https://assure.ameli.fr/PortailAS/appmanager/PortailAS/assure"

	#Deuxième passage pour récupérer les cookies sécurisés
	wget -dO /dev/null --cookies=on --keep-session-cookies --save-cookies=cookies.txt --load-cookies=cookies.txt --post-data "connexioncompte_2numSecuriteSociale=$login&amp;connexioncompte_2codeConfidentiel=$pass&amp;connexioncompte_2actionEvt=connecter&amp;submit=validerFormulaire(this)" "https://assure.ameli.fr/PortailAS/appmanager/PortailAS/assure"

	#Troisième passage pour se connecter
	wget -dO index.html --cookies=on --keep-session-cookies --save-cookies=cookies.txt --load-cookies=cookies.txt --post-data  "connexioncompte_2numSecuriteSociale=$login&amp;connexioncompte_2codeConfidentiel=$pass&amp;connexioncompte_2actionEvt=connecter&amp;submit=validerFormulaire(this)" "https://assure.ameli.fr/PortailAS/appmanager/PortailAS/assure"

Pour expliquer un peu ce qui se passe, il faut faire plusieurs passages pour récupérer les cookies. Sur les deux premiers, je ne conserve pas de fichiers de sortie en envoyant les fichiers vers /dev/null.

Le point important est de bien mettre les load et save cookies, et de remplir correctement la partie post. Pour savoir ce qu'il faut mettre dans le post, un petit coup d'extension web developer de firefox fera l'affaire.

### La même chose en Python 3

	#!python
	#!/usr/bin/python3.2
	import urllib.request, urllib.parse, urllib.error
	import http.cookiejar

	#Le fichier qui va stocker les cookies
	COOKIEFILE = 'cookies.lwp'
	cj = http.cookiejar.LWPCookieJar

	#Des raccourcis pour lancer les requêtes
	urlopen = urllib.request.urlopen
	Request = urllib.request.Request
	urlencode = urllib.parse.urlencode

	#Modification de l'opener pour gérer les cookies
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	urllib.request.install_opener(opener)

	#Notre fonction pour ouvrir les pages html avec gestion des cookies et de l'encodage
	#avec gestion du retour du code erreur
	def requete(url, values):
	   data = urlencode(values)
	   data = data.encode('utf-8')
	   req = Request(url, data)
	   try:
	       handle = urlopen(req)
	   except IOError as err:
	       if hasattr(err,'reason'):
	           print(url)
	           print('Reason:',err.reason)          
	       elif hasattr(err,'code'):
	           print(url)
	           print('Code erreur',err.code)
	   else:
	       return handle

	login = 'xxxxxx'
	password = 'xxxxxx'

	url = "https://assure.ameli.fr/PortailAS/appmanager/PortailAS/assure"
	values = {'connexioncompte_2numSecuriteSociale' : login,
	         'connexioncompte_2codeConfidentiel' : password,
	         'connexioncompte_2actionEvt' : 'connecter',
	         "submit" : "validerFormulaire(this)"}

	#Deux passages pour récupérer les cookies puis le cookie sécurisé
	handle = requete(url, values)
	handle = requete(url, values)
	print('These are the cookies we have received so far :')
	for index, cookie in enumerate(cj):
	   print(index, '  :  ', cookie)

	the_page = open("the_page.html", "wb")
	the_page.write(handle.read())
	the_page.close()


Dans values, nous allons trouver l'équivalent du post de wget. Il faut l'encoder en binaire en Python 3 d'où le urlencode.

Pourquoi écrire en plusieurs lignes Python quelquechose qui tient en 3 lignes en bash :

- Je vais pouvoir réutiliser le code pour d'autres connexions
- Je vais pouvoir mutualiser du code (gestion de l'opener, de la requête, ...)
- Je vais pouvoir l'insérer dans un programme plus large


Si certains sont intéressés, j'ai le même en Python 2.
