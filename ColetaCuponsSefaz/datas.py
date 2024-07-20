from datetime import datetime, timedelta

# Função para obter o primeiro e o último dia do mês anterior
def obter_primeiro_e_ultimo_dia_mes_anterior(data_atual):
    primeiro_dia_mes_atual = data_atual.replace(day=1)
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    primeiro_dia_mes_anterior = ultimo_dia_mes_anterior.replace(day=1)
    return primeiro_dia_mes_anterior, ultimo_dia_mes_anterior

# Função para percorrer os dias do mês anterior e fazer print
def percorrer_dias_mes_anterior():
    data_atual = datetime.now()
    primeiro_dia, ultimo_dia = obter_primeiro_e_ultimo_dia_mes_anterior(data_atual)
    
    dia_atual = primeiro_dia
    while dia_atual <= ultimo_dia:
        print(f"Data do dia setado: {dia_atual.strftime('%Y-%m-%d')}")
        dia_atual += timedelta(days=1)

# Chamar a função
percorrer_dias_mes_anterior()
