# =====================================================
# DADOS E PREMISSAS DO PROJETO
# Todos os valores abaixo são ESTIMADOS (premissas).
# =====================================================

# --- Premissas gerais ---
DIAS_MES = 30          # dias considerados em um mês
ANOS_ANALISE = 10      # período de referência comum para as duas alternativas
TARIFA_KWH = 0.78      # R$ por kWh (ESTIMADA, com impostos). Exemplo da conta da luz
FATOR_CO2 = 0.0385     # kg de CO2 por kWh (fator médio da rede elétrica brasileira, MCTI). Conferir o ano

# --- Alternativa A: trocar lâmpadas fluorescentes por LED ---
POTENCIA_LAMPADA_ATUAL_W = 23   # lâmpada fluorescente compacta (ESTIMADO)
POTENCIA_LAMPADA_LED_W = 10     # lâmpada LED equivalente (ESTIMADO)
HORAS_LAMPADA_DIA = 5           # horas de uso por dia (ESTIMADO)
PRECO_LAMPADA_LED = 12.00       # R$ por lâmpada LED (ESTIMADO)
QTD_LAMPADAS_PADRAO = 10        # quantidade de lâmpadas da casa exemplo

# --- Alternativa B: energia solar fotovoltaica (conectada à rede) ---
HSP = 4.5                       # horas de sol pleno por dia em São Paulo (ESTIMADO).
EFICIENCIA_SISTEMA = 0.80       # perdas do sistema (inversor, cabos, calor) (ESTIMADO)
CUSTO_POR_KWP = 4500.00         # R$ por kWp instalado (ESTIMADO).
CUSTO_DISPONIBILIDADE_KWH = 50  # kWh mínimos cobrados mesmo com solar (ex.: ligação bifásica)

# --- Casa exemplo: aparelhos e consumo (ESTIMADO) ---
# Família de 3 a 4 pessoas, casa em São Paulo.
# Potências e horas são valores típicos estimados, não medições.
APARELHOS = [
    {"nome": "Geladeira", "potencia_w": 150, "horas_dia": 8, "quantidade": 1},
    {"nome": "Chuveiro elétrico", "potencia_w": 5500, "horas_dia": 0.5, "quantidade": 1},
    {"nome": "Lâmpadas fluorescentes", "potencia_w": 23, "horas_dia": 5, "quantidade": 10},
    {"nome": "Televisão", "potencia_w": 100, "horas_dia": 5, "quantidade": 1},
    {"nome": "Ventilador", "potencia_w": 80, "horas_dia": 6, "quantidade": 2},
    {"nome": "Notebook", "potencia_w": 100, "horas_dia": 4, "quantidade": 1},
    {"nome": "Máquina de lavar", "potencia_w": 500, "horas_dia": 0.5, "quantidade": 1},
]