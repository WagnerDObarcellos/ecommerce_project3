from app import Create_app

#Arquivo principal
#cria a aplicação flask a partir da fabrica
app = Create_app()

if __name__ == "__main__":
    app.run(debug=True)