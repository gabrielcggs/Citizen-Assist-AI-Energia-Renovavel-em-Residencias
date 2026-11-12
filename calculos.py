import math
from dados import *


def kwh_por_mes(potencia_w, horas_dia, quantidade=1):
    return potencia_w * horas_dia * quantidade * DIAS_MES / 1000


def consumo_total_aparelhos():
    total = 0
    for aparelho in APARELHOS:
        total += kwh_por_mes(aparelho["potencia_w"],
                             aparelho["horas_dia"],
                             aparelho["quantidade"])
    return total


def calcular_led(qtd_lampadas, tarifa):
    """Alternativa A: troca de lâmpadas por LED."""
    kwh_antes = kwh_por_mes(POTENCIA_LAMPADA_ATUAL_W, HORAS_LAMPADA_DIA, qtd_lampadas)
    kwh_depois = kwh_por_mes(POTENCIA_LAMPADA_LED_W, HORAS_LAMPADA_DIA, qtd_lampadas)

    economia_kwh_mes = kwh_antes - kwh_depois
    economia_reais_mes = economia_kwh_mes * tarifa
    investimento = qtd_lampadas * PRECO_LAMPADA_LED
    meses = ANOS_ANALISE * 12

    economia_total = economia_reais_mes * meses
    saldo = economia_total - investimento
    if economia_reais_mes > 0:
        retorno_meses = investimento / economia_reais_mes
    else:
        retorno_meses = None
    co2_evitado = economia_kwh_mes * meses * FATOR_CO2

    return {
        "investimento": investimento,
        "economia_kwh_mes": economia_kwh_mes,
        "economia_reais_mes": economia_reais_mes,
        "economia_total": economia_total,
        "saldo": saldo,
        "retorno_meses": retorno_meses,
        "co2_evitado": co2_evitado,
    }


def calcular_solar(consumo_mensal, tarifa):
    """Alternativa B: sistema solar fotovoltaico conectado à rede."""
    a_compensar = consumo_mensal - CUSTO_DISPONIBILIDADE_KWH
    if a_compensar < 0:
        a_compensar = 0

    kwp = math.ceil(a_compensar / (HSP * DIAS_MES * EFICIENCIA_SISTEMA) * 2) / 2
    geracao_kwh_mes = kwp * HSP * DIAS_MES * EFICIENCIA_SISTEMA

    compensado = min(geracao_kwh_mes, a_compensar)

    economia_reais_mes = compensado * tarifa
    investimento = kwp * CUSTO_POR_KWP
    meses = ANOS_ANALISE * 12

    economia_total = economia_reais_mes * meses
    saldo = economia_total - investimento
    if economia_reais_mes > 0:
        retorno_meses = investimento / economia_reais_mes
    else:
        retorno_meses = None
    co2_evitado = compensado * meses * FATOR_CO2

    return {
        "kwp": kwp,
        "geracao_kwh_mes": geracao_kwh_mes,
        "investimento": investimento,
        "economia_kwh_mes": compensado,
        "economia_reais_mes": economia_reais_mes,
        "economia_total": economia_total,
        "saldo": saldo,
        "retorno_meses": retorno_meses,
        "co2_evitado": co2_evitado,
    }


def gerar_recomendacao(led, solar):
    texto = "1) Comece pela troca de lâmpadas por LED: o investimento é baixo e o retorno é rápido.\n"
    if solar["retorno_meses"] is None:
        texto += ("2) Com esse consumo, a energia solar não compensa: "
                  "o consumo está no nível da taxa mínima cobrada pela distribuidora.")
    elif solar["retorno_meses"] <= ANOS_ANALISE * 12:
        texto += ("2) A energia solar tem retorno estimado dentro de "
                  f"{ANOS_ANALISE} anos. Vale pedir orçamentos reais, "
                  "se você tem telhado próprio, com sol e sem sombra.")
    else:
        texto += (f"2) A energia solar demora mais de {ANOS_ANALISE} anos para se pagar "
                  "nesta estimativa. Avalie com cuidado antes de investir.")
    return texto