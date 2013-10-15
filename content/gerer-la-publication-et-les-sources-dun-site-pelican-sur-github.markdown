Title: Gérer la publication et les sources d'un site Pelican sur Github
Date: 2013-07-08 21:56
Category: Pelican
Tags: Pelican, Github 
Slug: gerer-la-publication-et-les-sources-dun-site-pelican-sur-github

Début d'une série de billets sur la création d'un site avec le générateur de site statique Pelican

Je commence par la fin. Comment publier son site sur github, ainsi que les sources ayant permis de créer le site ?

Mon objetcif était d'avoir une facilité de publication assez similaire de celle offerte par Octopress, avec le site sur les pages utilisateur dans un dépôt master


Créer un dépôt sur github
git init
git remote add origin git@github.com:letchap/letchap.github.io.git

git config --global user.name "Your Name"
git config --global user.email you@example.com


création du fichier .gitignore
output

git commit --allow-empty -m "initial commit"

git branch -m master source

git add .
git commit -m 'creation du source'
git push origin source

make html
ghp-import output
git push origin gh-pages:master





