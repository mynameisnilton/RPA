from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/execute_script', methods=['POST'])
def execute_script():

    python_executable = "C:\\Users\\nilto\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    script_path = "G:\\Meu Drive\\Certificados e Cursos\\Cursos\\Projetos - Python\\Desafio\\[robo].py"
    script_path = script_path.replace("[robo]","{nome_robo}") # estudar a forma que iremos pegar no POST enviado o nome do robo
    cmd = [python_executable, script_path]

    # Executa o comando
    processo = subprocess.run(cmd, capture_output=True, text=True)

    if processo.returncode!= 0:

        return jsonify({"retorno erro":processo.stderr})
    else:
        return jsonify({"status":processo.returncode,
                        "processo": "Finalizado"})


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)