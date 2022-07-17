from pandas import DataFrame


def obtenerAlquileres():
    return """
        SELECT * FROM alquileres
    """

def obtenerDfFromQuery(query: str, cursor) -> DataFrame:
    cursor.execute(query)
    resultado = cursor.fetchall()
    return DataFrame.from_records(resultado, columns=[col[0] for col in cursor.description])