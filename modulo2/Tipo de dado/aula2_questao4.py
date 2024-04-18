# Uma conta poupança foi aberta com um deposito de R$500,00. Esta conta é remunerada em 1% de juros ao mes. O codigo a seguir apresenta uma forma de implementação para 3 meses de acumulo de juros. Reescreva esse codigo usando apenas duas variaveis.

#juros = 1.01
#saldo = 500.0
#rendimento1 = saldo * juros 
#rendimento2 = rendimento1 * juros
#rendimento3 = rendimento2 * juros
#print("Após 3 meses meu novo saldo é:", rendimento3)

juros = 1.01
saldo = 500.0
saldo = juros * saldo
saldo = juros * saldo
saldo = juros * saldo

print("Após 3 meses meu novo saldo é:", saldo)
