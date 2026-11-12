from dados import *
from calculos import *


def ler_numero(mensagem, padrao):
    while True:
        texto = input(f"{mensagem} [padrão: {padrao:.2f}]: ").strip().replace(",", ".")
        if texto == "":
            return padrao
        try:
            valor = float(texto)
            if valor > 0:
                return valor
            print("Digite um número maior que zero.")
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def mostrar_consumo():
    print("\n--- Consumo da casa exemplo (valores ESTIMADOS) ---")
    for aparelho in APARELHOS:
        kwh = kwh_por_mes(aparelho["potencia_w"], aparelho["horas_dia"], aparelho["quantidade"])
        print(f"{aparelho['nome']}: {aparelho['quantidade']} x {aparelho['potencia_w']} W, "
              f"{aparelho['horas_dia']} h/dia = {kwh:.1f} kWh/mês")
    total = consumo_total_aparelhos()
    print(f"TOTAL: {total:.1f} kWh/mês (aprox. R$ {total * TARIFA_KWH:.2f} com tarifa de R$ {TARIFA_KWH:.2f}/kWh)")


def mostrar_comparacao(consumo, tarifa, qtd_lampadas):
    led = calcular_led(qtd_lampadas, tarifa)
    solar = calcular_solar(consumo, tarifa)

    print(f"\n--- Comparação para {ANOS_ANALISE} anos ---")
    print(f"Consumo: {consumo:.1f} kWh/mês | Tarifa: R$ {tarifa:.2f}/kWh | Lâmpadas: {int(qtd_lampadas)}")

    print("\n[A] Trocar lâmpadas por LED")
    print(f"  Investimento: R$ {led['investimento']:.2f}")
    print(f"  Economia: {led['economia_kwh_mes']:.1f} kWh/mês (R$ {led['economia_reais_mes']:.2f}/mês)")
    print(f"  Saldo em {ANOS_ANALISE} anos (economia - investimento): R$ {led['saldo']:.2f}")
    if led["retorno_meses"] is not None:
        print(f"  Retorno do investimento: {led['retorno_meses']:.1f} meses")
    print(f"  CO2 evitado: {led['co2_evitado']:.1f} kg")

    print("\n[B] Energia solar fotovoltaica (renovável)")
    print(f"  Sistema estimado: {solar['kwp']:.1f} kWp (gera ~{solar['geracao_kwh_mes']:.1f} kWh/mês)")
    print(f"  Investimento: R$ {solar['investimento']:.2f}")
    print(f"  Economia: {solar['economia_kwh_mes']:.1f} kWh/mês (R$ {solar['economia_reais_mes']:.2f}/mês)")
    print(f"  Saldo em {ANOS_ANALISE} anos (economia - investimento): R$ {solar['saldo']:.2f}")
    if solar["retorno_meses"] is not None:
        print(f"  Retorno do investimento: {solar['retorno_meses'] / 12:.1f} anos")
    print(f"  CO2 evitado: {solar['co2_evitado']:.1f} kg")

    return led, solar


def mostrar_limitacoes():
    print("\n--- Limitações (leia antes de decidir) ---")
    print("- Todos os valores são ESTIMATIVAS, não resultados garantidos.")
    print("- A tarifa foi considerada constante; na prática ela muda todo ano.")
    print("- Custos de instalação variam: peça orçamentos de empresas.")
    print("- Solar exige telhado adequado, sem sombra, e depende do clima.")
    print("- Regras de compensação da energia solar (Lei 14.300/2022) podem reduzir a economia.")
    print("- Não foram considerados manutenção, troca de inversor e perda de eficiência dos painéis.")
    print("- A redução de CO2 é pequena porque a rede elétrica brasileira já é majoritariamente renovável.")
    print("- Fontes: veja docs/referencias.md")


def main():
    consumo = consumo_total_aparelhos()
    tarifa = TARIFA_KWH
    qtd_lampadas = QTD_LAMPADAS_PADRAO

    print("=== Citizen Assist AI - Assistente de Energia ===")
    print("Ajuda moradores a avaliar economia de energia e energia solar.")

    while True:
        print("\nMENU")
        print("1 - Ver consumo da casa exemplo")
        print("2 - Informar meus dados (consumo, tarifa, lâmpadas)")
        print("3 - Comparar LED x energia solar")
        print("4 - Receber recomendação")
        print("5 - Ver limitações e referências")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            mostrar_consumo()
        elif opcao == "2":
            consumo = ler_numero("Consumo mensal em kWh (veja na conta de luz)", consumo)
            tarifa = ler_numero("Tarifa em R$ por kWh (veja na conta de luz)", tarifa)
            qtd_lampadas = ler_numero("Quantas lâmpadas fluorescentes quer trocar por LED?", qtd_lampadas)
            print("Dados atualizados!")
        elif opcao == "3":
            mostrar_comparacao(consumo, tarifa, qtd_lampadas)
        elif opcao == "4":
            led, solar = mostrar_comparacao(consumo, tarifa, qtd_lampadas)
            print("\n--- Recomendação ---")
            print(gerar_recomendacao(led, solar))
            print("\nAtenção: isto é uma estimativa, não uma garantia de economia.")
        elif opcao == "5":
            mostrar_limitacoes()
        elif opcao == "0":
            print("Obrigado por usar o assistente!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()