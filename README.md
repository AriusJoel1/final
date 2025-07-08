# Proyecto Final

Este repositorio tiene una aplicación Python que ejecuta análisis automatizados usando un binario externo, ofrece una API REST, y cuenta con pruebas automatizadas robustas con Pytest.

## Instalación General

```
git clone https://github.com/usuario/proyecto-final.git
cd proyecto-final
pip install pytest pytest-mock
pip install requests
chmod +x tests/stubs/fake-analyzer.sh
minikube start --driver=docker
minikube docker-env
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

