##PARA COMENZAR A CONTRIBUIR##


El proyecto tiene dos ramas, la rama main/master y la rama dev (que es a la que se deben pushear las contribuciones)



1.clonar repositorio remoto git clone https://github.com/22818g1/tp_22818_g1.git
2.ACTUALIZA LOS CAMBIOS: git pull. Este comando es necesario ejecutar antes de comenzar a trabajar ya que trae los cambios del repositorio remoto. De este modo, nos aseguramos estar trabajando sobre la version mas nueva.
3.DONDE ESTAS PARADO: git branch  Con este comando, se muestran todas las ramas existentes y con un asterisco indica en cual estamos posicionados en ese momento.
4.Vamos a pararnos en la rama dev y vamos a crear una nueva rama a partir de ella:
	git checkout dev
	git checkout -b GF_Funcionalidad sobre la que se trabaja (Iniciales de cada uno para estadarizar)
5.Una vez hecho el desarrollo, fusiona los cambios a la rama dev y luego elimina la rama creada por la funcionalidad
	Para ello:
	git checkout dev
	git merge nombre de rama creada
	git diff rama creada  rama dev (muestra las diferencias entre ramas)
	git checkout dev (nos movemos a rama dev)
	git branch -d rama creada (borra la rama de trabajo)
	
6.Al terminar de trabajar realiza un commit : git add . / git commit -m comentario que detalle lo que estoy enviando
7.Para ver los cambios registrados y su estado: git status
8.Para subir cambios al repositorio remoto: git push origin dev (SUPER IMPORTANTE!! PUSHEAR A DEV para preservar la rama main)
9.Para ver historial de commits git log ó git log --oneline (La segunda opcion solo muestra una linea con id commit y comentario)
"# DJANGO_GRUPO1" 
