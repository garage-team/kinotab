# KinoTab

Simple service for home library of movies and other contents in future.
Made by local free team for self.

### Quick Run 

```bash    
pip install -e kinotab_back  
manage.py migrate  
manage.py runserver
```

Create user from console through `manage.py createsuperuser`
or API for frontend  
```bash
curl --location --request POST 'http://localhost:8000/api/profile/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"email": "",
	"username": "",
	"first_name": "",
	"password": "",
	"confirm_password": ""
}'
```
