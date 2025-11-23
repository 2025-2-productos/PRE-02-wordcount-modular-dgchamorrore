# Configuración en MacOS y Linux

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

# Configuración en Windows

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv # 1ro - crear
python -m venv .venv # probar sin el 3

.venv\Scripts\activate # 2do - activar
setup # correr en cdm 
```

# Ejecución de pruebas

Ejecute el siguiente comando en el terminal:

```bash
pytest
```