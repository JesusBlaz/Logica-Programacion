from setuptools import setup, find_packages


setup(
    name="master_logica_programacion",
    version="1.0",
    description="Código fuente para los ejercicios de lógica de programación",
    author="Jesús Blaz",
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
