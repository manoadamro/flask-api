## Contributing

Try to make pull requests that fulfill a single purpose (don't try to do loads of things at once)

- Write tests for any new code
- update README where applicable

---

clone the repo:
```
git clone http://github.com/manoadamro/flask-api
```

change to flask-api directory:
```
cd flask-api
```

install tox:
```
pip3 install tox
```

run the tests:
```
# for python 3.6
tox -e py36

# for python 3.7
tox -e py37

# for all of the above
tox
```

run black:
```
black ./tests/ ./flask_api
```

create a pull request!
