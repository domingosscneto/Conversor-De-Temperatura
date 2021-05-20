def exibeMsg():
    print("Esse programa converte uma faixa de temperatura de Fahrenheit para Celsius,(para isso o usuário deve digitar F) e de Celsius para Fahrenheit (neste caso o usuário deve digitar C)")
def verificaOpcao():
    x = input("Digite F ou C:")
    return x
def exibeFahrenheitToCelsius(inicio, fim):
    for F in range (inicio, fim+1):
        C=(F-32)/1.8
        print("%f°F = %f °C" %(F,C))
def exibeCelsiusToFahrenheit(inicio, fim):
    for C in range (inicio, fim+1):
        F = (C*1.8) + 32
        print("%f°C = %fF" %(C,F))
def main():
    exibeMsg()
    op = verificaOpcao()
    inicio = int(input("Inicio do Intervalo: "))
    fim = int(input("Fim do Intervalo: "))
    if op == "F":
        exibeFahrenheitToCelsius(inicio, fim)
    else:
        exibeCelsiusToFahrenheit(inicio, fim)
main()
    
