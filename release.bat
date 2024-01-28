py -m pip install --upgrade build
py -m build
pip install twine
twine upload dist/*
