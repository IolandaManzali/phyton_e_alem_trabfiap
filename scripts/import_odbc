import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-FQOLT90;"
    "Database=DadosRegiao;"
)
conexao = pyodbc.connect(dados_conexao)
print('Conexao Bem Sucedida')

cursor = conexao.cursor()
cursor.execute("SELECT * FROM dadosagro ")

rows = cursor.fetchall()

for row in rows:
    print(row.nome,row.clima,row.solo,row.cultura)
