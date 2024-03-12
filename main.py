from Website import create_app

app = create_app()

if __name__ == '__main__':
    #app.run(debug=True)
    from waitress import serve
    app.run(host="0.0.0.0", port=8080)
