server:
	python manage.py runserver
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
check:
	python manage.py check
test:
	python manage.py test
superuser:
	python manage.py createsuperuser
changepassword:
	python manage.py changepassword
routes:
	python manage.py show_urls
shell:
	python manage.py shell